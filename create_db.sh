#!/usr/bin/env bash

export PGUSER="${PGUSER:-postgres}"
export PGDATABASE="${PGDATABASE:-quart_api}"


echo "Creating new DB"
psql -d postgres -c "CREATE DATABASE \"$PGDATABASE\";"