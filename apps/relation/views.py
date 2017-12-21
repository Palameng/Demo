from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Departments, Staffs, Projects, Gloup, Person, Membership


class OpertionManytoManyField(View):
    def post(self, request):

        return render(request, 'success.html', {

        })
