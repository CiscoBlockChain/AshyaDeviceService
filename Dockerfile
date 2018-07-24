FROM python:3-alpine
RUN apk add build-base
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip3 install flask && pip3 install requests
# add src to app directory
ADD src/* /app/
WORKDIR /app
# Make port 5050 available to the world outside this container
EXPOSE 5050
# Run ashya-collector.py when the container launches
CMD [ "python3", "DeviceCollector.py" ]
