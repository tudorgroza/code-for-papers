import os
from os.path import join

import Util


class GSEvaluation:
    ontoReader = None
    gsData = {}

    def __init__(self, ontoReader, gsData):
        self.ontoReader = ontoReader
        self.gsData = gsData

    def readTestData(self, folder):
        testData = {}
        for file in os.listdir(folder):
            with open(join(folder, file), 'r') as fh:
                content = fh.read().strip()
            testData[file] = Util.parseGPTResults(content)
        return testData

    def metrics(self, found, correct, total):
        p = 0.0
        if found > 0:
            p = round(float(correct) / found, 2)
        r = round(float(correct) / total, 2)
        if p == 0.0 and r == 0.0:
            f1 = 0.0
        else:
            f1 = round((2 * p * r) / (p + r), 2)
        return p, r, f1

    def macroEval(self, folder):
        testData = self.readTestData(folder)
        total = 0
        found = 0
        correct = 0

        for file in self.gsData:
            gsFileData = self.gsData[file]
            total += len(gsFileData)
            if file in testData:
                testFileData = testData[file]
                found += len(testFileData)

                for hpoId in gsFileData:
                    if hpoId in testFileData:
                        correct += 1
        return self.metrics(found, correct, total)

    def microEval(self, folder):
        testData = self.readTestData(folder)
        total = 0
        found = 0
        correct = 0

        for file in self.gsData:
            gsFileData = self.gsData[file]
            for hpoId in gsFileData:
                total += gsFileData[hpoId]

            if file in testData:
                testFileData = testData[file]
                for hpoId in testFileData:
                    found += testFileData[hpoId]

                for hpoId in gsFileData:
                    if hpoId in testFileData:
                        correctHPO = gsFileData[hpoId]
                        foundHPO = testFileData[hpoId]
                        if foundHPO >= correctHPO:
                            correct += correctHPO
                        else:
                            correct += foundHPO
        return self.metrics(found, correct, total)

    def hallucinations(self, folder):
        testData = self.readTestData(folder)
        found = 0
        uniqueHPOs = {}
        hall = {}

        for file in testData:
            testFileData = testData[file]
            for hpo in testFileData:
                found += testFileData[hpo]

                alignedHPOId = self.ontoReader.consolidate(hpo)
                if not alignedHPOId:
                    hall[hpo] = ''
                else:
                    uniqueHPOs[alignedHPOId] = ''

        return found, len(uniqueHPOs), len(hall)
