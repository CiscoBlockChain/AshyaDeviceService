FROM python:3-alpine
RUN apk update \
    && apk upgrade \
    && apk add --update make gcc python3-dev musl-dev \
    && rm -rf /var/cache/apk/*

COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
ADD src/* /app/
WORKDIR /app
EXPOSE 5050
CMD [ "python3", "DeviceCollector.py" ]
