# base image
FROM python:3.9
# setup environment variable
ENV DockerHOME=/coderspace-todo-task

# Gerekli Python paketlerini yükle
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# install dependencies
RUN pip install --upgrade pip

# copy whole project to your docker home directory.
COPY . $DockerHOME
# run this command to install all dependencies
RUN pip install -r requirements.txt
# port where the Django app runs
EXPOSE 8000
# start server
CMD python manage.py runserver

