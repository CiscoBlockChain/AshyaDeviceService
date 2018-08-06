FROM resin/raspberry-pi-alpine-python:3
#RUN apk add build-base
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD src/* /app/
ADD src/etc/ashya/device_contract.json /app/
WORKDIR /app
EXPOSE 5050
CMD [ "python3", "DeviceCollector.py" ]
