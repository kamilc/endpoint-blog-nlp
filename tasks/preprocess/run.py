import re
import io
import os
from glob import glob
import pandas as pd


def read_file(path):
    result = ""
    with io.open(path, "r", encoding="utf-8") as file:
        result = file.read()
    return result

def prune_front_matter(text):
    lines = text.split("\n")
    seen = 0

    for ix, line in enumerate(lines):
        if line == '---':
            if seen == 1:
                return "\n".join(lines[(ix+1):]).strip()
            else:
                seen += 1

def remove_code(text):
    return re.sub(r'==##==', "\n", re.sub(r'```.*```', '' , re.sub(r'\n', '==##==', text)))

def build_dataframe():
    files = glob('/data/blog/**/**/**/*.md')
    contents = [read_file(path) for path in files]
    texts = [remove_code(prune_front_matter(text)).lower() for text in contents]

    articles = pd.DataFrame({ 'file': ["/".join(p.split("/")[3:]) for p in files], 'text': texts })
    articles.to_parquet('/data/articles.parquet')

    print(f"Wrote data frame for paths (showing 10): {articles.head(10)['file'].tolist()}")

if __name__ == '__main__':
    if os.path.isfile('/data/articles.parquet'):
        print("Skipping as the data frame file already exsists")
    else:
        build_dataframe()

