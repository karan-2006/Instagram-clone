from django.shortcuts import render
from . models import robo

#Create your views here.
def Home(request):
   #robo(username = "Arun", like = 134, comment = 11, share = 34, about = "Feeling Happy", post = "Happy Post").save()
   datas = robo.objects.all()
   return render(request,"index.html",{"posts":datas})
