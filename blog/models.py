from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)  # 제목
    content = models.TextField()  # 내용

    creted_at = models.DateTimeField()  # 작성일
    # author : 추후 작성 예정       # 작성자 정보