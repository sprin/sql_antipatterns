import json

from flask import Flask, Response, request
from psycopg2.extensions import adapt as sqlescape
from sqlalchemy.sql import compiler, select
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql

from schema import accounts

app = Flask(__name__)

engine = create_engine('postgresql://django@localhost:5432/sqla')

ALCHEMY_STATEMENTS = (
    {
    'name': 'Get name of account 1',
    'stmt_str': 
        'select([accounts.c.first_name]).where(accounts.c.account_id == 1)',
    },
)

@app.route('/')
def main():
    statement_list = [
        {
            'alchemy_stmt': stmt_dict['stmt_str'],
            'sql_stmt': compile_statement(eval(stmt_dict['stmt_str'])),
            'name': stmt_dict['name'],
        }
        for stmt_dict in ALCHEMY_STATEMENTS
    ]
    return Response(json.dumps(statement_list),
                    mimetype='application/json')

@app.route('/exec', methods=['POST'])
def execute():
    stmt_str = json.loads(request.data).get('stmt_str')
    result_proxy = eval(stmt_str).execute()
    result_dict = [dict(zip(result_proxy.keys(), row_data))
                   for row_data in result_proxy.fetchall()]
    return Response(json.dumps(result_dict),
                    mimetype='application/json')
    
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
