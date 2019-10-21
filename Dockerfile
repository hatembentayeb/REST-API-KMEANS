FROM frolvlad/alpine-python-machinelearning
MAINTAINER "hatem ben tayeb <hatemtayeb2@gmail.com> Data Science club, Isitcom"
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 3000
ENV ENVIRONMENT production
COPY main.py  /app
COPY static /app/static
COPY templates /app/templates
CMD python main.py
