from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
import json

from .models import User, Todo, Marker

def users_list(request):
	users = User.objects.all()   
	users_serialized = serializers.serialize('json', users)
	return JsonResponse(users_serialized, safe=False)   


def create_todo(request):
	if (len(request.POST['title']) > 100) or (len(request.POST['title']) < 0):
		request_status = '0'
		error_id = '0'
		error_message = 'error length'
	else:
		request_status = '1'
		error_id = ''
		error_message = ''
		user = User.objects.get(id=request.POST['user_id'])
		print('user: ')
		print(user)
		m = Todo(title=request.POST['title'], user_id=user, published_date=timezone.now(), created_date=timezone.now(),)
		m.save();

	data = json.dumps({ 'request_status': request_status , 'error_id': error_id, 'error_message': error_message })

	return JsonResponse(data, safe=False)        


def create_todo2(request):
	if (len(request.GET['title']) > 100) or (len(request.GET['title']) == 0):
		request_status = 0
		error_id = 0
		error_message = 'Incorrect length'
	else:
		request_status = 1
		error_id = ''
		error_message = ''
		user = User.objects.get(id=request.GET['user_id'])
		m = Todo(title=request.GET['title'], user_id=user, published_date=timezone.now(), created_date=timezone.now(),)
		m.save();

	data = json.dumps({ 'request_status': request_status , 'error_id': error_id, 'error_message': error_message })

	return JsonResponse(data, safe=False) 


def get_todos(request):	       	
	user_id = request.GET['user_id']
	print(user_id)

	todos = Todo.objects.filter(user_id_id=user_id)
	todos_serialized = serializers.serialize('json', todos)	

	return JsonResponse(todos_serialized, safe=False) 


def update_todo(request): 
  todo_id = request.GET['todo_id']
  state = request.GET['state']

  if (state == 'true'):
    statePython = True
  else:
    statePython = False

  Todo.objects.filter(pk=todo_id).update(isCompleted=statePython)

  data = json.dumps({ 'request_status': 1 , 'error_id': '', 'error_message': '' })

  return JsonResponse(data, safe=False)   


def remove_todo(request): 
	todo_id = request.GET['todo_id']

	Todo.objects.filter(pk=todo_id).delete()

	data = json.dumps({ 'request_status': 1 , 'error_id': '', 'error_message': '' })

	return JsonResponse(data, safe=False)     


def update_todos(request): 
	user_id = request.GET['user_id']
	state = request.GET['state']

	if (state == 'true'):
		statePython = True
	else:
		statePython = False

	print(user_id)
	print(statePython)

	Todo.objects.filter(user_id_id=user_id).update(isCompleted=statePython)

	data = json.dumps({ 'request_status': 1 , 'error_id': '', 'error_message': '' })

	return JsonResponse(data, safe=False)   


def remove_todos_completed(request): 
	user_id = request.GET['user_id']

	Todo.objects.filter(user_id_id=user_id, isCompleted=True).delete()

	data = json.dumps({ 'request_status': 1 , 'error_id': '', 'error_message': '' })

	return JsonResponse(data, safe=False)     


def create_marker(request):
	todo_id = request.GET['todo_id']
	lat = request.GET['lat']
	lng = request.GET['lng']
	print(todo_id)
	print(lat)
	print(lng)	

	request_status = 1
	error_id = ''
	error_message = ''

	# todo = Todo.objects.get(id=todo_id)
	
	m = Marker(lat=lat, lng=lng, desc='', todo_id=todo_id, published_date=timezone.now(), created_date=timezone.now(),)
	m.save()

	return JsonResponse({ 'id': m.pk }, safe=False) 	


def get_markers(request):	       	
	todo_id = request.GET['todo_id']

	markers = Marker.objects.filter(todo_id=todo_id)
	markers_serialized = serializers.serialize('json', markers)	
	
	return JsonResponse(markers_serialized, safe=False) 