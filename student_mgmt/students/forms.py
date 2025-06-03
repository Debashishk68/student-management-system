from django import forms
from .models import Student, Course, Section

class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Date of Birth"
    )

    section = forms.CharField(
        label='Section Name',
        widget=forms.TextInput(attrs={'placeholder': 'e.g., 10A'}),
        required=True
    )

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth',
                  'phone_number', 'course', 'section', 'student_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Doe'}),
            'email': forms.EmailInput(attrs={'placeholder': 'john@example.com'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+91XXXXXXXXXX'}),
        }

    def clean_section(self):
        section_name = self.cleaned_data['section']
        course = self.cleaned_data.get('course')

        if not course:
            raise forms.ValidationError("Please select a course before entering a section.")

        # Try to find existing section or create new one
        section_obj, _ = Section.objects.get_or_create(name=section_name, course=course)
        return section_obj
    
