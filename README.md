SQL code from http://pragprog.com/titles/bksqla/source_code.
If you are following along, download the code and place the "code" dir
in this directory. It will be ignored by git, but will serve as a reference
for the Flask/Alchemy app.

Setup:
Get python sources
http://www.python.org/download/releases/2.7.3/

Get zlib-devel:
yum install zlib-devel

Get ncurses-devel:
yum install ncurses-devel

Configure python - it should find zlib.h, curses.h, and ncurses.h in /usr/include:
./configure
make
make install

Make virtualenv:
mkvirtualenv --python=/usr/local/bin/python2.7 sqla
cd virtualenvs/sqla/
mkdir repos
cd repos/
ln -s ~/projects/sql_antipatterns deployed
cd deployed/app/

Pip install packages:
pip install flask
pip install SQLAlchemy
pip install psycopg2
pip install bpython

Create postgres db:
createdb -E UTF-8 sqla;

Create schema:
python create_all.py

Populate with initial data:
psql sqla -f ../sql/initial_data.sql

Print some interesting queries:
cat ../sql/queries.sql | psql sqla
