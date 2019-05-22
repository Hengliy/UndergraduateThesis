from django.conf.urls import url
from contest import views
# 127.0.0.1:8000/app01/index.html
urlpatterns = [
    url('getContestListByParentindex',views.getContestListByParentindex),
    url('getAllContestTpye',views.getAllContestType),
    url('getAllContestInfo',views.getAllContestInfo)
]