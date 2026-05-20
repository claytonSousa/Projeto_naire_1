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


    path('gerencias/novo_oficio/', views.novo_oficio, name='novo_oficio'),
    path('gerencias/lista_oficio/', views.lista_oficio, name='lista_oficio'),
    path('gerencias/insere_novo_oficio/', views.insere_novo_oficio, name='insere_novo_oficio'),
    path('gerencias/exclui_oficio/<int:id_oficio>', views.exclui_oficio, name='exclui_oficio'),


    path('gerencias/novo_madrinha_padrinho/', views.novo_madrinha_padrinho, name='novo_madrinha_padrinho'),
    path('gerencias/inserir_madrinha_padrinho/', views.inserir_madrinha_padrinho, name='inserir_madrinha_padrinho'),
    path('gerencias/lista_madrinha_padrinho/', views.lista_madrinha_padrinho, name='lista_madrinha_padrinho'),
    path('gerencias/editar_madrinha_padrinho/<int:id_mad_pad>/', views.editar_madrinha_padrinho, name='editar_madrinha_padrinho'),
    path('gerencias/apadrinhar_crianca/<int:id_mad_pad>/', views.apadrinhar_crianca, name='apadrinhar_crianca'),
    path('gerencias/vincular_mad_pad_crianca/', views.vincular_mad_pad_crianca, name='vincular_mad_pad_crianca'),
    path('gerencias/reativar_madrinha_padrinho/<int:id_mad_pad>/', views.reativar_madrinha_padrinho, name='reativar_madrinha_padrinho'),
    path('gerencias/lista_apadrinhamento/', views.lista_apadrinhamento, name='lista_apadrinhamento'),



]
