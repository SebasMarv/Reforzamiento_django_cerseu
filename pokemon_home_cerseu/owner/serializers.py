from rest_framework import serializers

from owner.models import Owner


class OwnerSsr(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('nombre', 'pais', 'edad', 'identificacion', 'descripcion')
