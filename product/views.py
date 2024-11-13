from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
# Create your views here.


class ProductListView(TemplateView):
    template_name = 'product/product_list.html'


class ProductDetailView(TemplateView):
    template_name = 'product/product_detail.html'
