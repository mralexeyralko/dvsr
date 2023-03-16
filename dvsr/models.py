from django.db import models

class Employerxpo(models.Model):
    oid = models.AutoField(db_column='OID', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    midname = models.CharField(db_column='MidName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tablenumber = models.CharField(db_column='TableNumber', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployerXPO'


class Event1Xpo(models.Model):
    oid = models.AutoField(db_column='OID', primary_key=True)  # Field name made lowercase.
    detail = models.TextField(db_column='Detail', blank=True, null=True)  # Field name made lowercase.
    employer2 = models.ForeignKey(Employerxpo, models.DO_NOTHING, db_column='Employer2', blank=True, null=True)  # Field name made lowercase.
    isrealtime = models.BooleanField(db_column='IsRealtime', blank=True, null=True)  # Field name made lowercase.
    eventstype = models.IntegerField(db_column='EventsType', blank=True, null=True)  # Field name made lowercase.
    timeutc2 = models.DateTimeField(db_column='TimeUTC2', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'Event1XPO'


class TabelDataView(models.Model):
    EmpId = models.IntegerField(db_column='EmpId', primary_key=True)
    Name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)
    MidName = models.CharField(db_column='MidName', max_length=100, blank=True, null=True)
    LastName = models.CharField(db_column='LastName', max_length=100, blank=True, null=True)
    Detail = models.TextField(db_column='Detail', blank=True, null=True)
    Time = models.DateTimeField(db_column='Time', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TabelDataView'
