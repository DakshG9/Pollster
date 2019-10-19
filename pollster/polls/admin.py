from django.contrib import admin

from .models import Question, Choice, Contact

admin.site.site_header = "Pollster Poll Createor"
admin.site.site_title = "Welcome to the Pollster Poll Creator."
admin.site.index_title = "Pollster Poll Creator"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Contact)