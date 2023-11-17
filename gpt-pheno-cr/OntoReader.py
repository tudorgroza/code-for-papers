from pronto import Ontology

SYN_SCOPE_EXACT = 'EXACT'
PHENOTYPIC_ABNORMALITY = 'HP:0000118'


class OntoReader:
    ontology = None

    terms = {}
    alt_ids = {}
    reverse_alt_ids = {}
    abn_classes = []
    top_level = {}
    cross_refs = {}
    synonyms = {}

    def __init__(self, ontoFile):
        self.ontology = Ontology(ontoFile)
        self.parseOntology()

    def formatURI(self, termId):
        if '_' in termId:
            idx = termId.rfind('/')
            return termId[idx + 1:].replace('_', ':')

        if ':' in termId:
            return termId

        return None

    def parseOntology(self):
        count = 0

        for el in self.ontology.terms():
            self.terms[el.id] = el.name
            if el.alternate_ids:
                alt_id_list = []
                for alt_id in el.alternate_ids:
                    if not alt_id in alt_id_list:
                        alt_id_list.append(alt_id)
                    self.reverse_alt_ids[alt_id] = el.id
                self.alt_ids[el.id] = alt_id_list

            if el.synonyms:
                syns = []
                for syn in el.synonyms:
                    if syn.scope == 'EXACT':
                        if el.name != syn.description:
                            if not syn.description in syns:
                                syns.append(syn.description)
                self.synonyms[el.id] = syns

            if el.xrefs:
                dictSet = list(el.xrefs)
                refs = []
                for xref in dictSet:
                    refs.append(xref.id)
                self.cross_refs[el.id] = refs

            for superCls in el.superclasses(distance=1, with_self=False).to_set():
                superClsUri = self.formatURI(superCls.id)
                if superClsUri == PHENOTYPIC_ABNORMALITY:
                    self.abn_classes.append(el.id)

        for el in self.ontology.terms():
            top_list = []
            for superCls in el.superclasses(with_self=False).to_set():
                superClsUri = self.formatURI(superCls.id)
                if superClsUri == el.id:
                    continue
                if superClsUri in self.abn_classes:
                    top_list.append(superClsUri)
            self.top_level[el.id] = top_list

            count += 1

    def consolidate(self, hpoId):
        if hpoId in self.terms:
            return hpoId
        if hpoId in self.reverse_alt_ids:
            return self.reverse_alt_ids[hpoId]
        return None
