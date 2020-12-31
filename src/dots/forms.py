from typing import Tuple

from django import forms


def create_choices(start: int, stop: int, step: int = 1) -> Tuple:
    return tuple((i, i) for i in range(start, stop, step))


class DotCreateForm(forms.Form):
    x = forms.IntegerField(widget=forms.Select(choices=create_choices(-3, 6)), initial=0)
    y = forms.FloatField(min_value=-5, max_value=5, widget=forms.NumberInput(attrs={'placeholder': '[-5; 5]'}))
    r = forms.IntegerField(widget=forms.RadioSelect(choices=create_choices(1, 6)))
