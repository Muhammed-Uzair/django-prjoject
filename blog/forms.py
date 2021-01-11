from django import forms


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': ' form-control '}),
            'email': forms.TextInput(attrs={'class': ' form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostSearchForm(forms.Form):
    search = forms.CharField()
