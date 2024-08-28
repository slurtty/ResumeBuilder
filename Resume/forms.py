from django import forms

from Resume.models import Profile, Education, Experience, Skill, Language


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'site']
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': ''})
        # }


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ['institution_name', 'description', 'start_date', 'end_date', 'still_studying']


    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date'})


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = [
            'job_title', 'company_name', 'description', 'start_date', 'end_date', 'still_work'
        ]


    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['end_date'].widget = forms.DateInput(attrs={'type': 'date'})


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = [
            'name', 'rate'
        ]


class LanguageForm(forms.ModelForm):

    class Meta:
        model = Language
        fields = [
            'name', 'level'
        ]
