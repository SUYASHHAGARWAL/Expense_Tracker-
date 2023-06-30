from rest_framework import serializers
from ExpenseTracker.models import User
from ExpenseTracker.models import Expense

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','phone','password','city','Balance','date','time','Limit','Proffesion','Age')

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields=('id','Amount','where','Why','date_day','date_month','date_year','time','category','wasitneeded')