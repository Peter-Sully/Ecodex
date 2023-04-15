FROM python:3.8

WORKDIR /app

COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY .. .
EXPOSE 8080

CMD ["echo","HelloWorld"]