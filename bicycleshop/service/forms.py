from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    invoice_id = forms.IntegerField(widget=forms.HiddenInput())
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Service
        fields = ['id', 'specialist', 'service_startdate', 'service_enddate', 'status', 'service_cost', 'comment']

    def save(self, commit=True):
        service = super().save(commit=False)
        sale_id = self.cleaned_data.get('invoice_id')
        service.sale_id = sale_id
        if commit:
            service.save()
        return service