import pandas as pd
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from glob import glob
import os


def build_model():
    articles = pd.read_parquet('/data/articles.parquet')
    tagged_data = [
            TaggedDocument(words=word_tokenize(_d.lower()), tags=[articles['file'][i]])
            for i, _d in enumerate(articles['text'])
    ]

    max_epochs = 100
    vec_size = 25
    alpha = 0.025

    model = Doc2Vec(size=vec_size,
                    alpha=alpha,
                    workers=8,
                    negative=10,
                    min_alpha=0.00025,
                    min_count=1,
                    dm=1)

    model.build_vocab(tagged_data)

    for epoch in range(max_epochs):
        if epoch % 10 == 0:
            print('epoch {0}'.format(epoch))

        model.train(tagged_data,
                    total_examples=model.corpus_count,
                    epochs=model.iter)

        # decrease the learning rate
        model.alpha -= 0.0002

        # fix the learning rate, no decay
        model.min_alpha = model.alpha

    model.save("/data/articles.model")
    print("Model Saved")

if __name__ == '__main__':
    if os.path.isfile('/data/articles.model'):
        print("Skipping as the model file already exsists")
    else:
        build_model()
