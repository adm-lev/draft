from django.urls import include, path, re_path
from . import views




urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^book/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='books-detail'),
]


urlpatterns += [
    re_path('accounts/', include('django.contrib.auth.urls')),
]

