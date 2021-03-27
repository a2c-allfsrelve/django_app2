from django import forms
from .models import Friend


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']



# class HelloForm(forms.Form):
#     name = forms.CharField(label='Name')
#     mail = forms.EmailField(label='Email')
#     gender = forms.BooleanField(label='Gender', required=False)
#     age = forms.IntegerField(label='Age'),
#     birthday = forms.DateField(label='Birth'),




# class PullDown(forms.Form):
#     data = [
#         ('one', 'たけし'),
#         ('two', 'よしこ'),
#         ('three', 'まさお'),
#         ('four', 'みき'),
#         ('five', 'ヤバ男'),
#     ]

#     choise = forms.ChoiceField(label='radio', choices=data, widget=forms.Select(attrs={'size': 5}))
         