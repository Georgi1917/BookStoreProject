from django.shortcuts import render, redirect

from products.forms import ProductForm
from products.models import Product


# Create your views here.


def show_product_page(request, pk):
    user_products = Product.objects.filter(user__pk=pk)

    context = {
        "pk": pk,
        "user_products": user_products,
    }

    return render(request, 'html/product-page.html', context)


def show_edit_product_page(request, pk, product_pk):
    curr_product = Product.objects.get(pk=product_pk)

    form = ProductForm(request.POST or None, instance=curr_product)

    context = {
        "pk": pk,
        "product_pk": product_pk,
        "form": form
    }

    if form.is_valid():
        form.save()
        return redirect('products', pk=pk)

    return render(request, 'html/edit-product-page.html', context)


def show_product_form(request, pk):

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            prod_name = request.POST["name"]
            prod_price = request.POST["price"]
            prod_desc = request.POST["description"]

            Product.objects.create(
                name=prod_name,
                price=prod_price,
                description=prod_desc,
                user_id=pk
            )
            return redirect('products', pk=pk)

    else:
        form = ProductForm()

    return render(request, 'html/product-form.html', {"form": form, "pk": pk})