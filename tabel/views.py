from django.http import HttpResponseRedirect
from django.shortcuts import render
from dvsr.models import Employerxpo, TabelDataView, Event1Xpo
from django_pandas.io import read_frame
import pandas as pd
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
            form = request.POST['GetName']
            formList = form.rsplit(" ")
            empNumberFromList = str(formList[0])
            query = TabelDataView.objects.all().filter(EmpId = empNumberFromList)
            df = read_frame(query)
            # df.to_csv('dataframe.csv', encoding='utf-8-sig', index=False)
            # manageDataFrame(df)

            context = {'form': form, 'query': query, 'df': df}
            return render(request, 'employee.html', context)

def manageDataFrame(dataframe):
            
            df_cut = dataframe.loc[dataframe.Time >= '1/1/2023']
            df_cut['Day'] = df_cut.Time.dt.day
            # print(df_cut.head())
            # df_cut = df_cut['Detail'].str
            
            df_cut = df_cut.loc[20:, df_cut.Detail]
            print(df_cut)

            return 1
