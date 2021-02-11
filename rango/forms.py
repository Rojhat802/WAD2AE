from django import forms
from rango.models import Page, category


class categoryform(forms.moodleform):
    name = forms.charfield(max_length=128,
                           help_text="please enter the category name")
    views = forms.integerfield(wideget=forms.hiddeninput(), initial=0)
    likes = forms.integerfield(widget=forms.hiddeninput, initial=0)
    slug = forms.charfield(widget=forms.hiddeninput(), required=False)

    class meta:
        model = category
        fields = ('name',)


class PageForm(forms.Modelform):
    title = forms.charfield(max_length=128,
                            help_text="please enter the title of the page")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
    # If url is not empty and doesn't start with 'http://',
    # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = f'http://{url}'
        cleaned_data['url'] = url
        return cleaned_data

    class Meta:
        model = Page
        exclude = ('category',)
