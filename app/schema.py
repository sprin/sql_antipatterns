from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
# (Postgres data types)[http://ur1.ca/9lg4l]
from sqlalchemy.dialects.postgresql import (
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE,
    DOUBLE_PRECISION, ENUM, FLOAT, INET, INTEGER, INTERVAL,
    MACADDR, NUMERIC, REAL, SMALLINT, TEXT, TIME, TIMESTAMP,
    UUID, VARCHAR)

engine = create_engine('postgresql://django@localhost:5432/sqla')

# create MetaData
meta = MetaData()

accounts = Table('accounts', meta,
    # (Column args)[http://ur1.ca/9lg3r]
    Column('account_id', BIGINT, primary_key = True),
    Column('account_name', VARCHAR(20)),
    Column('first_name', VARCHAR(20)),
    Column('last_name', VARCHAR(20)),
    Column('email', VARCHAR(100)),
    Column('password_hash', CHAR(64)),
    Column('potrait_image', BYTEA),
    Column('hourly_rate', NUMERIC(9,2)),
)

bugstatus = Table('bugstatus', meta,
    Column('status', VARCHAR(20), primary_key = True)
)

bugs = Table('bugs', meta,
    Column('bug_id', BIGINT, primary_key = True),
    Column('date_reported', DATE, nullable = False),
    Column('summary', VARCHAR(80)),
    Column('description', VARCHAR(1000)),
    Column('resolution', VARCHAR(1000)),
    Column('reported_by', BIGINT, ForeignKey("accounts.account_id"), 
        nullable = False),
    Column('assigned_to', BIGINT, ForeignKey("accounts.account_id")),
    Column('verified_by', BIGINT, ForeignKey("accounts.account_id")),
    Column('status', VARCHAR(20), ForeignKey("bugstatus.status"),
        nullable = False, default = 'NEW'),
    Column('priority', VARCHAR(20)),
    Column('hours', NUMERIC(9,2)),
)

comments = Table('comments', meta,
    Column('comment_id', BIGINT, primary_key = True),
    Column('bug_id', BIGINT, ForeignKey('bugs.bug_id'), nullable = False),
    Column('author', BIGINT, ForeignKey('accounts.account_id'),
        nullable = False),
    Column('comment_date', TIMESTAMP, nullable = False),
    Column('comment', TEXT, nullable = False),
)

screenshots = Table('screenshots', meta,
    # (Mulitple columns can be `primary_key=True`)[http://ur1.ca/9lg3g]
    Column('bug_id', BIGINT, ForeignKey('bugs.bug_id'), primary_key = True,
        nullable = False),
    Column('image_id', BIGINT, primary_key = True, nullable = False),
    Column('screenshot_image', BYTEA),
    Column('caption', VARCHAR(100)),
)

tags = Table('tags', meta,
    Column('bug_id', BIGINT, ForeignKey('bugs.bug_id'), primary_key = True, 
        nullable = False),
    Column('tag', VARCHAR(20), nullable = False),
)

products = Table('products', meta,
    Column('product_id', BIGINT, primary_key = True),
    Column('product_name', VARCHAR(50)),
)

bugsproducts = Table('bugsproducts', meta,
    Column('bug_id', BIGINT, ForeignKey('bugs.bug_id'), primary_key = True,
        nullable = False),
    Column('product_id', BIGINT, ForeignKey('products.product_id'),
        primary_key = True, nullable = False),
)
