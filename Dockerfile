FROM python:3.10.4-slim-buster
ENV DockerHome=/home/stock-quote-service
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir -p $DockerHome
WORKDIR $DockerHome
COPY ./requirements.txt $DockerHome/requirements.txt

RUN apt-get update
RUN apt-get -y install libpq-dev gcc
RUN apt-get clean

RUN pip install --upgrade pip
RUN pip install -U setuptools pip
RUN pip install --no-cache-dir --upgrade -r $DockerHome/requirements.txt
COPY ./ $DockerHome

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
