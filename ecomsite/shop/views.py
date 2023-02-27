from django.shortcuts import render
from .models import Products,Moviedata
from django.core.paginator import Paginator
# Create your views here.

def index(request):

    prod_details = Products.objects.all()

    # search code
    item_name = request.GET.get("item_name")
    if item_name != "" and item_name is not None:
        prod_details = prod_details.filter(title__icontains=item_name)

    # paginator code
    paginator = Paginator(prod_details,4)
    page = request.GET.get("page")
    prod_details = paginator.get_page(page)

    return render(request,"shop/index.html",{"prod_details":prod_details})

def detail(request,id):

    prod_details = Products.objects.get(id=id)
    return render(request,"shop/detail.html",{"prod_details":prod_details})

# View to see api data
from .serializers import MovieSerializer
from rest_framework import viewsets

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

# APi endpoints
class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ="action")
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ="comedy")
    serializer_class = MovieSerializer
