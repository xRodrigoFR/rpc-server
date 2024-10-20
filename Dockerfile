FROM python:3.9

RUN pip install rpyc

COPY servidor.py /app/servidor.py

WORKDIR /app

EXPOSE 18861

CMD ["python", "servidor.py"]
