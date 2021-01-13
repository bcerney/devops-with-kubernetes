FROM python:3.6

# TODO: update Dockerfile w/ best practices

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]
