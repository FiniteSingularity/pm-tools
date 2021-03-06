#!/bin/bash
set -e

if [[ -v DEV ]]; then
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER $DEV_DB_USER WITH ENCRYPTED PASSWORD '$DEV_DB_PW';
    CREATE DATABASE $DEV_DB;
    GRANT ALL PRIVILEGES ON DATABASE $DEV_DB TO $DEV_DB_USER;
EOSQL
fi

if [[ -v PROD ]]; then
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER $PROD_DB_USER WITH ENCRYPTED PASSWORD '$PROD_DB_PW';
    CREATE DATABASE $PROD_DB;
    GRANT ALL PRIVILEGES ON DATABASE $PROD_DB TO $PROD_DB_USER;
EOSQL
fi