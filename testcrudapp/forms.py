from django.forms import ModelForm
from .models import Ordering


class OrderingForm(ModelForm):
    class Meta:
        model = Ordering
        fields = '__all__'