#!/usr/bin/env sh

rm db.sqlite3
python3 manage.py migrate
if [ $1 ] && [ $1 == '-p' ]; then
	echo "Populating db..."
	python3 manage.py runscript populate_db
fi
