import base64
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers


class MyImageField(serializers.ImageField):
    def to_internal_value(self, data):
        format, imgstr = data.split(';base64,')
        file_name = str(uuid.uuid4())[:12]
        ext = format.split('/')[-1]
        data = ContentFile(
            base64.b64decode(imgstr),
            name=file_name + '.' + ext
        )
        django_field = self._DjangoImageField()
        django_field.error_messages = self.error_messages
        return django_field.clean(data)
