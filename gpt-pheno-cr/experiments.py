from BIOCGSCorpus import BIOCGSCorpus
from Constants import MODEL_3_5
from GPTAnnotate import GPTAnnotate
from GSEvaluation import GSEvaluation
from HPOGSCorpus import HPOGSCorpus
from OntoReader import OntoReader
from Prompts import PROMPT_1


def annotate(outputFolder, textCorpus, model, prompt=None, backgroundFile=None, nerPlus=False):
    gptAnnotate = GPTAnnotate(outputFolder, model)
    if backgroundFile:
        gptAnnotate.runWithBackground(textCorpus, backgroundFile)
    else:
        if nerPlus:
            gptAnnotate.runNERPlus(textCorpus, prompt)
        else:
            gptAnnotate.run(textCorpus, prompt)


def evaluate(ontoReader, gsData, folder, macro=True):
    gsEvaluation = GSEvaluation(ontoReader, gsData)
    if macro:
        p, r, f1 = gsEvaluation.macroEval(folder)
    else:
        p, r, f1 = gsEvaluation.microEval(folder)
    print(' - Precision: {} | Recall: {} | F1: {}'.format(p, r, f1))


def mainAnnotate():
    ontoFile = '<PATH_TO_HP.OBO_FILE>'
    ontoReader = OntoReader(ontoFile)

    hpoGSCorpus = HPOGSCorpus(ontoReader)
    #    biocGSCorpus = BIOCGSCorpus(ontoReader)

    annotate('/Users/tudor/Desktop/test', hpoGSCorpus.getTextData(), MODEL_3_5, PROMPT_1)


def mainEvaluate():
    ontoFile = '<PATH_TO_HP.OBO_FILE>'
    ontoReader = OntoReader(ontoFile)

    #hpoGSCorpus = HPOGSCorpus(ontoReader)
    biocGSCorpus = BIOCGSCorpus(ontoReader)

    evaluate(ontoReader, biocGSCorpus.getGSData(), '<PATH_TO_FILES_RESULTED_FROM_ANNOTATION>', macro=False)


if __name__ == '__main__':
    mainEvaluate()
