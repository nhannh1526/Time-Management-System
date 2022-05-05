from django.urls import path
from django.views.generic import TemplateView

app_name = 'tms'

urlpatterns = [
    path('', TemplateView.as_view(template_name="tms/index.html")),
]
