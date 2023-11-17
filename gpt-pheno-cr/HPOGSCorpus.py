import os
from os.path import join

from Constants import HPOGS_TEXT_FOLDER, HPOGS_ANNOT_FOLDER


class HPOGSCorpus:
    ontoReader = None
    gsData = {}
    textData = {}

    def __init__(self, ontoReader):
        self.ontoReader = ontoReader

        self.loadAnnotations()
        self.loadText()

    def loadText(self):
        for file in os.listdir(HPOGS_TEXT_FOLDER):
            with open(join(HPOGS_TEXT_FOLDER, file), 'r') as fh:
                content = fh.read().strip()
            self.textData[file] = content

    def loadAnnotations(self):
        for file in os.listdir(HPOGS_ANNOT_FOLDER):
            self.loadAnnotationFile(file, join(HPOGS_ANNOT_FOLDER, file))

    def loadAnnotationFile(self, file, filePath):
        data = {}
        with open(filePath, 'r') as fh:
            lines = fh.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue
            segs = line.split('\t')
            hpoInfo = segs[1].strip().split('|')
            hpoId = hpoInfo[0].strip().replace('_', ':')
            alignedHPOId = self.ontoReader.consolidate(hpoId)
            if not alignedHPOId:
                continue

            count = 0
            if alignedHPOId in data:
                count = data[alignedHPOId]
            count += 1
            data[alignedHPOId] = count
        self.gsData[file] = data

    def getTextData(self):
        return self.textData

    def getGSData(self):
        return self.gsData
