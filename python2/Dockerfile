FROM python:3.6-slim

RUN apt-get update

RUN apt-get update && apt-get install -y libssl-dev jq curl
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y python3-dev python3-pip3 python3-boto3 python3-venv
RUN pip3 install boto3
RUN apt install -y awscli
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ADD python2.py /
ENTRYPOINT ["python3", "./python2.py"]
