from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'translation', 'image']
        
    def clean_word(self):
        word = self.cleaned_data['word']
        if len(word) < 2:
            raise forms.ValidationError('Слово слишком короткое! Минимум 2 буквы.')
        return word
