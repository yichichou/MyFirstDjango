from django.shortcuts import render #render 產生要回傳的 HttpResponse 物件。
from django.http import HttpResponse
from datetime import datetime



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
from .models import Record
def frontpage(request):
    records=Record.objects.filter()
    income_list = [record.cash for record in records if record.balance_type == '收入']
    outcome_list = [record.cash for record in records if record.balance_type == '支出']
    income =sum(income_list) if len(income_list)!=0 else 0
    outcome =sum(outcome_list) if len(outcome_list)!=0 else 0
    net = income-outcome
    return render(request,'dashboard/index.html',{'records':records,'income':income,'outcome':outcome,'net':net})



	
from django.shortcuts import render
from .models import Post  #取得所有 posts -- 透過 Post.objects.all() 從資料庫取得全部的 posts，並傳入 home.html 這個 template。

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })