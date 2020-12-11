from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model=Song
		fields='__all__'
	def to_representation(self, instance):
		rep = super(SongSerializer, self).to_representation(instance)
		rep['artist'] = instance.artist.first_name
		return rep 