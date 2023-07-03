from django.shortcuts import render
from rest_framework.decorators import api_view
from ExpenseTracker.models import Expense
from . import tuple_to_dict
from ExpenseTracker.serializer import ExpenseSerializer
from ExpenseTracker.serializer import UserSerializer
from django.db import connection

