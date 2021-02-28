from django import forms

class PullDown(forms.Form):
    data = [
        ('one', 'たけし'),
        ('two', 'よしこ'),
        ('three', 'まさお'),
        ('four', 'みき'),
        ('five', 'ヤバ男'),
    ]

    choise = forms.ChoiceField(label='radio', choices=data, widget=forms.Select(attrs={'size': 5}))
         