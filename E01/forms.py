from django.forms import ModelForm
from django import forms
from .models import MeetingRoom, Equipment

class MeetingRoomModelForm(forms.ModelForm):
    class Meta:
        model = MeetingRoom
        fields = ['name', 'address', 'picture', 'keyword']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'address' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'picture' : forms.URLInput(attrs={'class': 'form-control mb-3'}),
            'keyword' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
        }

class EquipmentModelForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['meetingroom_id', 'space', 'capacity', 'equip_audio', 'equip_video', 'equip_other', 'layout', 'information']

        widgets = {
            'meetingroom_id' : forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'space' : forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'capacity' : forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'equip_audio' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'equip_video' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'equip_other' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'layout' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'information' : forms.Textarea(attrs={'class': 'form-control mb-3'}),
        }