FROM python:3
ADD . /srv/
EXPOSE 8000
CMD [ "python", "/srv/srv.py" ]