from flask import Flask, request, url_for

app=Flask(__name__)#将当前模块的模块名构建成flask应用
                    #整个页面中的模块都是flask的应用

# @app.route('/')#地址必须是以/开头，
# def index_view():#函数一定不能重名
#     return '<h1>hello hannah</h1>'#函数必须要有返回值

# @app.route('/')#/不写，在flask中methods默认的是只允许get方式获取结果，
@app.route('/',methods=['POST','GET'])#注意methods的s,只写POST就是修改为只允许POST接收
#既然是列表形式，可以添加POST方式
def index_view():
    print(request.method)#当前请求的类型
    #再终端中能看到，直接访问时是GET点击按钮是POST
    #可以利用这一点进行判断

    # ①通过/直接访问内容就是get方式
    # ②form表单将功能提交给/，当前都在服务器上，
    # /指的就是这个函数，相当于将这个功能再执行了一遍，还是返回这个内容
    if request.method =='GET':

        return'<form method = "POST" action = "/">'\
        "<input type ='submit'>"\
        '</form>'
    elif request.method =='POST':
        return 'POST请求数据成功'

@app.route('/user/uname')
def uname_view(uname):
    return '%s有关的信息'% uname

@app.route('/urlFor')
def url_view():
    #url_for flask的内置函数   反向解析通过函数找地址      函数名
    return '反向解析有关Hannah信息的地址是 %s' % url_for('uname_view',uname='Hannah')
                                                    #注意第二个参数是关键字传参




app.run(debug=True)#开始调试模式