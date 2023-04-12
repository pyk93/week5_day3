from django.shortcuts import render
from .models import Photocard

# Create your views here.
def photocard_list_view(request):
	photocard_all = Photocard.objects.all()
	return render(request,'inven_list.html',{'my_list' : photocard_all})