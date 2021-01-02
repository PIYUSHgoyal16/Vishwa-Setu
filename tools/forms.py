from django import forms

class SandhiForm(forms.Form):
    txt1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the first word','class': 'form-control'}))
    txt2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the second word','class': 'form-control'}))


class DictForm(forms.Form):
    type = forms.ChoiceField(choices=[("sans", "Sanskrit"), ("eng", "English")])
    txt = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input word','class': 'form-control'}))

class SandhiSplitterForm(forms.Form):
    txt = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Input word','class': 'form-control'}))
    type = forms.ChoiceField(choices=[('समासच्छेदः', 'समासच्छेदः'),('पदच्छेदः', 'पदच्छेदः'), ('उभयोरपि', 'उभयोरपि')])
    
