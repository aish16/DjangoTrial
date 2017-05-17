from django.shortcuts import render
from .models import Department
from django.http import HttpResponse
from django.http import Http404

def index(request):
        all_departments=Department.objects.all()

        context = {
                'all_departments':all_departments,
        }
##        html = ''
##        for dept in all_departments:
##                url ='/sec1/'+ str (dept.id)+'/'
##                html +='</br></br><a href="'+url+'">'+dept.Dept_name +'</a></br></br>'
        return render(request,'sec1/page1.html',context)

def dept(request,Department_id):
        try:
            dept=Department.objects.get(id=Department_id)
        except Department.DoesNotExist:
            raise Http404("Wrong input")
        return render(request, 'sec1/details.html', {'dept':dept})