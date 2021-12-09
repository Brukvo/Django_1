from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from .models import CommonUser

class ShopUserLoginForm(AuthenticationForm):
    
    class Meta:
        model = CommonUser
        fields = ('username', 'password')
        
    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            

class ShopUserRegisterForm(UserCreationForm):
    class Meta:
	model = CommonUser
	fields = ('username', 'age', 'avatar', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
	super().__init__(*args, **kwargs)
	for field_name, field in self.fields.items():
	    field.widget.attrs['class'] = 'form-control'
	    field.help_text = ''
	

class ShopUserEditForm(UserChangeForm):
    class Meta:
	model = ShopUser
	fields = ('username', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
	super().__init__(*args, **kwargs)
	for field_name, field in self.fields.items():
	    field.widget.attrs['class'] = 'form-control'
	    field.help_text = ''
	    if field_name == 'password':
		field.widget = forms.HiddenInput()
