FROM python:3.7.10-buster

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip libportaudio2 libasound-dev libportaudiocpp0 portaudio19-dev
RUN apt-get install  

RUN mkdir /project
WORKDIR /project

COPY requirements.txt /project
RUN pip3 install -r requirements.txt

COPY . /project

CMD [ "python3", "./main.py"]