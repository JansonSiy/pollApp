from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# app_name = 'polls'
# urlpatterns = [
#     # example: /polls/
#     path('', views.index, name='index'),
#     # example: /polls/1/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # example: /polls/1/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # example: /polls/1/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

# NOTES THAT SHOULD BE IN polls/templates/polls/index.html
# notes: hardcoded
# <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
# notes: using polls.urls.py
# <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
# notes: using app_name in urls.py
# <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>