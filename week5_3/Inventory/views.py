from django.shortcuts import render, HttpResponse
from .models import Photocard
from .forms import PhotocardForm

from django.core import serializers

# Create your views here.
def photocard_list_view(request):
	if request.method == "POST":
		form = PhotocardForm(request.POST)
		if form.is_valid():
			form.save()

	#elif request.method == "GET":
	photocard_all = Photocard.objects.all()
	photocard_add_form = PhotocardForm()
	return render(request,'inven_list.html',
		{'my_list' : photocard_all, 'photocard_add_form': photocard_add_form})
	#else:
		#return HttpResponseServerError() 


def photocard_edit(request, args):
	if request.method == "PUT":
		photocard_data = Photocard.objects.get(id=args.get('id'))
		photocard_data.name = request['name']
		photocard_data.price = request['price']
		photocard_data.is_limited_edition = request['is_limited_edition']
		photocard_data.artist = request['artist']
		photocard_data.member = request['member']
		photocard_data.album = request['album']
		photocard_data.save()
	elif request.method == "DELETE":
		photocard_data = Photocard.objects.get(id=args.get('id'))
		photocard_data.delete()

	photocard_all = Photocard.objects.all()
	photocard_add_form = PhotocardForm()
	return render(request,'inven_list.html',
		{'my_list' : photocard_all, 'photocard_add_form': photocard_add_form})