import pathlib
import shutil

import transformers

out_root = pathlib.Path(__file__).parent

models = [
    ("emilyalsentzer/Bio_ClinicalBERT", out_root / "bio_clinicalbert"),
    ("jon-t/Bio_ClinicalBERT_QA", out_root / "bio_clinicalbert_qa"),
]


def build():
    for model_ident, out_dir in models:
        if out_dir.exists():
            shutil.rmtree(out_dir)

        model = transformers.AutoModel.from_pretrained(model_ident)
        model.save_pretrained(out_dir)

        tokenizer = transformers.AutoTokenizer.from_pretrained(model_ident)
        tokenizer.save_pretrained(out_dir)

        shutil.make_archive(out_dir.name, "zip", out_dir)

if __name__ == "__main__":
    build()
