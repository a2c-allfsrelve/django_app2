from django import forms
from .models import Friend


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)

class CheckForm(forms.Form):
    # empty = forms.CharField(label='empty', empty_value=True)
    # min = forms.CharField(label='min', min_length=10)
    # max = forms.CharField(label='max', max_length=10)
    # required = forms.IntegerField(label='required')
    # minnum = forms.IntegerField(label='MinNum', min_value=10)
    # maxnum = forms.IntegerField(label='MaxNum', max_value=10)

    # date = forms.DateField(label='Date', input_formats=['%d'])
    # time = forms.TimeField(label='Time')
    # datetime = forms.DateTimeField(label='DateTime')

    str = forms.CharField(label='String')

    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if(str.lower().startswith('no')):
            raise forms.ValidationError('You input No!!!')





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
         