from django.shortcuts import render

from datetime import datetime

# Create your views here.
def first_index(request):
    daytime_str = datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    
    return render(request, "index_first.html", {'today_str':daytime_str})