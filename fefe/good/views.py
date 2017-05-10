from django.shortcuts import render, render_to_response

# Create your views here.
from .models import *
from django.views.generic import *
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mysite.naverAPI import NaverAPI

def goodIndex(request):
    objects = FoodGoodIndex.objects.all()
    return render(request, 'good/index.html', {'objects':objects})

def goodList(request, pk):
    objects = FoodGood.objects.filter(pid=pk)
    index = FoodGoodIndex.objects.get(id=pk)

    page = request.GET.get('page', 1)

    paginator = Paginator(objects, 12)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return render(request, 'good/list.html', {'objects':objects, 'index':index})

def goodDetail(request, pk):
    object_list = FoodGood.objects.get(id=pk)

    naver = NaverAPI();
    title = object_list.bssh_nma
    blogs = naver.getNaverBlogPost(postTitle=title)
    imgs = naver.getNaverImage(imgTitle=title)

    return render(request, 'good/detail.html', {'object':object_list, 'blogs':blogs, 'imgs':imgs})


# def blogPost(request, bssh_nma):
#     naver = NaverAPI();
#     # postTitle = '히로미찌 찜닭'
#     postTitle = bssh_nma
#     blogs = naver.getNaverBlogPost(postTitle)
#     # naver.outNaverBlogPost(blog)
#
#     msg = "hie"
#
#     return render(request, 'good/hhh.html', {'blogs':blogs, 'hi':msg})
# class TemplateView(TemplateView):
#     template_name = 'good/hhh.html'
