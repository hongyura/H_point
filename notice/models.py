from django.conf import settings
from django.db import models

class Notice(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)#게시글 조회수
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')#게시글 작성일
    top_fixed = models.BooleanField(verbose_name='상단고정', default=False)#중요 게시글 상단고정 여부

    def __str__(self):
        return self.title



    class Meta:
        db_table = '공지사항'
        verbose_name = '공지사항'
        verbose_name_plural = '공지사항'
