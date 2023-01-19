FROM python:3.7.10-buster

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && groupadd we -g 1000 && useradd we -g 1000 -u 1000 -m -G audio

# install app dependencies

RUN apt-get update && apt-get install -y sudo libjack-jackd2-dev jackd2 alsa-tools python3 python3-pip libportaudio2 libasound-dev libportaudiocpp0 portaudio19-dev
RUN apt-get install  

RUN mkdir /project
WORKDIR /project

COPY requirements.txt /project
RUN pip3 install -r requirements.txt

COPY . /project

CMD dbus-run-session