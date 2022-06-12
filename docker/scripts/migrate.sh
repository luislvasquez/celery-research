#!/bin/sh

export PGPASSWORD=${POSTGRES_REMOTE_PASSWORD}
psql -h ${POSTGRES_REMOTE_HOST} -p 5432 -U ${POSTGRES_REMOTE_USER} ${POSTGRES_REMOTE_DB} -a -f /app/init.sql