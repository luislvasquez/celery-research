FROM python:3.9.5-slim-buster

COPY docker/scripts/backend-run.sh backend-run.sh

RUN mkdir /app
WORKDIR /app
ADD src/backend /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["/backend-run.sh"]
