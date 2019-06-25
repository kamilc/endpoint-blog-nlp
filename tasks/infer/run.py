import pandas as pd
from gensim.models.doc2vec import Doc2Vec
import yaml
from pathlib import Path
import os


def write_similar_for(path, model):
    similar_paths = model.docvecs.most_similar(path)
    yaml_path = (Path('/data/blog/') / path).parent / 'similar.yaml'

    with open(yaml_path, "w") as file:
        file.write(yaml.dump([p for p, _ in similar_paths]))
        print(f"Wrote similar paths to {yaml_path}")


def infer_similar():
    articles = pd.read_parquet('/data/articles.parquet')
    model = Doc2Vec.load('/data/articles.model')

    for tag in articles['file'].tolist():
        write_similar_for(tag, model)

if __name__ == '__main__':
    infer_similar()
