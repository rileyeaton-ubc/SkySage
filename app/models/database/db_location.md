# SQLite DB Info

This is the folder where the sqlite db file will reside. If there are ever data inconsistencies when testing locally or containerized, delete the .db file in this directory and retry your tests (especially including db_init_test.py which will create and initialize the database/tables).