from django.conf.urls import url
from group import views
# 127.0.0.1:8000/app01/index.html
urlpatterns = [
    # url('getContestListByParentindex',views.getContestListByParentindex),
    url('getAllGroupBrief',views.getAllGroupBrief),
    url('getGroupInfoById',views.getGroupInfoById)
    # url('getAllContestInfo',views.getAllContestInfo)
]