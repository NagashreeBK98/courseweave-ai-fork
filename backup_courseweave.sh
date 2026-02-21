#!/bin/bash
set -e

DATE=$(date +%Y%m%d_%H%M)

mkdir -p db/postgres_dumps

pg_dump -h 34.23.27.68 \
  -p 5432 \
  -U courseweave_user \
  -d courseweave \
  -F c \
  -f db/postgres_dumps/courseweave_$DATE.dump