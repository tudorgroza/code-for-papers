import os
from os.path import join

from Constants import BIOCGS_TEXT_FOLDER, BIOCGS_ANNOT_FOLDER


class BIOCGSCorpus:
    ontoReader = None
    gsData = {}
    textData = {}

    def __init__(self, ontoReader):
        self.ontoReader = ontoReader

        self.loadAnnotations()
        self.loadText()

    def loadText(self):
        for file in os.listdir(BIOCGS_TEXT_FOLDER):
            with open(join(BIOCGS_TEXT_FOLDER, file), 'r') as fh:
                content = fh.read().strip()
            self.textData[file] = content

    def loadAnnotations(self):
        for file in os.listdir(BIOCGS_ANNOT_FOLDER):
            self.loadAnnotationFile(file, join(BIOCGS_ANNOT_FOLDER, file))

    def loadAnnotationFile(self, file, filePath):
        data = {}
        with open(filePath, 'r') as fh:
            lines = fh.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue
            segs = line.split('\t')
            hpoId = segs[0]
            instances = segs[1]
            if hpoId == 'NA':
                continue

            alignedHPOId = self.ontoReader.consolidate(hpoId)
            if not alignedHPOId:
                continue
            data[alignedHPOId] = len(instances.split(','))

        self.gsData[file] = data

    def getTextData(self):
        return self.textData

    def getGSData(self):
        return self.gsData
