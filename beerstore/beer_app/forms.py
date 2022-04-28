from django import forms

from beerstore.beer_app.models import Beer, Review


class BeerAddForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = '__all__'


class BeerEditForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = '__all__'


class BeerDeleteForm(forms.ModelForm):
    class Meta:
        model = Beer
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'


class ReviewAddForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('beer', 'review')