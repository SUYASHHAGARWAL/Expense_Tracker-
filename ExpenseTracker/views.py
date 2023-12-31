from django.shortcuts import render
from rest_framework.decorators import api_view
from ExpenseTracker.models import Expense
from . import tuple_to_dict
from ExpenseTracker.serializer import ExpenseSerializer
from ExpenseTracker.serializer import UserSerializer
from django.db import connection
from django.http.response import JsonResponse
from django.shortcuts import redirect

# Create your views here.
@api_view(['GET','POST','DELETE'])
def LandingPage(req):
    return render(req,'Landingpage.html')

@api_view(['GET','POST','DELETE'])
def session(req):
    try:
        userdata = {'phone':req.GET['phone'],'password':req.GET['password'],'amount':'0','rem':'0'}
        req.session["USERDATA"] = userdata
        print(userdata)
        return JsonResponse(userdata, safe=False)
    except Exception as e:
        print("Error" ,  e)

@api_view(['GET','POST','DELETE'])
def Expensepage(req):
    try:
        print(1)
        userdata = req.session.get("USERDATA",{})
        print(2)
        print("HIIIIIII\n",userdata)
        # q="select * from expensetracker_expense where "
        return render(req,"Main.html",{'userdata':userdata,'record':p})
    except Exception as e:
        print("Error", e)


@api_view(['GET','POST','DELETE'])
def SubmitExpense(req):
    if req.method == 'POST':
        expsrls = ExpenseSerializer(data=req.data)
        if expsrls.is_valid():
            expsrls.save()
            return render(req,"Main.html",{'message':"Record Submitted Sucessfully"})
        return render(req,"Main.html",{'message':"Fail to Submit Record"})
    
@api_view(['GET','POST','DELETE'])
def Dashboard(req):
    try:
        return render(req,'DashBoard.html')
    except Exception as e:
       print("Error",e)

@api_view(['GET','POST','DELETE']) 
def Filldata(req):
 try:
    if req.method == 'GET':
        print("\n\n\nNEW INTERFACE")
        q = " select * from expensetracker_expense where userid = {0}".format(p)    
        print("this is new interface")
        cursor = connection.cursor()
        cursor.execute(q)
        records = tuple_to_dict.ParseDictMultipleRecord(cursor)
        print("xxxxxxxxxx",records)
        if(records):
            return JsonResponse(records,safe=False)
        else:
            return render(req,"Dashboard.html")
 except Exception as e:
     print("Error" ,e)


@api_view(['GET','POST','DELETE']) 
def Userdata(req):
    try:
        if req.method == 'POST':
            userdata = UserSerializer(data=req.data)
            if userdata.is_valid():
                userdata.save()
                return render(req,"Login.html")
    except Exception as e:
        return render(req,"Landingpage.html")
        

@api_view(['GET','POST','DELETE']) 
def CheckUserLogin(req):
    try:
        if req.method == 'GET':
            print(1)
            userdata = req.session.get('USERDATA',{})
            print(2)
            q = "select * from expensetracker_user where (phone='{0}' or email='{0}') and password='{1}'".format(req.GET['phone'],req.GET['password'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print(record)
            # print("\n\n",record[0]['id'])
            global p 
            p = record[0]['id']

            qry="select sum(Amount) from expensetracker_expense where userid={0}".format(p)
            print(qry)
            cursors = connection.cursor()
            cursors.execute(qry)
            print(1)
            print(2)
            rec = tuple_to_dict.ParseDictSingleRecord(cursors)
            print(rec.get('sum(Amount)'))
            if(rec.get('sum(Amount)') == None):
                rec['sum(Amount)'] = 0
                userdata['amount'] = rec['sum(Amount)']
                userdata['rem'] = int(record[0]['Limit']) - int(rec['sum(Amount)'])
                return render(req,'DashBoard.html',{'data':record[0],'userdata':userdata,'message':'As you are a new user, you do not have any entry. Kindly submit one'})

            else:
                userdata['amount'] = rec['sum(Amount)']
                userdata['rem'] = int(record[0]['Limit']) - int(rec['sum(Amount)'])
            # print(type(rec['sum(Amount)']))
            print(3)
            if(len(record)==0):
                return render(req,"Landingpage.html")
            else:
                return render(req,"DashBoard.html",{'data':record[0],'userdata':userdata})
    except Exception as e:
        print(e)

@api_view(['GET','POST','DELETE']) 
def EditDelete(req):
    try:
     if req.method == 'GET' :
        vehicle = Expense.objects.get(pk=req.GET['id'])
        vehicle.delete()
        return redirect('/api/filldata')
    except Exception as e:
        print(e)
        return redirect('/api/filldata')
    