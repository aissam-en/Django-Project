from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.ticket_detail, name='ticket_detail'),

    path('acheter/<int:id_match>&<int:id_clnt>', views.ticket_acheter, name='ticket_acheter'),

    path('create_checkout_session/<int:id_match>&<int:id_clnt>', views.create_checkout_session, name='create_checkout_session'),# for stripe
    path('success/', views.SuccessView.as_view()),# for stripe
    path('cancel/', views.CancelView.as_view()),# for stripe

    path('telecharger_ticket/<int:id_tckt>&<int:numero>', views.telecharger_ticket, name='telecharger_ticket'),

]