from django.urls import path
from Dashboards import views

urlpatterns =[
    path('prediction/',views.prediction_view,name='prediction_view'),
    path('livescore/',views.livescore, name='livescore'),
    path('Analysis/',views.analysis, name='analysis'),
]