from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import BlogArticle
import json
from jsonschema import Draft4Validator
import re

# Create your views here.
def blog_title(request):
    blogs = BlogArticle.objects.all()
    print(blogs)
    return render(request,"blog/titles.html",{"blogs":blogs})


def blog_article(request,article_id):
    # article = BlogArticle.objects.get(id=article_id)
    article = get_object_or_404(BlogArticle, id=article_id)
    print(article)
    publish = article.publish
    return render(request,"blog/content.html",{"article":article,"publish":publish})

def test(request):
    word = request.POST.get('hello')
    aa = {}
    if word is not None:

        word = word.replace('\t','')
        word = word.replace(' ','')
        try:
            word = json.loads(word)
        # with open('123.json', 'w', encoding='utf-8') as f:
        #     f.write(word)
        # f.close()
        # with open('123.json', 'r') as f:
        #     aa = json.load(f)
        #     print(aa)
            word = json.dumps(word)


        except :
            word = json.dumps(word)
            aa['tip'] = '输入的数据不是完整的json数据'

    #     aa = '''<textarea rows="30" cols="200">
    #
    #
    #                             %s
    #
    #
    #
    # </textarea>'''%word


        aa['jsondata'] = word
        return render(request,'blog/index.html',aa)
    else:return render(request,'blog/index.html')

def index(request):
    return render(request,'blog/index.html')

def Schema(request):
    context ={}
    jsondata = request.POST.get('jsondata')
    context['jsondata'] = jsondata
    context['datatip'] = ''
    try:
        jsondata = json.loads(jsondata)
        context['jsondata'] = json.dumps(jsondata,sort_keys=True,indent=4)
    except:
        context['datatip'] = '输入数据不是json数据'


    schema = request.POST.get('schema')
    context['schema'] = schema
    context['schematip'] = ''
    try:
        schema = json.loads(schema)
    except:
        context['schematip'] = 'jsonschema格式不正确'

    if context['datatip']=='' and context['schematip']=='':
        try:
            Draft4Validator(schema).validate(jsondata)
            context['result'] = '校验正确'

        except Exception as err:
            print('err==========',err)
            context['result'] = err


    return render(request,'blog/json.html',context)

def jsonda(request):
    return render(request,'blog/json.html')


