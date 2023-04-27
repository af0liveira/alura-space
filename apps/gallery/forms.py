from django import forms

from apps.gallery.models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = [
            'public',
        ]

        labels = {
            'title': 'Título',
            'caption': 'Legenda',
            'category': 'Categoria',
            'description': 'Descrição',
            'photo': 'Fotografia',
            'date_added': 'Data de Cadastramento',
            'user': 'Usuário',
        }

        widgets = dict(
            title=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Título da foto',
                },
            ),
            caption=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Insira uma legenda para a imagem.',
                },
            ),
            category=forms.Select(
                attrs={
                    'class': 'form-control',
                },
            ),
            description=forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Mais informações sobre a imagem.',
                },
            ),
            date_added=forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                },
            ),
            user=forms.Select(
                attrs={
                    'class': 'form-control',
                },
            ),
            photo=forms.FileInput(
                attrs={
                    'class': 'form-control',
                },
            ),
        )
