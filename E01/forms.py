from django import forms
from .models import MeetingRoom

class MeetingRoomModelForm(forms.ModelForm):
    picture_file = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control mb-3'}), label='사진')

    class Meta:
        model = MeetingRoom
        fields = ['name', 'address', 'picture_file', 'space', 'capacity', 'audio', 'video', 'other', 'information']

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'address' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'space' : forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'capacity' : forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'audio' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'video' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'other' : forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'information' : forms.Textarea(attrs={'class': 'form-control mb-3'}),
        }

        labels = {
            'name' : '명칭', 'address' : '주소', 'space' : '면적(㎡)', 'capacity' : '수용인원(명)', 'audio' : '음향시설', 'video' : '영상시설', 'other' : '기타시설', 'information' : '상세설명'
        }