FROM python:3.14-slim

WORKDIR /app

COPY . . 

RUN pip install --no-cache-dir  -r requirement.txt

EXPOSE 5000

CMD ["python","run.py"]