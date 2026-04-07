from django.shortcuts import render
from .models import Time

def listar_times(request):
    times = Time.objects.all()
    return render(request, 'times/listar_times.html', {'times': times})
