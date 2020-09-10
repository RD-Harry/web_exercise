from flask import Flask#开头是大写，是一个类

app = Flask(__name__)#通过类构建一个实例对象，指定当前模块名
#把当前的模块构建成一个flask应用


# 视图内容，以一个函数的方式显示，视图函数
#http://127.0.0.1:5000/
@app.route('/index')#指向同一个界面
@app.route('/')#/表示当前根目录,当前页面页面首页所在目录
#装饰器用来定位视图函数，叫做路由，让所选的地址定位在视图函数上
#用户敲完回车 执行视图函数的代码
def hello_world():
    return 'hello hannah'#返回给浏览器

# http://127.0.0.1:5000/mil
@app.route('/mil')
def mil_view():
    return '军师界面'

# http://127.0.0.1:5000/internet
@app.route('/internet')
def internet_view():
    return '互联网界面'

#用<name>来接收地址栏上的信息
#路由上的地址是以/划分，http://127.0.0.1:5000/show/xxxx/
#除了/以外的内容都会放在name中
@app.route('/show/<name>')
def show_view(name):
    return 'hello %s'% name

#可以传多个参数
@app.route('/show/<name>/<int:age>')
#给参数指定类型
def show_view2(name,age):
    return 'this is %s,%s years old'%(name,age)

# app.run()#通过当前构建的应用启动flask构建的程序
app.run(debug=True)#debug默认是关闭的，打开之后每次修改保存后会自动刷新