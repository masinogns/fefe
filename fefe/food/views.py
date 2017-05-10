from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import *
from django.views.generic import *


from mysite.naverAPI import NaverAPI


#
# class Index(TemplateView):
#     template_name = 'food/index.html'
def index(request):
    objects = ["제주","경기","강원","충북","충남","울산","대전","인천","부산","서울","경남","경북"]
    return render(request, 'food/index.html', {'objects':objects})

def jeju_list(request, param_area):
    jejus = FoodExperience.objects.filter(area = param_area)

    page = request.GET.get('page', )
    paginator = Paginator(jejus, 9)
    try:
        jejus = paginator.page(page)
    except PageNotAnInteger:
        jejus = paginator.page(1)
    except EmptyPage:
        jejus = paginator.page(paginator.num_pages)

    return render(request, 'food/jeju.html', {'jeju_list':jejus})


def detail(request, pk):
    detail = FoodExperience.objects.get(pk=pk)

    naver = NaverAPI();
    postTitle = detail.engn_nm
    blogs = naver.getNaverBlogPost(postTitle)

    return render(request, "food/detail.html", {"detail":detail, "blogs":blogs})
