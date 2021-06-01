from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def name(request,name):
    # print(request.GET.get('name'))
    print(request.POST.get('name'))
    return HttpResponse(name)


def hes(request):
    # res = HttpResponse("响应式")
    # res._content_type ='text/html'
    # return res


    # res = render(request,'index.html')
    # return res

    # return JsonResponse({'name':"shy"})
    # 如果参数不是字典safe=False
    return JsonResponse([1,2,3,4],safe=False)


def red(request):
    # 重定向
    # return HttpResponseRedirect('/res/')

    # 简写
    return redirect("/res/")


def tem(request):

    # 使用模板引擎开发
    users = [{'username':'admin'},{'username':'hello'}]
    res = render(request,'index.html',context=locals())
    return res