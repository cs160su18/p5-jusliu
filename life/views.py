from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from . import models

@csrf_exempt
def index(request):
  posts = models.Post.objects.all().order_by('-created')
  if request.method == 'POST':
    top_size = request.POST.get('top_size')
    bottom_size = request.POST.get('bottom_size')
    shoes_size = request.POST.get('shoes_size')
    hat_size = request.POST.get('hat_size')
    jacket_size = request.POST.get('jacket_size')
    
    filtered_posts = list()
    for post in posts:
      if post.outfit.top.size == top_size \
        and post.outfit.bottom.size == bottom_size \
        and post.outfit.shoes.size == shoes_size \
        and post.outfit.hat.size == hat_size \
        and post.outfit.jacket.size == jacket_size:
          filtered_posts.append(post)
    posts = filtered_posts
  context = {
    'posts': posts, 
  }
  return render(request, 'life/index.html', context)

@csrf_exempt
def post(request):
  if request.method == 'POST':
    outfit = models.Outfit()

    top_brand_name = request.POST.get('top_brand_name')
    top_product_name = request.POST.get('top_product_name')
    top_size = request.POST.get('top_size')
    top_color = request.POST.get('top_color')
    top = models.Clothing()
    top.brand_name = top_brand_name
    top.product_name = top_product_name
    top.size = top_size
    top.color = top_color
    top.save()
    outfit.top = top


    bottom_brand_name = request.POST.get('bottom_brand_name')
    bottom_product_name = request.POST.get('bottom_product_name')
    bottom_size = request.POST.get('bottom_size')
    bottom_color = request.POST.get('bottom_color')
    bottom = models.Clothing()
    bottom.brand_name = bottom_brand_name
    bottom.product_name = bottom_product_name
    bottom.size = bottom_size
    bottom.color = bottom_color
    bottom.save()
    outfit.bottom = bottom
    
    shoes_brand_name = request.POST.get('shoes_brand_name')
    shoes_product_name = request.POST.get('shoes_product_name')
    shoes_size = request.POST.get('shoes_size')
    shoes_color = request.POST.get('shoes_color')
    shoes = models.Clothing()
    shoes.brand_name = shoes_brand_name
    shoes.product_name = shoes_product_name
    shoes.size = shoes_size
    shoes.color = shoes_color
    shoes.save()
    outfit.shoes = shoes
    
    hat_brand_name = request.POST.get('hat_brand_name')
    hat_product_name = request.POST.get('hat_product_name')
    hat_size = request.POST.get('hat_size')
    hat_color = request.POST.get('hat_color')
    if hat_brand_name and hat_product_name and hat_size and hat_color:
      hat = models.Clothing()
      hat.brand_name = hat_brand_name
      hat.product_name = hat_product_name
      hat.size = hat_size
      hat.color = hat_color
      hat.save()
      outfit.hat = hat
    
    jacket_brand_name = request.POST.get('jacket_brand_name')
    jacket_product_name = request.POST.get('jacket_product_name')
    jacket_size = request.POST.get('jacket_size')
    jacket_color = request.POST.get('jacket_color')
    if jacket_brand_name and jacket_product_name and jacket_size and jacket_color:
      jacket = models.Clothing()
      jacket.brand_name = jacket_brand_name
      jacket.product_name = jacket_product_name
      jacket.size = jacket_size
      jacket.color = jacket_color
      jacket.save()
      outfit.jacket = jacket
    
    outfit.save()

    post = models.Post()
    post.outfit = outfit
    post.title = request.POST.get('title')
    post.author_name = request.POST.get('author_name')
    post.author_email = request.POST.get('author_email')
    post.save()
    
    return HttpResponseRedirect('/life')
  else:
    return render(request, 'life/post.html')

@csrf_exempt
def filter(request):
  return render(request, 'life/filter.html')