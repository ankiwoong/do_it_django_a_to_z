from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)  # 제목
    content = models.TextField()  # 내용

    creted_at = models.DateTimeField(auto_now_add=True)  # 작성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일
    # author : 추후 작성 예정       # 작성자 정보

    def __str__(self):
        return f"[{self.pk}]{self.title}"  # [해당 포스트의 pk값]해당 포스트의 title 값