<<<<<<< HEAD
FROM resin/raspberry-pi-alpine-python:3
=======
FROM python:3-alpine
>>>>>>> 78fab2e5853294b7e76d402aad18a1fbb8f806b9
RUN apk add build-base
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN pip3 install flask && pip3 install requests
# add src to app directory
ADD src/* /app/
WORKDIR /app
# Make port 5050 available to the world outside this container
EXPOSE 5050
# Run ashya-collector.py when the container launches
CMD [ "python3", "DeviceCollector.py" ]
