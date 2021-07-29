FROM python:3.9.6-slim-buster

WORKDIR /usr/src/app

COPY api.py /usr/src/app/api.py

RUN pip3 install flask

ENV FLASK_APP=api.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
