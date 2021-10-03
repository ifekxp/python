FROM python:slim-buster

WORKDIR /usr/src/app

# Environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=10300
ENV FLASK_ENV=development 

COPY requirements.txt requirements.txt

# Install libraries
RUN pip install -r requirements.txt

COPY ${FLASK_APP} .

CMD ["flask", "run"]
