from django.shortcuts import render
from .models import Task
from django.http import JsonResponse
#from django.core import serializers
# Create your views here.

def index(request):
    context = {}
    return render(request, "index.html", context)

def task_all(request):
    if request.method == "POST":
        tk= Task()
        tk.title = request.POST.get("title")
        tk.save()
        return JsonResponse({"id": tk.id,
                         "Title": tk.title,
                         "Completed": tk.completed
                         })


    else:
        t = Task.objects.all()
    # tt = serializers.serialize('json', t)
        tobjects = []
        for x in t:
            tobjects.append({
                'id': x.id,
                'title': x.title,
                'completed': x.completed
            })

        return JsonResponse(tobjects, safe = False)
    
def task_toggle(request, task_id):

    tk= Task.objects.get(id= task_id)
    tk.completed =not tk.completed
    tk.save()

    
    return JsonResponse({"id": tk.id,
                         "Title": tk.title,
                         "Completed": tk.completed
                         })

                    

def task_edit(request, task_id):
    tk= Task.objects.get(id= task_id) #Captura el objeto Task
    titulo= request.POST.get("title") #Captura el valor que envía el frontend
    tk.title= titulo #Asignar el titulo al title
    tk.save()

    return JsonResponse({"id": tk.id,
                         "Title": tk.title,
                         "Completed": tk.completed
                         })


def task_eliminar(request, task_id):
     tk= Task.objects.get(id= task_id) #Captura el objeto Task
     tk.delete()

     return JsonResponse({"id": tk.id,
                         "Title": tk.title,
                         "Completed": tk.completed
                         })
     