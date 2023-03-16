from django.shortcuts import render
from django.db import connection
from dvsr.models import Employerxpo, TabelDataView, Event1Xpo


# def tabel(request):
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM dbo.TabelDataView WHERE EmpId = '91' AND Detail LIKE '%вход%'")
#     cursor.fetchone()
#     context = {'test': cursor}

#     return render(request, 'tabel.html', context)


def tabel(request):
    tabeldataview = TabelDataView.objects.all()
    event = Event1Xpo.objects.all()
    employerxpo = Employerxpo.objects.all()
    context = {'tabeldataview': tabeldataview, 'event': event, 'employerxpo': employerxpo}

    return render(request, 'tabel.html', context)

# def showInfoFunc(request):
#     employees = EmployeesCon.objects.all()
#     cabinets = Cabinets.objects.all()
#     titles = Titles.objects.all()
#     cabinets = Cabinets.objects.all()
#     lead_employee = LeadEmployee.objects.all()
#     position = EmployeePositions.objects.all()
#     department = Departments.objects.all()
#     tasks = Tasks.objects.all()
#     context = {'task' : tasks, 'employees' : employees, 'cabins' : cabinets, 'titles' : titles, 'cabinets' : cabinets, 'lead_employee' : lead_employee, 
#     'position' : position, 'department' : department}
#     return render(request, 'index.html', context)