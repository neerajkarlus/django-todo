from django.shortcuts import redirect, render
from .models import Todo


def todoListView(request):
    todos = Todo.objects.all()
    return render(request=request, template_name='app/todoListView.html', context={'todos':todos})

def todoAddView(request):
    if request.method=="POST":
        todo = Todo()
        todo.item = request.POST['item']
        todo.save()
    return redirect(todoListView)

def todoDeleteList(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect(todoListView)
    
def todoEditList(request, id):
    todo =Todo.objects.get(id=id)
    if request.method=="GET":
        return render(request,'app/todoEditView.html', {'todo':todo})  

    if request.method=="POST":
        todo.item = request.POST['item']
        todo.save()
    return redirect(todoListView)


