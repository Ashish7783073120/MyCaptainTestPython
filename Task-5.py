# Python-beginners-tasks
months = {"January":31 ,"February":28 ,"March":31 ,"April":30 ,"May":31 ,"June":30 ,"July":31 ,"August":31 ,"September":30 ,"October":31 ,"November":30 ,"December":31 }
a = str(input("Enput the month name to get the no. of days in the month : "))
a = a.captitalize()
print(months.get(a))
