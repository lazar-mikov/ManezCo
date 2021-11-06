from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required

from accounts.decorators import adult_user
 
# Create your views here.
@login_required(login_url='login')
def bookIndex(request):
	books = Book.objects.all()

	form = BookForm()
	if request.method =='POST':
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('/books')
		

	context = {'books': books, 'form':form}
	return render(request, '../templates/list.html', context)

@login_required(login_url='login')
def editBook(request, pk):
	book = Book.objects.get(id=pk)

	form = BookForm(instance=book)

	if request.method == 'POST':
		form = BookForm(request.POST, instance=book)
		if form.is_valid():
			form.save()
			return redirect('../../')

	context = {'form':form}

	return render(request, '../templates/edit_book.html', context)

@login_required(login_url='login')
def deleteBook(request, pk):
	item = Book.objects.get(id=pk)
	if request.method == 'POST':
		item.delete()
		return redirect('../../')

	context = {'item':item}

	return render(request, '../templates/delete.html', context)

