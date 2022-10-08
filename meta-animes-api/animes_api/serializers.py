from rest_framework import serializers
from .models import *

class ChaptersSerializer(serializers.ModelSerializer):

    class Meta:

        model = Chapters
        fields = ('title', 'language', 'url_video', 'url_ref')
    
    def create(self, validated_data):
        validated_data['anime'] = Animes.objects.filter(name=validated_data['anime']).get()
       # print(anime)
        Chapters.objects.create(**validated_data)
    
    def validate(self, validated_data):
        # if not validated_data['title']:
        #     raise serializers.ValidationError({'TITLE': 'NOT BLANK'})
        return validated_data


class AnimeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Animes
        fields = '__all__'
    
    def create(self, validated_data):
        Animes.objects.create(**validated_data)
    
    def validate(self, validated_data):
        # if not validated_data['title']:
        #     raise serializers.ValidationError({'TITLE': 'NOT BLANK'})
        return validated_data



	# { 
    # "anime": "BOKU NO HERO",
	# 	"title": "Assistir Boku no Hero Academia Episodio 1 Online",
	# 	"language": "  Dublado ",
	# 	"url_video": "https://www.blogger.com/video.g?token=AD6v5dzR18VMmb44ARDW7zTkPetmZxGNt1MI6nvfUuRz7eXirFepIQVC1pNkGFTr825JG0f2Ef06WlDG9fNbOXmsNklICLF9d_7NUc3D6bfnsYe2D1EQKGEw2DtqbJHdfa11Gs0y4Uk2",
	# 	"url_ref": "https://animesbr.biz/episodio/boku-no-hero-academia-episodio-1/"
	# }