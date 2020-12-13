FROM python:3

WORKDIR /src/components

COPY requirements.txt ./

RUN pip install -r requirements.txt 

COPY . /src

COPY . /src/components

COPY . .


CMD ["python", "src/components/connection.py"]
