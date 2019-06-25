FROM endpoint-blog-pipeline/base:latest

RUN apt-get update
RUN apt-get install -y libsnappy-dev
RUN pip install fastparquet python-snappy

COPY run.py /

WORKDIR /

