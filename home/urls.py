from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('maqolalar/', views.maqolalar, name='maqolalar'),
    path('maqola-arxiv/', views.arxiv_view, name='maqola-arxiv'),
    path('konferensiya/', views.konferensiya_view, name='konferensiya'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact, name='contact'),

    path("search/", views.get_queryset, name="search_results"),

    path('register/', views.signup, name='register'),
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout_view, name="logout"),
]
