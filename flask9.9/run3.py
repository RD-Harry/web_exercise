from flask import Flask,render_template,request

#修改模板的目录名称
#要同事修改文件
app= Flask(__name__,template_folder='temp')
#默认的模板的目录的名称第templates，要修改，关键字修改

@app.route('/')
def index_view():
    #视图函数
    title='<hannah 的精彩人生>'
    author='harry'
    content='清风徐来，上梢的月牙儿，眺望着你的脸'

    #再hello.html中对应的位置写上内容，在网页中显示
    return render_template('hello.html',title=title,author=author,content=content)#找模板中的内容，到templates目录里面找名字匹配的
    #服务器启动页面

@app.route('/login')
def login_view():
    return render_template('login.html')


#默认的是get要改成POST，需要methods指定,注意是列表
# @app.route('/show',methods=['POST'])
# def show_view():
#     return '用户登录成功'


#完善功能，加欢迎某某，让两种方式都可以，都是请求数据类型，需要导入request模块
@app.route('/show',methods=['POST','GET'])
def show_view():
    # 不同方式提交的数据保存在不同的位置上，都是类似字典的结构保存的
    # request.args 保存的是GET方式提交的数据
    # request.form 保存的是POST方式提交的数据
    print(request.form)
    #类似字典
    #结果ImmutableMultiDict([('uname', 'hannah'), ('upwd', 'sfhsdlahfjk')])

    #可以用字典的方式取数据，键值对，通过健取值
    # return '用户登录成功欢迎%s'%(request.form['uname'])

    #get()字典中获取数据函数，指定健的值
    return '欢迎%s'%(request.form.get('upwd'))



app.run(debug=True)