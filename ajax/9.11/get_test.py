from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/get')
def get_request():
    return '请求成功'

if __name__=='__main__':
    app.run(debug=True)