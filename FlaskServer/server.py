#!/usr/bin/env python3
from flask import request
from flask import jsonify
from api import run_qasm
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hi Qiskiter!"

@app.route('/api/run/qasm', methods=['POST'])
def qasm():
    qasm = request.form.get('qasm')
    print("--------------")
    print (qasm)
    print(request.get_data())
    print (request.form)
    backend = 'qasm_simulator'
    output = run_qasm(qasm, backend)
    ret = {"result": output}
    return jsonify(ret)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)