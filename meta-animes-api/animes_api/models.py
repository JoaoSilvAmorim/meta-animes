from django.db import models
import uuid


class Animes(models.Model):

    class Meta:
        db_table = 'animes'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
   
class Chapters(models.Model):

    class Meta:
        db_table = 'chapters'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64)
    language = models.CharField(max_length=24)
    url_video = models.URLField(max_length = 200)
    url_ref = models.URLField(max_length = 200)
    anime = models.ForeignKey(Animes, on_delete=models.CASCADE)

