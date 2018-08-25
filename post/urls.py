from django.conf.urls import include
from django.urls import path
from post.views import *

urlpatterns = [
		path('', anasayfa),
		path('anasayfa', anasayfa),
		path('tum_sorular', tum_sorular, name='tum_sorular'),
		path('cevapsizlar', cevapsizlar),
		path('en_yeniler', en_yeniler),
		path('<int:pk>/', post_detail, name='detail'),
		path('<int:pk>/comment', add_comment_to_post, name='add_comment_to_post'),
		path('comment/<int:pk>/approve', comment_approve, name='comment_approve'),
		path('comment/<int:pk>/remove', comment_remove, name='comment_remove'),
		path('soru_sor', soru_sor),
		path('kayit', kayit),
		path('iletisim', iletisim),
		path('', include('django.contrib.auth.urls')),
]


