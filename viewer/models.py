from PIL import Image
from django.db.models import Model, CharField, ForeignKey, DO_NOTHING, IntegerField, DateField, TextField, \
    DateTimeField, ImageField, FloatField
from accounts.models import Profile


class Cars(Model):
    name = CharField(max_length=128)
    car_model = CharField(max_length=128)
    image = ImageField(default="default_car.jpg", upload_to="car_thumbnails")
    engine = FloatField()
    year_of_production = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car_model}; {self.year_of_production}"


class Rental(Model):
    profile_id = ForeignKey(Profile, on_delete=DO_NOTHING)
    car_id = ForeignKey(Cars, on_delete=DO_NOTHING)