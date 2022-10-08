from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from .serializers import *
from .models import *

class chapters(APIView):
  def get_chapter(id):
    try:
      return Chapters.objects.filter(id=id).get()
    except:
      return Response(status=status.HTTP_400_BAD_REQUEST) 

  def get(self, request, id=None):
    if id == None:
      chapters = Chapters.objects.all()
      serializer = ChaptersSerializer(chapters, many=True)
      return Response(serializer.data)
    else:
      chapters = self.get_Chapters(id)
      serializer = ChaptersSerializer(chapters)
      return Response(serializer.data)
      
  def post(self, request):
    serializer = ChaptersSerializer(data=request.data)
    if serializer.is_valid():
      serializer.create(request.data)
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'msg' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class animes(APIView):
  def get_chapter(id):
    try:
      return Animes.objects.filter(id=id).get()
    except:
      return Response(status=status.HTTP_400_BAD_REQUEST) 

  def get(self, request, id=None):
    if id == None:
      chapters = Animes.objects.all()
      serializer = AnimeSerializer(chapters, many=True)
      return Response(serializer.data)
    else:
      chapters = self.get_Chapters(id)
      serializer = AnimeSerializer(chapters)
      return Response(serializer.data)
      
  def post(self, request):
    serializer = AnimeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.create(request.data)
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'msg' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
# {
# "chapters": [
# 	{ 
#     "anime": "BOKU NO HERO",
# 		"title": "Assistir Boku no Hero Academia Episodio 1 Online",
# 		"language": "  Dublado ",
# 		"url_video": "https://www.blogger.com/video.g?token=AD6v5dzR18VMmb44ARDW7zTkPetmZxGNt1MI6nvfUuRz7eXirFepIQVC1pNkGFTr825JG0f2Ef06WlDG9fNbOXmsNklICLF9d_7NUc3D6bfnsYe2D1EQKGEw2DtqbJHdfa11Gs0y4Uk2",
# 		"url_ref": "https://animesbr.biz/episodio/boku-no-hero-academia-episodio-1/"
# 	},
# 	{
# 		"title": "Assistir Boku no Hero Academia Episodio 1 Online",
# 		"language": "  Legendado ",
# 		"url_video": "https://www.blogger.com/video.g?token=AD6v5dw4GF-zOXz1BlGv0OBRjeSotiHjZXUPX2Np8-KSyP26lnPIScuqJ5UNsjRsT8qUB96Q_nLWIR7D1qmy18S2dJBpJstTV-4jWkmLdn065zyHfSsUFLEXmI21yAqoCmZS41gzGlRa",
# 		"url_ref": "https://animesbr.biz/episodio/boku-no-hero-academia-episodio-1/"
# 	}
# ]
# }