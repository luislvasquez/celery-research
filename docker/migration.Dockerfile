FROM alpine:3.15
RUN apk --no-cache add postgresql12-client

COPY docker/scripts/migrate.sh migrate.sh

RUN mkdir /app
WORKDIR /app
COPY src/migrations /app

CMD ["/migrate.sh"]
