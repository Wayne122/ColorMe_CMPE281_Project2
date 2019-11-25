from django.db import models
from django.contrib.auth.models import User
import uuid
import os
from django.core.exceptions import ValidationError


# Create your models here.
def update_filename(instance, filename):
    old_filename, extension = os.path.splitext(filename)
    new_filename = old_filename + "_" + str(instance.id) + extension
    return new_filename


def validate_file_size(value):
    filesize = value.size
    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value


def validate_file_ext(value):
    if os.path.splitext(os.path.basename(value.name))[1] != '.png' and os.path.splitext(os.path.basename(value.name))[1] != '.jpg':
        raise ValidationError("Please upload png, jpg files only.")
    else:
        return value


class picLabel(models.Model):
    name = models.CharField(max_length=128)


class s3objects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to=update_filename, validators=[validate_file_size, validate_file_ext])
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    new_url = models.URLField()
    labels = models.ManyToManyField(picLabel)
    uploadTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return os.path.basename(self.file.name)