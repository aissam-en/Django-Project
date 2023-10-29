from django.shortcuts import render,redirect
from .models import Tickets

# Create your views here.

# def ticket_detail(request, id):
#     ticket = Tickets.objects.filter(client_id = id)
#     return render(request, 'tickets_app/tickets_index.html', {'ticket':ticket})

from django.shortcuts import get_object_or_404
from .models import Tickets
from users_app.models import Client
from events_app.models import Events

def ticket_detail(request, id):
    clnt = Client.objects.get(id=id) 
    tickets = Tickets.objects.filter(client=clnt)
    return render(request, 'tickets_app/tickets_index.html', {'tickets': tickets})


import datetime

def ticket_acheter(request, id_match, id_clnt):
    match = Events.objects.get(id = id_match)
    clnt = Client.objects.get(id = id_clnt)

    if request.method == 'POST':
        print("after == POST ticket_acheter()")
        mtch = match        
        tckt_type = request.POST.get('ticket_type')
        nbr = request.POST.get('quantity')
        date = datetime.datetime.now().strftime("%Y-%m-%d")

        tckt = Tickets(client=clnt ,match=mtch, date=date, ticket_type=tckt_type, nbr=nbr)
        tckt.save()
        print("after tckt.save()")
        return redirect('ticket_detail',id_clnt)

    return render(request, 'tickets_app/tickets_acheter.html', {'match':match})




# for stripe
# Stripe product IDs
# Regulier Ticket : prod_O7tS5rZSBCb0iA
# VIP Ticket : prod_O7tTVrK1aE4ZGZ
# 
# link docs: https://stripe.com/docs/payments/accept-a-payment?ui=checkout
# 

# for stripe
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request, id_match, id_clnt):

    nbr = request.POST.get('quantity')

    tckt_type = request.POST.get('ticket_type')
    unit_amount = 12000    #120 DH
    if tckt_type == 'VIP' : unit_amount = 20000    #200 DH

    name = tckt_type+' Ticket : '+str(nbr)

    session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'mad',
        'product_data': {
        'name': name,
        },
        'unit_amount': unit_amount,
      },
      'quantity': nbr,
    }],
    mode='payment',
    success_url='http://127.0.0.1:8000/ticket/success',
    cancel_url='http://127.0.0.1:8000/ticket/cancel',
    )

    if(session):
        match = Events.objects.get(id = id_match)
        clnt = Client.objects.get(id = id_clnt)
        tckt_type = request.POST.get('ticket_type')
        nbr = request.POST.get('quantity')
        date = datetime.datetime.now().strftime("%Y-%m-%d")

        tckt = Tickets(client=clnt ,match=match, date=date, ticket_type=tckt_type, nbr=nbr)
        tckt.save()
        print("after tckt.save()")
        
    return redirect(session.url)



# for stripe
from django.views.generic.base import TemplateView
class SuccessView(TemplateView):
    template_name = 'success.html'
class CancelView(TemplateView):
    template_name = 'cancel.html'



def telecharger_ticket(request, id_tckt, numero):
    ticket = Tickets.objects.get(id=id_tckt)
    return render(request, 'tickets_app/telecharger_ticket.html', {'ticket': ticket, 'numero':numero})


