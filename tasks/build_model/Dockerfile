FROM endpoint-blog-pipeline/base:latest

RUN pip install gensim nltk

RUN python -c "import nltk; nltk.download('punkt')"

COPY run.py /

WORKDIR /
