from django import forms
from .models import *



# Staff profile form
class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            'f_name', 'l_name', 'gender', 'phone_no', 'blood_group', 'DoB', 
            'father_name', 'father_phone', 'address', 'city', 'state',
            'pin_code', 'married_status', 'qualification','subject','experience',
            'email', 'image','position',
        ]
        widgets = {
            'f_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first Name'}),
            'l_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last Name'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone','type': 'tel', 'pattern': '[0-9]{10}'}),
            'blood_group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blood group'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter father name'}),
            'father_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter father phone','type': 'tel', 'pattern': '[0-9]{10}'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter teching subject'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'}),
            'pin_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter pin code'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Qualifications'}),
            'experience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Experience'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '@gmail.com'}),
            'DoB': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': 'yyyy-MM-dd'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'married_status': forms.Select(attrs={'class': 'form-select'}),
            'position':forms.Select(attrs={'class': 'form-select'})
        }


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'f_name', 'l_name', 'gender', 'blood_group', 'DoB','standard','section', 
            'father_name', 'father_occupation', 'mother_occupation', 'mother_phone', 'mother_name', 
            'register_no', 'father_phone', 'address', 'city', 'state', 'pin_code', 'image'
        ]
        widgets = {
            'f_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first Name'}),
            'l_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last Name'}),
            'blood_group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blood group'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter father name'}),
            'father_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter father phone','type': 'tel', 'pattern': '[0-9]{10}'}),
            'section': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter section'}),
            'standard': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter standard'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'}),
            'pin_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter pin code'}),
            'DoB': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': 'yyyy-MM-dd'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'register_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Reg.No'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mother name'}),
            'mother_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mother phone', 'type': 'tel', 'pattern': '[0-9]{10}'}),
            'mother_occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mother occupation'}),
            'father_occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter father occupation'}),
        }


class SignUpForm(forms.ModelForm):
    c_password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        label="Confirm Password"
    )

    class Meta:
        model = Sign_Up
        fields = ['user_type', 'username', 'email', 'password']
        widgets = {
            'user_type': forms.Select(attrs={'class': 'form-select'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }



class SignInForm(forms.Form):
    user_type = forms.ChoiceField(
        choices=Sign_Up.USER_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['subject', 'title', 'description', 'due_date', 'students', 'created_by']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Name'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assignment Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Assignment Description', 'rows': 2}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select Due Date'}),
            'students': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Select Students'}),
            'created_by': forms.Select(attrs={'class': 'form-select'}),  # Use Select widget for ForeignKey
        }

