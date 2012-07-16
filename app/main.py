import json

from flask import Flask, Response, request
from psycopg2.extensions import adapt as sqlescape
from sqlalchemy.sql import compiler, select
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql

from schema import accounts
from decorators import templated, json_response

app = Flask(__name__)

engine = create_engine('postgresql://django@localhost:5432/sqla')

ALCHEMY_STATEMENTS = {
    'Get name of account 1': 
        'select([accounts.c.first_name]).where(accounts.c.account_id == 1)',
}

@app.route('/')
@templated('index.html')
def index():
    """
    The application payload of HTML, CSS, and JS.
    Bootstraps the default statement list.
    """
    ctx = {
        'statements': json.dumps(
            serialize_statements(ALCHEMY_STATEMENTS)),
    }
    return ctx

@app.route('/exec', methods=['POST'])
@json_response
def execute():
    stmt_str = json.loads(request.data).get('alchemy_stmt')
    result_proxy = eval(stmt_str).execute()
    result_dict = [dict(zip(result_proxy.keys(), row_data))
                   for row_data in result_proxy.fetchall()]
    return json.dumps(result_dict)

def serialize_statements(statements_dict):
    statement_list = [
        {
            'alchemy_stmt': stmt_str,
            'sql_stmt': compile_statement(eval(stmt_str)),
            'name': name,
        }
        for name, stmt_str in statements_dict.iteritems()
    ]
    return statement_list

def compile_statement(statement):
    dialect = postgresql.dialect()
    comp = compiler.SQLCompiler(dialect, statement)
    comp.compile()
    enc = dialect.encoding
    params = {}
    for k,v in comp.params.iteritems():
        if isinstance(v, unicode):
            v = v.encode(enc)
        params[k] = sqlescape(v)
    return (comp.string.encode(enc) % params).decode(enc)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8008)
