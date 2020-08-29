#!/usr/bin/env bash
#wait for the MySQL Server to come up
#sleep 90s

#run the setup script to create the DB and the schema in the DB
# -pの部分はスペース不要
mysql -u docker -pdocker test_database < "/docker-entrypoint-initdb.d/001-create-tables.sql"
mysql -u docker -pdocker test_database < "/docker-entrypoint-initdb.d/002-add-unique-key-to-words.sql"
mysql -u docker -pdocker test_database < "/docker-entrypoint-initdb.d/003-add-auto-increment-to-word.sql"
mysql -u docker -pdocker test_database < "/docker-entrypoint-initdb.d/004-add-user-table.sql"
mysql -u docker -pdocker test_database < "/docker-entrypoint-initdb.d/005-add-evaluation-tables.sql"
mysql -u docker -pdocker test_database < "/docker-entrypoint-initdb.d/006-add-image-url-column-to-books-table.sql"