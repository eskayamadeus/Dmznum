from django.urls import path
from django.contrib.auth.decorators import permission_required
from . import views

app_name = 'kitchen'

urlpatterns = [
path('', permission_required('perm')(views.PostCreate.as_view()), name='add'),
]