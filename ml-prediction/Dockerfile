FROM python:3.10.6-alpine

WORKDIR /prod

ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]
