from collections import UserList
from django import forms


from .models import Music, UserProfile

class MusicUploadForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['song_name', 'album', 'language', 'song_image', 'year', 'singer', 'song_file']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['stage_name', 'genre', 'bio', 'display_name', 'country',
                  'notify_emails', 'notify_in_app', 'public_profile',
                  'show_activity', 'audio_quality']    