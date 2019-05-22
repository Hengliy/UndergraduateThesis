from django.conf.urls import url
from department import views
# 127.0.0.1:8000/app01/index.html
urlpatterns = [
    url('getDepartmentList',views.getDepartmentList)
]