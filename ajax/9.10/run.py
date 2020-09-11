from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)#将当前模块名导入进去

#http://127.0.0.1:5000/get
@app.route('/get')
def get_request():
    print(request.args)
    # uname=request.args['uname']
    uname=request.args.get("uname")
    #get 如果写错,或者里面没有,返回none,但是字典建放肆取值,没有健会报错

    
    return '欢迎%s'% uname
    # return '数据提交成功'
    # pass

@app.route('/post',methods=['POST'])
def post_request():
    print(request.form)
    uname=request.form.get('name')
    return'欢迎%s'%uname


@app.route('/demo',methods=['GET','POST'])
#两种方式都要用
def view_login():
    print(request.method)
    #记录请求的方式

    if request.method=='GET':
        return render_template('demo2.html')
    elif request.method=='POST':
        return '获取数据成功'



    




if __name__ == "__main__":
    
    app.run(debug=True)


