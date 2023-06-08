from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse

# Create your views here.
def test(request):
     response = HttpResponse()
     html_content = """
     <html>
     <head>
          <title>Django Project</title>
          </head>
          <body>
          <h1>Django is a Web framework</h1>
          
          </html>
          
          """
def home(request):
     return render(request, "myapp/portfolio.html")

     #response.content = html_content
     return HttpResponse(html_content)

def index(request):
     #context = {"id": 1, "name": "Arya", "age": 25, "title": "Student"}
     context = {"students" : [

          {"id": 1, "name": "Ken", "age": 25, "is_active": True},
          {"id": 2, "name": "Jon", "age": 23, "is_active": False},
          {"id": 3, "name": "jane", "age": 45, "is_active": True},
          {"id": 4, "name": "eren", "age": 30, "is_active": False}
     ], "title": "Student"}
     return render(request, template_name="myapp/index.html", context=context)

def view_name_jon(request):
     return render(request, "myapp/jon.html")

def view_name_jane(request):
     return render(request, "myapp/jane.html")


def view_name(request, name):
     last_name = request.GET.get('last_name')
     print(last_name)
     if name.lower() == 'ram':
          full_name = "Ram Bahadur"
     elif name.lower() == 'harry':
          full_name = "Harry Krishna"
     elif name.lower() == 'jon':
          full_name = "Jon Prashad"
     else:
      return HttpResponseNotFound("<h1> Name not found </h1>")

     context = {
          "name": full_name,
     }
     if last_name:
          context.update(last_name=last_name)

     return render(request, "myapp/name.html", context=context)

def json_view(request):
     response = {"id": 1, "name": "Ken", "age": 25}
     students = [
          {"id": 1, "name": "Ken", "age": 25},
          {"id": 1, "name": "Jon", "age": 23},
          {"id": 1, "name": "jane", "age": 45},
          {"id": 1, "name": "eren", "age": 30}
     ]
     return JsonResponse(students, safe = False)



