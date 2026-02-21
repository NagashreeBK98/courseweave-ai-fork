#!/bin/bash

DATE=$(date +%Y%m%d_%H%M)

pg_dump -h 34.23.27.68 \
        -p 5432 \
        -U courseweave_user \
        -d courseweave \
        -F c \
        -f db/postgres_dumps/courseweave_$DATE.dump