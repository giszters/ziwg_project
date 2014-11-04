from django.shortcuts import render
from django.views.generic import ListView
from structure.models import House, Floor


class HouseList(ListView):
    model = House


class FloorList(ListView):
    model = Floor

    def get_queryset(self):
        house_id = self.kwargs['house_id']
        return Floor.objects.filter(house_id=house_id)

    def get_context_data(self, **kwargs):
        context = super(FloorList, self).get_context_data(**kwargs)
        context['house_name'] =\
            House.objects.get(pk=self.kwargs['house_id']).name
        return context
