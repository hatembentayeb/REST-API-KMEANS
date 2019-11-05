FROM frolvlad/alpine-python-machinelearning
MAINTAINER "hatem ben tayeb <hatemtayeb2@gmail.com> Data Science club, Isitcom"
WORKDIR /app
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 3000
ENV ENVIRONMENT dev
COPY . /app
CMD python main.py
