from django.contrib import admin
from .models import Question, Answer

# admin에 데이터 검색 기능 추가
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']         # admin에서 제목으로 질문을 검색할 수 있도록 검색항목을 추가함


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Answer, AnswerAdmin)
