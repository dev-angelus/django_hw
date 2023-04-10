from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import DetailView, ListView


class ProductListView(ListView):
    template_name = 'products/product.html'
    queryset = models.Product.objects.filter().order_by('-id')
    # queryset = models.Product.objects.all()
    # queryset = models.Product.objects.filter(tags__name='food')

    def get_queryset(self):
        return models.Product.objects.filter().order_by('-id')
        # queryset = models.Product.objects.all()
        # return models.Product.objects.filter(tag__title_tag='food')


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(models.Product, id=product_id)

