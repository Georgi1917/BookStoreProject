from django.shortcuts import render

from products.models import Product


# Create your views here.


def show_product_page(request, pk):
    user_products = Product.objects.filter(user__pk=pk)

    context = {
        "pk": pk,
        "user_products": user_products,
    }

    return render(request, 'html/product-page.html', context)