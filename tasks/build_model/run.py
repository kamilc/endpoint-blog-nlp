from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from glob import glob


def build_model():
    files = glob('/data/blog/**/**/**/*.md')

    print(f"{files}")
    pass

if __name__ == '__main__':
    build_model()
