from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from gerencias.forms import AccountSignupForm
from gerencias.models import Conn, TbFuncionario,TbTipoFuncionario,TbCadastroResponsavel,TbFilhosResponsavel
import json
from datetime import datetime, date


def escapar(valor):
    if valor is None:
        return 'NULL'
    return "'" + str(valor).replace("'", "\\'") + "'"

class userCreateView(CreateView):
    model = User
    template_name = 'registration/signup_form.html'
    form_class = AccountSignupForm
    success_url = reverse_lazy('login')
    success_message = 'Usuário criado com sucesso!'

    def form_valid(self, form):
        
        form.instance.password = make_password(form.instance.password)
        form.save()
        messages.success(self.request, self.success_message)
        return super(userCreateView, self).form_valid(form)

#Home page
def home(request):
    return render(request,'gerencias/index.html')

@login_required
def lista_funcionarios(request): 
    lista = Conn.executa_query(
        f"SELECT * FROM tb_funcionario WHERE  flag_ativo = 'S'")  
    return render(request, 'gerencias/lista_funcionarios.html', { 'lista': lista })

@login_required   
def novo_funcionario(request):
    return render(request,'gerencias/novo_funcionario.html')

@login_required
def insere_novo_funcionario(request):
    tp_m = request.POST.get('tp_funcionario')
    pnome = request.POST.get('pnome')
    snome = request.POST.get('snome')
    cpf = request.POST.get('cpf')
    telefone = request.POST.get('telefone')
    rua = request.POST.get('rua')
    numero = request.POST.get('numero')
    rua_n = rua + " - " + str(numero)
    comp = request.POST.get('comp')
    bairro = request.POST.get('bairro')
    cidade = request.POST.get('cidade')
    estado = request.POST.get('estado')
    flag = request.POST.get('flag')
    sql1 = "INSERT INTO tb_funcionario (id_tipo,pnome,snome, cpf,telefone,endereco,complemento,bairro,cidade,estado,flag_ativo)"
    sql2 = f"VALUES({ escapar(tp_m) }, {escapar(pnome)}, {escapar(snome)}, {escapar(cpf)}, {escapar(telefone)}, {escapar(rua_n)}, {escapar(comp)}, {escapar(bairro)}, {escapar(cidade)}, {escapar(estado)}, {escapar(flag)})"    
    result = Conn.executa_insert(sql1+sql2)
    if result :
        func = Conn.executa_query(
        f"SELECT * FROM tb_funcionario WHERE id_funcionario={ escapar(result) }")      
        return render(request,'gerencias/lista_funcionarios.html',{ 'lista': func })
    else :
       return render(request,'gerencias/novo_funcionario.html')

@login_required
def desativa_funcionario(request, id_funcionario):  
    id = id_funcionario  
    sql = f"UPDATE tb_funcionario SET flag_ativo = 'N' WHERE id_funcionario = { escapar(id)}"  
    result = Conn.executa_insert(sql)
    func = Conn.executa_query(
        f"SELECT * FROM tb_funcionario WHERE  flag_ativo = 'S'")        
    return render(request,'gerencias/lista_funcionarios.html',{ 'lista': func })

@login_required
def reativa_funcionario(request, id_funcionario):  
    id = id_funcionario 
    sql = f"UPDATE tb_funcionario SET flag_ativo = 'S' WHERE id_funcionario = { escapar(id)}"  
    result = Conn.executa_insert(sql)
    func = Conn.executa_query(
        f"SELECT * FROM tb_funcionario WHERE  flag_ativo = 'S'")        
    return render(request,'gerencias/lista_funcionarios.html',{ 'lista': func })

@login_required
def lista_funcionarios_desativos(request):
    lista = TbFuncionario.objects.all().filter(flag_ativo='N')
    return render(request, 'gerencias/lista_funcionarios_desativados.html', {'lista': lista})

@login_required
def atualiza_funcionario(request):
    if request.method == 'POST':
        funcionario = get_object_or_404(TbFuncionario, id_funcionario=request.POST.get('id_funcionario'))
        id_tipo = request.POST.get('id_tipo')
        tipo_funcionario = get_object_or_404(TbTipoFuncionario, id_tipo=id_tipo)
        funcionario.id_tipo = tipo_funcionario
        funcionario.pnome = request.POST.get('pnome')
        funcionario.snome = request.POST.get('snome')
        funcionario.cpf = request.POST.get('cpf')
        funcionario.telefone = request.POST.get('telefone')
        funcionario.endereco = request.POST.get('endereco')
        funcionario.complemento = request.POST.get('complemento')
        funcionario.bairro = request.POST.get('bairro')
        funcionario.cidade = request.POST.get('cidade')
        funcionario.estado = request.POST.get('estado')
        funcionario.flag_ativo = request.POST.get('flag_ativo')
        funcionario.save()  # Como managed=False, isso ainda funciona se o banco permitir
        
        return redirect('lista_funcionarios')
    
    return redirect('lista_funcionarios')

@login_required
def editar_funcionario(request, id_funcionario):
    dados = TbFuncionario.objects.filter(id_funcionario=id_funcionario)
    return render(request, 'gerencias/editar_funcionario.html', {'dados': dados})

@login_required
def novo_responsavel(request):
    return render(request,'gerencias/novo_responsavel.html')


#BLOCO RESPONSAVEL
@login_required
def insere_novo_responsavel(request):
    if request.method == 'POST':
        id_fun_cad = request.POST.get('id_usuario_cad')
        nome = request.POST.get('pnome')
        sobrenome = request.POST.get('snome')
        cpf = request.POST.get('cpf')
        dt_nasc = request.POST.get('dt_nasc')
        resp_trabalha = request.POST.get('resp_trabalha')
        flag_conjuge = request.POST.get('flag_conjuge')
        conjuge_trabalha = request.POST.get('conjuge_trabalha')
        endereco = request.POST.get('endereco')
        comp = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        obs = request.POST.get('obs')
        sql1 = "INSERT INTO tb_cadastro_responsavel (id_usuario_cad, pnome, snome, cpf, data_nascimento, flag_responsavel_trabalha, flag_conjuge, flag_conjuge_trabalha, endereco, complemento, bairro, cidade, estado,observacoes)"
        sql2 = f"VALUES({ escapar(id_fun_cad) }, {escapar(nome)}, {escapar(sobrenome)}, {escapar(cpf)}, {escapar(dt_nasc)}, {escapar(resp_trabalha)}, {escapar(flag_conjuge)}, {escapar(conjuge_trabalha)}, {escapar(endereco)}, {escapar(comp)}, {escapar(bairro)}, {escapar(cidade)}, {escapar(estado)}, {escapar(obs)})"
        result = Conn.executa_insert(sql1+sql2)    
        if result :
            
            return redirect('lista_responsavel')

        return redirect('lista_responsavel')


@login_required
def lista_responsavel(request):
    responsavel = TbCadastroResponsavel.objects.filter(flag_ativo = 'S', flag_validado = 'S') 
    contexto = {
        'dados': responsavel,
        'titulo': 'Responsável Validados'
    }
    return render(request, 'gerencias/lista_responsavel.html', contexto)


@login_required
def lista_responsavel_nval(request):
    responsavel = TbCadastroResponsavel.objects.filter(flag_ativo = 'S', flag_validado = 'N') 
    contexto = {
        'dados': responsavel,
        'titulo': 'Responsável não Validados'
    }
    return render(request, 'gerencias/lista_responsavel_nval.html', contexto)


@login_required
def lista_responsavel_des(request):
    responsavel = TbCadastroResponsavel.objects.filter(flag_ativo = 'N') 
    contexto = {
        'dados': responsavel,
        'titulo': 'Responsável não Validados'
    }
    return render(request, 'gerencias/lista_responsavel_nval.html', contexto)


@login_required
def edit_responsavel(request, id_responsavel):
    responsavel = TbCadastroResponsavel.objects.all().filter(pk=id_responsavel)  
    contexto = {
        'dados': responsavel,
        'titulo': 'Responsável'
    }
    return render(request, 'gerencias/editar_responsavel.html', contexto)


@login_required
def atualiza_responsavel(request):
    responsavel = get_object_or_404(TbCadastroResponsavel, pk=request.POST.get('id_responsavel'))
    responsavel.pnome = request.POST.get('pnome')
    responsavel.snome = request.POST.get('snome')
    responsavel.cpf = request.POST.get('cpf')
    responsavel.data_nascimento = request.POST.get('dt_nasc')
    responsavel.flag_responsavel_trabalha = request.POST.get('resp_trabalha')
    responsavel.flag_conjuge = request.POST.get('flag_conjuge')
    responsavel.flag_conjuge_trabalha = request.POST.get('conjuge_trabalha')
    responsavel.endereco = request.POST.get('endereco')
    responsavel.complemento = request.POST.get('complemento')
    responsavel.bairro = request.POST.get('bairro')
    responsavel.cidade = request.POST.get('cidade')
    responsavel.estado = request.POST.get('estado')
    responsavel.flag_validado = request.POST.get('validado')
    responsavel.flag_ativo = request.POST.get('ativo')
    responsavel.save()
    return redirect('lista_responsavel')


@login_required
def desativa_responsavel(request, id_responsavel):
    responsavel = get_object_or_404(TbCadastroResponsavel, pk=id_responsavel)
    responsavel.flag_ativo = 'N'  
    responsavel.save()
    registros = TbCadastroResponsavel.objects.filter(flag_ativo='N').order_by('-ultima_atualizacao')
    contexto = {
        'dados': registros,
        'titulo': 'Responsáveis Inativos'
    }
    return render(request, 'gerencias/lista_responsavel.html', contexto)

@login_required
def reativa_responsavel(request, id_responsavel):
    responsavel = get_object_or_404(TbCadastroResponsavel, pk=id_responsavel)
    responsavel.flag_ativo = 'S'  
    responsavel.save()
    registros = TbCadastroResponsavel.objects.filter(flag_ativo='S').order_by('-ultima_atualizacao')
    contexto = {
        'dados': registros,
        'titulo': 'Responsáveis Inativos'
    }
    return render(request, 'gerencias/lista_responsavel.html', contexto)

#Bloco Filhos
@login_required
def lista_filhos(request, id_responsavel):    
    registros = TbFilhosResponsavel.objects.filter(id_responsavel=id_responsavel)
    contexto = {
        'lista': registros,
        'id_responsavel': id_responsavel, 
        'titulo': 'Criancas Cadastrados'
    }
    return render(request, 'gerencias/lista_filhos.html', contexto)


@login_required
def lista_filhos_total(request):    
    lista = Conn.executa_query(
        f"SELECT * FROM tb_filhos_responsavel WHERE  flag_ativo = 'S' ORDER BY id_responsavel")  
    
    return render(request, 'gerencias/lista_filhos_total.html', {'lista': lista})


@login_required
def desativa_filhos_responsavel(request,id_responsavel):
    lista = get_object_or_404(TbCadastroResponsavel, pk=id_responsavel)
    for filho in lista:
        filho.flag_ativo = 'N'  
        filho.save()


@login_required
def reativa_filhos_responsavel(request,id_responsavel):
    lista = get_object_or_404(TbCadastroResponsavel, pk=id_responsavel)
    for filho in lista:
        filho.flag_ativo = 'S'  
        filho.save()


@login_required
def desativar_filho(request,id_filho,id_responsavel):
    registro = TbFilhosResponsavel.objects.filter(id_filho=id_filho).first()
    registro.objects.update(flag_ativo = 'N')
    registro.save()
    return redirect('lista_filhos',id_responsavel)


@login_required
def reativar_filho(request,id_filho):
    registro = TbFilhosResponsavel.objects.filter(id_filho=id_filho).first()
    registro.objects.update(flag_ativo = 'S')
    registro.save()
    return redirect('lista_filhos',registro.id_responsavel)


@login_required
def lista_filhos_responsavel(request):
    registros = TbFilhosResponsavel.objects.filter(id_responsavel=request.POST.get('id_responsavel'),flag_ativo='S').order_by('-data_cadastro')
    contexto = {
        'dados': registros,
        'titulo': 'Responsáveis Ativos'
    }
    return render(request, 'gerencias/lista_responsavel.html', contexto)


@login_required
def novo_filho(request,id_responsavel):
    registro = TbFilhosResponsavel.objects.filter(id_responsavel=id_responsavel).first()
    contexto = {
        'dados': registro,
        'id_responsavel': id_responsavel,  # Isso é suficiente
        'titulo': 'Criancas Cadastrados'
    }
    return render(request, 'gerencias/novo_filho.html', contexto)


@login_required
def insere_novo_filho(request):

    if request.method == 'POST':
        id_responsavel = request.POST.get('responsavel')
        id_usuario_cad = request.user.id
        pnome = request.POST.get('pnome')
        snome = request.POST.get('snome')
        dt_nasc = request.POST.get('dt_nasc')
        cpf = request.POST.get('cpf')
        sexo = request.POST.get('sexo')
        roupa = request.POST.get('roupa')
        sapato = request.POST.get('sapato')
        outra_ong = request.POST.get('outra_ong')

        sql1 = "INSERT INTO tb_filhos_responsavel (id_responsavel, id_usuario_cad, pnome, snome, data_nascimento, cpf, sexo, numero_roupa, numero_sapato, cadastro_outra_ong)"
        sql2 = f"VALUES({ escapar(id_responsavel) }, {escapar(id_usuario_cad)}, {escapar(pnome)}, {escapar(snome)}, {escapar(dt_nasc)}, {escapar(cpf)}, {escapar(sexo)}, {escapar(roupa)}, {escapar(sapato)}, {escapar(outra_ong)})"
        
        result = Conn.executa_insert(sql1+sql2)    
        if result :
            return redirect('lista_filhos', id_responsavel) 
    
    return render(request, 'gerencias/novo_filho.html', {'id_responsavel': id_responsavel})

@login_required
def buscar_filhos(request):
    resultados = []
    termo_busca = ''
    tipo_busca = 'nome'
    
    if request.method == 'POST':
        termo_busca = request.POST.get('termo_busca', '').strip()
        tipo_busca = request.POST.get('tipo_busca', 'nome')
        
        if termo_busca:
            if tipo_busca == 'nome':
                # Busca por nome completo
                resultados = Conn.executa_query(
                    f"SELECT * FROM tb_filhos_responsavel WHERE flag_ativo = 'S' AND CONCAT(pnome, ' ', snome) LIKE '%{ termo_busca }%'"
                )
                contexto = {
                    'resultados': resultados,
                    'termo_busca': termo_busca,
                    'tipo_busca': tipo_busca,
                    'total_resultados': len(resultados),
                }
                return render(request, 'gerencias/buscar_filhos.html', contexto)
            elif tipo_busca == 'idade':
                try:
                    idade_busca = int(termo_busca)
                    todos_filhos = TbFilhosResponsavel.objects.select_related('id_responsavel')
                    
                    for filho in todos_filhos:
                        idade = calcular_idade(filho.data_nascimento)
                        if idade == idade_busca:
                            resultados.append(filho)
                            
                except ValueError:
                    resultados = []
                    termo_busca = 'Por favor, digite um número válido para idade'
    
    # Adiciona a idade calculada a cada resultado
    for filho in resultados:
        filho.idade = calcular_idade(filho.data_nascimento)
    
    contexto = {
        'resultados': resultados,
        'termo_busca': termo_busca,
        'tipo_busca': tipo_busca,
        'total_resultados': len(resultados),
    }
    
    return render(request, 'gerencias/buscar_filhos.html', contexto)

@login_required
def calcular_idade(data_nascimento_str):
    if not data_nascimento_str:
        return None
    try:    
        data_nasc = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()   
        hoje = date.today()
        idade = hoje.year - data_nasc.year   
        if hoje.month < data_nasc.month or (hoje.month == data_nasc.month and hoje.day < data_nasc.day):
            idade -= 1       
        return idade
    except:
        return None
