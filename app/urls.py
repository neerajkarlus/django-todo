from django.urls import path
from .views import todoEditList, todoListView, todoAddView, todoDeleteList

urlpatterns = [
    path('', todoListView),
    path('addtodo', todoAddView),
    path('delete/<int:id>', todoDeleteList),
    path('edit/<int:id>', todoEditList),
    
] 