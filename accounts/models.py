from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, CharField, TextField, ImageField
from PIL import Image


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    name = CharField(max_length=126, blank=False)
    image = ImageField(default="default.jpg", upload_to="profile_pics")
    gender = CharField(max_length=6, blank=True)
    biography = TextField(blank=True)

    def __str__(self):
        return f"{self.name} Profile"
