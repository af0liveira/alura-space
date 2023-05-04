from django import forms

class LoginForm(forms.Form):
    login_name = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joao_silva',
            }
        )
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            },
        ),
    )

class SignupForm(forms.Form):
    login_name = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joao_silva',
            }
        )
    )
    email = forms.CharField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: jsilva@xpto.com',
            }
        )
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Escolha sua senha',
            },
        ),
    )
    password_confirmation = forms.CharField(
        label='Confirmação da Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha',
            },
        ),
    )

    def clean_login_name(self):
        login_name = self.cleaned_data.get('login_name')

        if login_name:
            login_name = login_name.strip()
            if ' ' in login_name:
                raise forms.ValidationError("O nome de login não pode conter espaços!")
            else:
                return login_name

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password and password_confirmation:
            if password != password_confirmation:
                raise forms.ValidationError("Senhas diferem!")
            else:
                return password_confirmation
            

