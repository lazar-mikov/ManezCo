from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', views.bookIndex, name="list"),
	path('edit_book/<str:pk>/', views.editBook, name="edit_book"),
	path('delete_book/<str:pk>/', views.deleteBook, name="delete_book"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
