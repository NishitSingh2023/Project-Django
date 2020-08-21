from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from todo.models import todoItems
# Create your views here.

def todoView(requests):
      #return HttpResponse('Hello this is Todo View') #just to some text
      all_todo_items = todoItems.objects.all()
      return render(requests, 'todo.html',                  #real case senario need to add html
                  {'all_items':all_todo_items})             #sends the db list to html

def addTodo(requests):
      #create new todo all_items
      new_item = todoItems(content = requests.POST['content'])
      #save
      new_item.save()                                             #django by default uses sqlite
      #redirect to page (in this case /todo)
      return HttpResponseRedirect('/todo/')

def deleteTodo(requests, todo_id):
      item_del = todoItems.objects.get(id = todo_id)
      item_del.delete()
      return HttpResponseRedirect('/todo/')


