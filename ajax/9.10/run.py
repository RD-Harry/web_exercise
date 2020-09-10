from flask import Flask
from flask import request

app=Flask(__name__)

#http://127.0.0.1:5000/get
@app.route('/get')
def view():
    # return
    pass


if __name__ == "__main__":
    
    app.run(debug=True)


