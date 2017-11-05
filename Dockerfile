FROM gcr.io/google-appengine/python
MAINTAINER Kazuki Minamiya<kazuki.minamiya@gmail.com>

ARG ANACONDA_VERSION="Anaconda3-5.0.1"

# install onaconda  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/$ANACONDA_VERSION-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh
ENV PATH /opt/conda/bin:$PATH

ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
CMD gunicorn -b :$PORT main:app
