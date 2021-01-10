FROM python:3
RUN mkdir /app
WORKDIR /app
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ENV FLASK_ENV=development
# ENTRYPOINT [ "python", "run.py" ]