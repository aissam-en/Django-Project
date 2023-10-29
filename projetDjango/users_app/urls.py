from django.urls import path
from . import views

urlpatterns = [

    path('profile/<int:id>', views.profile_view, name='profile'),
    path('modifier_profil/<int:id_user>', views.modifier_profil_view, name='modifier_profil'),

    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('ajouter_match/', views.ajouter_match, name='ajouter_match'),

    path('to_dashboard/', views.to_dashboard, name='to_dashboard'),
    path('to_dashboard_clnts/', views.to_dashboard_clnts, name='to_dashboard_clnts'),
    path('to_dashboard_events/', views.to_dashboard_events, name='to_dashboard_events'),

]
