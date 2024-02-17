from django import forms

class ResetPasswordForm(forms.Form):
    def clean_password(self):
        password = self.data.get('password')
        password_confirm = self.data.get('password_confirm')

        if (not password or not password_confirm):
            raise forms.ValidationError('Please fill password and password confirmation fields')

        if (password != password_confirm):
            raise forms.ValidationError('Password mismatch error ')

        return password

    class Meta:
        fields = [
            "password",
            "password_confirm"
        ]
