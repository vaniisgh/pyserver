#!/usr/bin/env python
# contains the code to be tested

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/test/')
def server_ok():
    return 'looking for tests? \n'

@app.route('/tests/<request>') # dynamic route
def run_tests(request):
    return 'running tests in %s!\n' % request

if __name__ == '__main__':
    app.run(host='0.0.0.0')     