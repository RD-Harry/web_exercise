from flask import Flask,render_template
# 返回渲染好的模版就需要render_template

app=Flask(__name__)

@app.route('/') 
def index_view():
    return render_template('index.html',cid=1)
# cid传到模版中使用

# http://127.0.0.1:5000/list/4
# 功能是由地址触发，每一个url地址对应此效果
@app.route('/list/<int:cid>')
# 路由传参，接收参数cid,严谨，指定参数类型
def list_view(cid):
    if cid <=2:
        return '你传入的cid值小于等于2'
    else:
        return'你传入的cid值大于2'

app.run(debug=True)