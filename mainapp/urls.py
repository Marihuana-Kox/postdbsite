from django.urls import path

from .views import MainPage, SitePageDetail, ListArticleView


urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('<slug:slug>/', SitePageDetail.as_view(), name='site_page_detail'),
    path('list/allarticls/', ListArticleView.as_view(), name='list_article'),
]