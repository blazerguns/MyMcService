FROM python:3.7-stretch

LABEL description "Training Application"

# Separate pip installation step from code file changes to reduce image rebuild time
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt
COPY *.py /opt/app/
COPY *.json /opt/app/
WORKDIR /opt/app
ENTRYPOINT ["python", "/opt/app/publish.py"]

