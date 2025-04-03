from django import forms


class UploadFileForm(forms.Form):
    xml_file = forms.FileField()
