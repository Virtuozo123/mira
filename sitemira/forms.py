from django import forms
from .models import create, Comment
from django.utils.translation import ugettext_lazy as _ 


class create_project(forms.ModelForm):
    
    class Meta:
        model = create
        fields =(
            'name_project',
            'first_name',
            'second_name',
            'third_name',
            'organizathion_name',
            'chosen_category',
            'chosen_category_2',
            'low_description',
            'description',
            'coordinates',
            'phone',
            'email',
            'logo_pic'
        )
        
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)        