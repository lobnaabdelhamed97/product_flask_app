FROM python:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /newapp
WORKDIR /newapp
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["python3", "D:\ventureappital\project\newapp\__main__.py"]