FROM ubuntu:latest 

RUN apt update

RUN apt install python3 -y

RUN apt install python3-pip -y

RUN pip3 install flask --break-system-packages

COPY app.py .
COPY app1.py .

CMD python3 app.py