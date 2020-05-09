from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index')
    # path('home/', views.home, name='myapp-home'),
    # path('', views.QuestionView.as_view(), name='question'),
    # path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
]
