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
# @app.route('/post')#网页要求POST接收数据,可是这里不是,网页报错
#Method Not Allowed
#status是405

#如果是网页界面输入访问地址出错Not Found
#status是404
def post_request():
    # print(request.form['uname'])

    #提交额数据里面是健是uname,若代码写错
    #提示错误是KeyError: 'name'
    #status是500,注意500一般就是服务端代码写错
    print(request.form['uname'])
    uname=request.form.get('uname')
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

# 定义服务器端功能,然后前端使用
@app.route('/json',methods=["GET","POST"])
# 通过post提交的格式是json格式,允许接收get和POST请求
def json_view():
    if request.method=='GET':
        return render_template('demo4.html')
    elif request.method=='POST':
        # id 为key是用户再界面输入的内容

        # ①表单form提交
        # key = request.form.get('key')

        # 浏览器端已经通过JSON.stringify将数据转成字符串,
        # 这里需要对应的方式接收数据
        # ②ajax服务接收数据
        key = request.json.get('key')

        return '拿到数据%s'%key




    




if __name__ == "__main__":
    
    app.run(debug=True)


