from django import forms
from .models import create, Comment, blog, Comment2
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
        
class CommentForm2(forms.ModelForm):

    class Meta:
        model = Comment2
        fields = ('author', 'text',) 
        
class create_blog(forms.ModelForm):
     
    class Meta:
        model = blog
        fields = ('author','blog_name','blog_text','blog_items')