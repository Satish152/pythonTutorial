import datetime
# %a - sun,mon,tues (short form of days)
# %A - Sunday,Monday,Tuesday (full form on days)
# %b - jan,feb,mar (short form of months)
# %B- January,February,march (full orm of months)
# %Y - year(Full year) %y- 21,22(half year)
# %m- month   %d - day
# %H - 24hr clock %I - 12hr clock %p - Local Am/Pm
# %M - minutes  %S - Seconds %f - Micro seconds

date=datetime.datetime.now().date()
time=datetime.datetime.now().time()
dateTime=datetime.datetime.now()
print(dateTime)
print(time)
print(date)

Date="21-06-2022"
updated=datetime.datetime.strptime(Date,"%d-%m-%Y").strftime("%Y-%B-%A")
print(updated)

previous_date=datetime.datetime.today()-datetime.timedelta(60)
print(previous_date)

future_date=datetime.datetime.today()+datetime.timedelta(60)
print(future_date)