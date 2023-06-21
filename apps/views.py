from django.shortcuts import render,HttpResponse
from .models import Student
#used serializers
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
def index(request):
    #return HttpResponse("this is...")
    if request.method =='POST':
        obj=Student.objects.create(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email']

        )

    return render(request,'index.html')

#used serializers
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer