from django.urls import path

from .views import RequestList, RequestDetail

app_name = 'tms_api'

urlpatterns = [
    path('<int:pk>/', RequestDetail.as_view(), name='detailcreate'),
    path('', RequestList.as_view(), name='listcreate'),
]
