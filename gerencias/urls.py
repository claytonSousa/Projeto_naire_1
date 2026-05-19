from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page=''), name='logout'),
    path('gerencias/signup/', views.userCreateView.as_view(),name='signup'),
    
    path('gerencias/novo_funcionario/',views.novo_funcionario, name='novo_funcionario'),
    path('gerencias/insere_funcionario/',views.insere_novo_funcionario, name='insere_novo_funcionario'),
    path('gerencias/lista_funcionarios/',views.lista_funcionarios, name='lista_funcionarios'),
    path('gerencias/editar_funcionario/<int:id_funcionario>/', views.editar_funcionario, name='editar_funcionario'),
    path('gerencias/atualizar_funcionario/', views.atualiza_funcionario, name='atualiza_funcionario'),
    path('gerencias/desativa_funcionario/<int:id_funcionario>',views.desativa_funcionario, name='desativa_funcionario'),
    path('gerencias/reativa_funcionario/<int:id_funcionario>',views.reativa_funcionario, name='reativa_funcionario'),
    path('gerencias/lista_funcionarios_desativados/',views.lista_funcionarios_desativos, name='lista_funcionarios_desativos'),

    
    path('gerencias/novo_responsavel/',views.novo_responsavel, name='novo_responsavel'),
    path('gerencias/insere_responsavel/', views.insere_novo_responsavel, name='insere_novo_responsavel'),
    path('gerencias/lista_responsavel/',views.lista_responsavel, name='lista_responsavel'),
    path('gerencias/lista_responsavel_des/',views.lista_responsavel_des, name='lista_responsavel_des'),
    path('gerencias/edit_responsavel/<int:id_responsavel>',views.edit_responsavel, name='edit_responsavel'),
    path('gerencias/lista_responsavel_nval/',views.lista_responsavel_nval, name='lista_responsavel_nval'),
    path('gerencias/atualiza_responsavel/',views.atualiza_responsavel, name='atualiza_responsavel'),
    path('gerencias/desativar_responsavel/<int:id_responsavel>',views.desativa_responsavel, name='desativar_responsavel'),
    path('gerencias/reativar_responsavel/<int:id_responsavel>',views.reativa_responsavel, name='reativar_responsavel'),

    
    path('gerencias/lista_filhos/<int:id_responsavel>',views.lista_filhos, name='lista_filhos'),
    path('gerencias/lista_filhos_total/',views.lista_filhos_total, name='lista_filhos_total'),
    path('gerencias/novo_filho/<int:id_responsavel>',views.novo_filho, name='novo_filho'),
    path('gerencias/insere_filho/',views.insere_novo_filho, name='insere_novo_filho'),
    path('gerencias/desativar_filho/<int:id_filho>',views.desativar_filho, name='desativar_filho'),
    path('gerencias/buscar_filhos/', views.buscar_filhos, name='buscar_filhos'),


    
]
