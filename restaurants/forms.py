from django import forms


class VoteForm(forms.Form):
    restaurant_id = forms.IntegerField()
