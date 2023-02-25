from django.shortcuts import render
from .models import Products
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