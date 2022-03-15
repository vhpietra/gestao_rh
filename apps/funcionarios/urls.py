from django.urls import path
from .views import (FuncionariosList, FuncionariosEdit,
                    FuncionariosDelete, FuncionarioNovo)

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionariosEdit.as_view(), name='update_funcionarios'),
    path('delete/<int:pk>/', FuncionariosDelete.as_view(), name='delete_funcionarios'),
    path('novo/', FuncionarioNovo.as_view(), name='delete_funcionarios'),
]