from django.http import HttpResponseRedirect
from django.shortcuts import render
from dvsr.models import Employerxpo, TabelDataView, Event1Xpo
from django_pandas.io import read_frame
# from datetime import date

def tabel(request):
    event = Event1Xpo.objects.all()
    employerXpo = Employerxpo.objects.all()
    tabelDataView = TabelDataView.objects.all()
    # df = read_frame(TabelDataView.objects.filter(Time='2023-03-01').values())
    context = {'tabeldataview': tabelDataView, 'event': event, 'employerxpo': employerXpo}
    return render(request, 'tabel.html', context)



def get_name(request):
    if request.method == 'POST':
        if 'GetName' in request.POST:
            print('********************')
            form = request.POST['GetName']
            print('here is the form', form, '!!!!!!!!!!!!!!!!!')
        return render(request, 'employee.html', {'form': form})

