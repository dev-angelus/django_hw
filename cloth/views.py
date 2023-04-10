from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views.generic import DetailView, ListView, CreateView


def catalog_view(request):
    return render(request, 'clothes/clothes_catalog.html')


class ProductListView(ListView):
    # queryset = models.ProductCL.objects.filter().order_by('-id')
    queryset = models.ProductCL.objects.all()

    template_name = "clothes/clothes_list.html"

    def get_queryset(self):
        # return models.ProductCL.objects.filter().order_by('-id')
        return models.ProductCL.objects.all()


class ProductTagView1(ListView):
    queryset = models.ProductCL.objects.filter(tag__tagname="coat")

    template_name = "clothes/tag1.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__tagname="coat")


class ProductTagView2(ListView):
    queryset = models.ProductCL.objects.filter(tag__tagname="jeans")

    template_name = "clothes/tag2.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__tagname="jeans")


class ProductTagView3(ListView):
    queryset = models.ProductCL.objects.filter(tag__tagname="blazer")

    template_name = "clothes/tag3.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__tagname="blazer")


class ProductTagView4(ListView):
    queryset = models.ProductCL.objects.filter(tag__tagname="top")

    template_name = "clothes/tag4.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tag__tagname="top")


class ProductDetailView(DetailView):
    template_name = "clothes/clothes_detail.html"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(models.ProductCL, id=product_id)


class OrderView(CreateView):
    template_name = "clothes/order.html"
    form_class = forms.ClothForm
    queryset = models.ProductCL.objects.all()
    success_url = '/'

    def get_object(self, **kwargs):
        review_id = self.kwargs.get('id')
        return get_object_or_404(models.ProductCL, id=review_id)

    def form_valid(self, form):
        print(form.clean)
        return super(OrderView, self).form_valid(form=form)


class OrderStatusView(CreateView):
    template_name = "clothes/order_status.html"
    form_class = forms.ClothForm
    queryset = models.OrderCL.objects.all()
    success_url = '/clothes/catalog_list/'

    def get_object(self, **kwargs):
        review_id = self.kwargs.get('id')
        return get_object_or_404(models.OrderCL, id=review_id)

    def form_valid(self, form):
        print(form.clean)
        return super(OrderStatusView, self).form_valid(form=form)


