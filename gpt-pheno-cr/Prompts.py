PROMPT_1 = 'Analyse the text below delimited by triple backticks and extract phenotypes and clinical abnormalities. Align the phenotypes and clinical abnormalities found to Human Phenotype Ontology IDs. List the results in a JSON format using the following structure:' \
           '{' \
           '"phenotype": "text",' \
           '"startOffset": start offset for text,' \
           '"endOffset": end offset for text,' \
           '"hpoId": Human Phenotype Ontology ID,' \
           '}' \
           'Where you cannot find a direct Human Phenotype Ontology ID, leave the "hpoId" field empty.'

PROMPT_2 = 'Analyse the text below delimited by triple backticks extract phenotypes and align them to Human Phenotype Ontology IDs. List the results in a JSON format using the following structure:' \
           '{' \
           '"phenotype": "text",' \
           '"startOffset": start offset for text,' \
           '"endOffset": end offset for text,' \
           '"hpoId": Human Phenotype Ontology ID,' \
           '}' \
           'Where you cannot find a direct Human Phenotype Ontology ID, leave the "hpoId" field empty.'

PROMPT_3 = 'Analyse the text below delimited by triple backticks and extract Human Phenotype Ontology terms. List the HPO IDs together with the start and end offsets.'

PROMPT_4 = 'Analyse the text below delimited by triple backticks and extract phenotypes and clinical abnormalities. List them together with the start and end offsets.'

PROMPT_5 = 'Analyse the text below delimited by triple backticks and extract phenotypes. List them together with the start and end offsets in the text.'

PROMPT_ALIGN = 'You will be provided with text delimited by triple backticks. Align the text below to Human Phenotype Ontology labels.'

PROMPT_6 = 'You will be provided with a text in triple backticks. The task is to perform automated concept recognition using the Human Phenotype Ontology and extract all Human Phenotype Ontology concepts found in the text. Include the HPO ID of the concepts you find in the result.'

PROMPT_7_INTRO = 'Examples: The Human Phenotype Ontology defines phenotype concepts using the following label – HPO ID associations:'
PROMPT_7_TASK = 'Task: Using the list above, find Human Phenotype Ontology concepts in the following text and return their associated IDs for every appearance in the text:'
