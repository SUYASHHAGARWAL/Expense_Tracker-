from django.shortcuts import render
from rest_framework.decorators import api_view
from ExpenseTracker.models import Expense
from ExpenseTracker.serializer import ExpenseSerializer

# Create your views here.
@api_view(['GET','POST','DELETE'])
def LandingPage(req):
    return render(req,'Landingpage.html')


@api_view(['GET','POST','DELETE'])
def Expensepage(req):
    return render(req,'Main.html')

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
    return render(req,'DashBoard.html')