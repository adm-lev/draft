from django.urls import include, path, re_path
from . import views




urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^book/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='books-detail'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^test/$', views.test, name='test'),
    re_path(r'^author/$', views.AuthorListView.as_view(), name='authors'),
]


urlpatterns += [
    re_path('accounts/', include('django.contrib.auth.urls')),
]

