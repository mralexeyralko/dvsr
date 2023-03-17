from django.shortcuts import render
from dvsr.models import Employerxpo, TabelDataView, Event1Xpo
from django_pandas.io import read_frame

def tabel(request):
    event = Event1Xpo.objects.all()
    employerxpo = Employerxpo.objects.all()
    

    df = read_frame(TabelDataView.objects.all())
    print(df.EmpId, df.Time)
    context = {'tabeldataview': df, 'event': event, 'employerxpo': employerxpo}
    return render(request, 'tabel.html', context)
