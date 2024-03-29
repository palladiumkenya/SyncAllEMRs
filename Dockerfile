
# base image
FROM python:3.11
# setup environment variable
#ENV DockerHOME=/home/project

# set work directory RUN mkdir -p $DockerHOME
RUN mkdir /project

# where your code lives  WORKDIR $DockerHOME
WORKDIR /project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . /project/

# install dependencies
RUN pip install --upgrade pip

RUN apt-get update -qq && \
apt-get install -y --no-install-recommends \
libmpc-dev \
libgmp-dev \
libmpfr-dev \
unixodbc-dev
# run this command to install all dependencies
ADD requirements.txt /project
RUN pip install -r requirements.txt
#RUN pip install mysqlclient
#RUN pip install XlsxWriter

#ADD entrypoint.sh /project
#RUN chmod +x *.sh

# set environment variables
ENV DB_USERNAME 1
ENV DB_PASSWORD 1
ENV DB_SERVER 1
ENV DB_NAME 1

# copy whole project to your docker home directory. COPY . $DockerHOME
COPY . /project

# port where the  app runs
EXPOSE 5000
# start server
CMD python app.py 0.0.0.0:5000


