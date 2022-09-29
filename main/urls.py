from django.urls import path
from.import views
from.views import articledetailview,editview
urlpatterns = [
    path('', views.index, name='index'),
    path('addpost/', views.addpost, name='addpost'),
   # path('postowner', views.postowner, name='postowner'),
    path('register/', views.register, name='register'),
    #path('login/', views.login, name='login'),, djangon dosent need if for loginng page he handles it himself
    path('updateuser', views.updateuser, name='updateuser'),
    path('author', views.author, name='author'),
    #path('article<int:id>', views.article, name='article'),
    path('article<int:pk>', articledetailview.as_view(), name='article'),
    path('article/editpost<int:pk>', editview.as_view(), name='editpost')
    

]
