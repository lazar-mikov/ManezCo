from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('/')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def adult_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_adult == True:
			return redirect('/books')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

	



