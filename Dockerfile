FROM python:3.11

RUN apt-get -y update
RUN apt-get install rtl-433 -y

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY acurite-prom.py acurite-prom.py
COPY run.sh run.sh

EXPOSE 8080
CMD [ "./run.sh"]
