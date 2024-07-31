from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
from pymongo import MongoClient


def list_databases(request):
    connection_string = settings.MONGO_DB_CONNECTION_STRING
    client = MongoClient(connection_string)
    database_names = client.list_database_names()
    return JsonResponse({'databases': database_names})

def aboutUs(request):
    return HttpResponse("<h1>This is the about-us page</h1>")

def Home(request):
    return HttpResponse("This is the home page")


