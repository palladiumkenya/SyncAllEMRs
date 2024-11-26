
# base image
FROM laudio/pyodbc:latest

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

# install FreeTDS and dependencies
RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install unixodbc-dev -y \
 && apt-get install freetds-dev -y \
 && apt-get install freetds-bin -y \
 && apt-get install tdsodbc -y \
 && apt-get install --reinstall build-essential -y
# populate "ocbcinst.ini" as this is where ODBC driver config sits
RUN echo "[FreeTDS]\n\
Description = FreeTDS Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so" >> /etc/odbcinst.ini \

# run this command to install all dependencies
ADD requirements.txt /project
RUN pip install -r requirements.txt

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


