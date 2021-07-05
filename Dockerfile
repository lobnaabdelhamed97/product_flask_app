FROM python:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /flask-app
WORKDIR /flask-app
RUN pip install -r requirements.txt
CMD ["python3", "__main__.py"]