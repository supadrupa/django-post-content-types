from django import forms


class MultipartForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        min_length=3,
        error_messages={
            "required": "Username is required",
            "min_length": "Username must be at least 3 characters long",
            "max_length": "Username cannot exceed 150 characters",
        },
    )
    email = forms.EmailField(
        required=True,
        error_messages={
            "required": "Email is required",
            "invalid": "Please enter a valid email address",
        },
    )
    avatar = forms.FileField(
        required=False, error_messages={"invalid": "Please upload a valid file"}
    )

    def clean_avatar(self):
        avatar = self.cleaned_data.get("avatar")
        if avatar:
            if avatar.size > 5 * 1024 * 1024:
                raise forms.ValidationError("File size cannot exceed 5MB")

            allowed_types = ["image/jpeg", "image/png", "image/gif", "image/webp"]
            if avatar.content_type not in allowed_types:
                raise forms.ValidationError(
                    f'Invalid file type. Allowed types: {", ".join(allowed_types)}'
                )
        return avatar

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username:
            if not username.replace("_", "").isalnum():
                raise forms.ValidationError(
                    "Username can only contain letters, numbers, and underscores"
                )
        return username


class URLEncodedForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        min_length=3,
        error_messages={
            "required": "Username is required",
            "min_length": "Username must be at least 3 characters long",
            "max_length": "Username cannot exceed 150 characters",
        },
    )
    email = forms.EmailField(
        required=True,
        error_messages={
            "required": "Email is required",
            "invalid": "Please enter a valid email address",
        },
    )
    password = forms.CharField(
        required=True,
        min_length=8,
        error_messages={
            "required": "Password is required",
            "min_length": "Password must be at least 8 characters long",
        },
    )
    bio = forms.CharField(
        required=False,
        max_length=500,
        widget=forms.Textarea,
        error_messages={"max_length": "Bio cannot exceed 500 characters"},
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username:
            if not username.replace("_", "").isalnum():
                raise forms.ValidationError(
                    "Username can only contain letters, numbers, and underscores"
                )
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password:
            if password.isdigit():
                raise forms.ValidationError("Password cannot be entirely numeric")
            if password.lower() == password or password.upper() == password:
                raise forms.ValidationError(
                    "Password must contain both uppercase and lowercase letters"
                )
        return password
