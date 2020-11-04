FROM jgphilpott/flask-pack:mini

ADD . /root

WORKDIR /root

CMD ["python3", "app/root.py"]
