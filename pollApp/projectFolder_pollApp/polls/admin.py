from django.contrib import admin

# importing Question and Choice models in /admin
from .models import Choice, Question

# STRUCTURE #1
# best practice is to use fieldsets
# easier to arrange them especially if there will be dozen of fields

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Date information', {'fields': ['pub_date']}),
#         ('Question Information', {'fields': ['question_text']}),
#     ]

# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)

# STRUCTURE #2
# setting up the Choice model in the Question model
# design choices ex. StackedInline, TabularInline and etc.
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['pub_date']}),
        ('Question Information', {'fields': ['question_text']}),
    ]
    # display individual column fields in the list
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # display filtering feature
    list_filter = ['pub_date']
    # adds a search box at the top of the change list
    search_fields = ['question_text']
    # placing the Choice model inline with Question model
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)