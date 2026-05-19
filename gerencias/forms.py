from .models import TbFuncionario, TbTipoFuncionario
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class AccountSignupForm(forms.ModelForm):
    password = forms.CharField(
        label="Senha",
        max_length=50,
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = User
        fields = ('username','password')


class TbFuncionarioForm(forms.ModelForm):
    class Meta:
        
        model = TbFuncionario
        
        fields = ['id_tipo', 'pnome', 'snome', 'cpf', 'endereco', 'telefone', 'complemento', 'bairro', 'cidade', 'estado', 'flag_ativo']

        widgets = {
            'pnome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'snome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Complemento'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UF', 'maxlength': 2}),
            'id_tipo': forms.Select(attrs={'class': 'form-control'}),
            'flag_ativo': forms.Select(attrs={'class': 'form-control'}, choices=[('', '---------'), ('S', 'Sim'), ('N', 'Não')]),
        }
        
        labels = {
            'id_tipo': 'Tipo de Funcionário',
            'pnome': 'Primeiro Nome',
            'snome': 'Sobrenome',
            'cpf': 'CPF',
            'endereco': 'Endereço',
            'telefone': 'Telefone',
            'complemento': 'Complemento',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado (UF)',
            'flag_ativo': 'Ativo',
        }
        
        help_texts = {
            'cpf': 'Apenas números, 11 dígitos',
            'telefone': 'Informe o telefone com DDD',
            'estado': 'Sigla do estado com 2 letras',
        }