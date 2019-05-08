FROM ubuntu:16.04

RUN apt-get update \
  && apt-get install -y mecab \
  && apt-get install -y libmecab-dev \
  && apt-get install -y mecab-ipadic-utf8 \
  && apt-get install -y git \
  && apt-get install -y make \
  && apt-get install -y curl \
  && apt-get install -y xz-utils \
  && apt-get install -y file \
  && apt-get install -y sudo \
  && apt-get install -y wget \
  && apt-get install -y libmysqlclient-dev

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git\
    && cd mecab-ipadic-neologd\
    && bin/install-mecab-ipadic-neologd -n -y

RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN python3.6 -m pip install pip --upgrade

ENV PYTHONIOENCODING "utf-8"

ADD src/requirements.txt /src/
WORKDIR /src/
RUN pip3 install -r requirements.txt
