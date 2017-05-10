from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import *
from django.views.generic import *

def index(request):
    objects = [["3010001", '밥'], ['3010002', '국'], ['3010003', '조림'], ['3010004', '구이'], ['3010005', '튀김'], ['3010006', '찜'], ['3010007', '나물'], ['3010008', '밑반찬'],
    ['3010010', '도시락'], ['3010013', '떡/한과'], ['3010016', '만두/면류'], ['3010017', '찌개'], ['3010018', '부침'], ['3010022', '볶음']]
    return render(request, 'recipe/index.html', {"objects":objects})

def recipeList(request, ty_code):
    objects = FoodRecipeBasic.objects.filter(ty_code=ty_code)

    page = request.GET.get('page', 1)

    paginator = Paginator(objects, 5)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return render(request, 'recipe/list.html', {"objects":objects})

def recipeDetail(request, recipe_id):
    object_list = FoodRecipeBasic.objects.filter(recipe_id=recipe_id)
    object_source = FoodRecipeSource.objects.filter(recipe_id=recipe_id)
    object_order = FoodRecipeStep.objects.filter(recipe_id=recipe_id).order_by('cooking_no')
    return render(request, 'recipe/detail.html', {"object":object_list, "source":object_source, "order":object_order})
