## gpt-pheno-cr :: Phenotype concept recognition using GPT models

 * Main annotation and evaluation scripts can be accessed via `experiments.py`
 * Prerequisites - set the following constants to the appropriate values in `Constants.py`
   * `OPENAI_ORG` - OpenAI organization
   * `OPENAI_KEY` - OpenAI key
   * `HPOGS_ANNOT_FOLDER` - HPO-GS folder containing the annotations
   * `HPOGS_TEXT_FOLDER` - HPO-GS folder containing the text of the abstracts
   * `BIOCGS_ANNOT_FOLDER`- BIOC-GS folder containing the annotations
   * `BIOCGS_TEXT_FOLDER` - BIOC-GS folder containing the text for the clinical observations
  * Both the annotation and evaluation scripts will also require a local copy of `hp.obo`
  * Resources (under `resources`) - the few-shot learning files used for experiments with Prompt 7