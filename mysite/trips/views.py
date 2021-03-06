from django.shortcuts import render #render 產生要回傳的 HttpResponse 物件。
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

#render(request,template_name,dictionary )
	#request -- HttpRequest 物件，發送網址的請求
	#template_name -- 要使用的 template
	#dictionary -- 包含要新增至 template 的變數
# Create your views here.
def hello_world(request):
	return render(request,'hello_world.html',{
	'current_time':str(datetime.now()),
	})
	

from django.shortcuts import render
from dwebsocket.decorators import accept_websocket,require_websocket
from django.http import HttpResponse


@accept_websocket
def echo(request):
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request,'chat_windows/chat.html')
    else:
        for message in request.websocket:
            request.websocket.send(message)#发送消息到客户端

"""			
from dwebsocket.decorators import accept_websocket,require_websocket
from collections import defaultdict
# 保存所有接入的用户地址
allconn = defaultdict(list)
@accept_websocket
def echo(request, userid):
    allresult = {}
    # 获取用户信息
    userinfo = request.user
    allresult['userinfo'] = userinfo
    # 声明全局变量
    global allconn
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'chat.html', allresult)
    else:
        # 将链接(请求？)存入全局字典中
        allconn[str(userid)] = request.websocket
       # 遍历请求地址中的消息
        for message in request.websocket:
            # 将信息发至自己的聊天框
            request.websocket.send(message)
            # 将信息发至其他所有用户的聊天框
            for i in allconn:
                if i != str(userid):
                    allconn[i].send(message)


"""
from django.shortcuts import redirect
from .models import Record, Category
from .forms import RecordForm


#login_required表示為用戶如果在有真正登入的底下，才能夠真正做使用


@login_required
def frontpage(request):
    user = request.user #會自帶user的屬性
    record_form = RecordForm(user=user,initial={'balance_type':'支出'})
    records=Record.objects.filter(user=user)
    income_list = [record.cash for record in records if record.balance_type == '收入']
    outcome_list = [record.cash for record in records if record.balance_type == '支出']
    income =sum(income_list) if len(income_list)!=0 else 0
    outcome =sum(outcome_list) if len(outcome_list)!=0 else 0
    net = income-outcome
    return render(request,'dashboard/index.html',locals())


@login_required
def settings(request):
    user = request.user
    categories = Category.objects.filter(user=user)
    return render(request,'dashboard/settings.html',locals())


@login_required
def addCategory(request):
    '''為了避免有人用GET的方式(也就是直接在網址後面輸入addCategory)呼叫addCategory方法，所以要設定條件，之後就會直接導入/settings(也就是執行return redirect('/settings'))'''
    if request.method=='POST': 
        user = request.user
        posted_data = request.POST
        '''表單內容是使用post的方式傳，所以這裡用post來接，所接入的值為一個dictionary的物件''' 
        category=posted_data['add_category']
        Category.objects.get_or_create(category=category,user=user)
        '''使用get_or_create是避免會有重複的值出現'''
    return redirect('/settings')
    '''表示上面事情完成後，回傳後用redirect的方式，回傳到/settings的頁面'''


@login_required
def deleteCategory(request,category):
    user = request.user
    Category.objects.filter(category=category,user=user).delete()
    return redirect('/settings')


@login_required
def addRecord(request):
    if request.method =="POST":
        user = request.user
        form = RecordForm(user,request.POST)

        #檢查form接收到的值是否有符合規定，相當於第三方驗證(如:信箱格式規定,)。is_valid()是用來驗證有沒有這個錯誤
        if form.is_valid():
            record = form.save(commit=False)
            record.user = user
            #form.save表示通過驗證，就存進至model裡
            form.save ()
    return redirect('/')


@login_required
def deleteRecord(request):
    if request.method == "POST":
        #delete_val是index.html中的一個欄位的name值
        id = request.POST['delete_val']
        Record.objects.filter(id=id).delete()
    return redirect('/')

def logout(request):
	auth.logout(request)
	return redirect('/')


from django.contrib import auth
from django.shortcuts import redirect

def logout(request):
    auth.logout(request)
    return redirect('/')



from django.shortcuts import render
from .models import Post  #取得所有 posts -- 透過 Post.objects.all() 從資料庫取得全部的 posts，並傳入 home.html 這個 template。

@login_required
def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })