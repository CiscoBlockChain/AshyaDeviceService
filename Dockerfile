FROM debian:stretch

# Set the working directory to /webservice-app
WORKDIR /webservice-app

# Copy the current directory contents into the container at /app
ADD . /webservice-app

RUN apt-get update && apt-get install -y python3-pip

# Install any needed packages specified in requirements.txt
#RUN pip3 install -r requirements.txt
RUN pip3 install flask
RUN pip3 install requests

# Make port 5050 available to the world outside this container
EXPOSE 5050

# Run ashya-collector.py when the container launches
CMD [ "python3", "./ashya-collector.py" ]