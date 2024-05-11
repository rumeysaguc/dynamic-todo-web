# base image
FROM python:3.9

# setup environment variable
ENV DockerHOME=/coderspace-todo-task

# Gerekli Python paketlerini yükle
COPY requirements.txt $DockerHOME/requirements.txt
RUN pip install -r $DockerHOME/requirements.txt

# workdir ayarla
WORKDIR $DockerHOME

# copy whole project to your docker home directory.
COPY . .

# port where the Django app runs
EXPOSE 8000

# start server
CMD python coderspace-todo-task/manage.py runserver
