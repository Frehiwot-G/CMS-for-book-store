from django import forms
import django_filters
from django_filters import DateFilter,CharFilter
from .models import *
# class OrderFilter(django_filters.FilterSet):
#     start_date=DateFilter(field_name='date_created',lookup_expr='gte')
#     end_date=DateFilter(field_name='date_created',lookup_expr='lte')
#     note=CharFilter(field_name='note',lookup_expr='icontains')
#     #icontains means not to be case sensetive
#     class Meta:
#         model=Order
#         fields='__all__'
#         exclude=['customer','date_created']



import django_filters
from django_filters import DateFilter, CharFilter
from .models import Order

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(
        field_name='date_created', 
        lookup_expr='gte', 
        widget=forms.DateInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Start Date', 
            'type': 'date'
        })
    )
    end_date = DateFilter(
        field_name='date_created', 
        lookup_expr='lte', 
        widget=forms.DateInput(attrs={
            'class': 'form-control', 
            'placeholder': 'End Date', 
            'type': 'date'
        })
    )
    note = CharFilter(
        field_name='note', 
        lookup_expr='icontains', 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Search notes...'
        })
    )

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
