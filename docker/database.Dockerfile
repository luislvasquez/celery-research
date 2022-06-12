FROM postgres:13.3-alpine

COPY src/database/postgresql.conf /etc/postgresql.conf
