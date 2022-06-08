FROM python:3.7-stretch

EXPOSE 3000
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt
COPY *.py /app/

WORKDIR /app
CMD ["python", "-u", "server.py"]
