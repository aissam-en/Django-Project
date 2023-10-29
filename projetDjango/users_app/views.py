from django.shortcuts import render
# Create your views here.


# from : https://github.com/YashMarmat/django-ecommerce-bookstore#signup_view
# from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserCreationForm
# from django.views import generic

# class SignUpView(generic.CreateView):
#     form_class    = UserCreationForm
#     success_url   = reverse_lazy('login')
#     template_name = 'templates/events_app/signup.html'



from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Organisateur, Admininstrateur, Client, Users

from .forms import CustomUserCreationForm

from django.contrib.auth import logout 



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in :
            user = form.get_user()
            login(request, user)
            return redirect('event_index')
        else: return redirect('login')
    else :
        form = AuthenticationForm()
        return render(request, 'users_app/login.html', {'form':form})


def signup_view(request):
    if request.method == 'POST':
        print("after == POST")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("after is_valide")
            user = form.save()
            if form.cleaned_data['user_type'] == "Client":
                print("after === Client")
                clnt = Client.objects.create(
                    email=form.cleaned_data['email'],
                    user_type=form.cleaned_data['user_type'],
                    addresse=form.cleaned_data['addresse'],
                    nom=form.cleaned_data['nom'],
                    prenom=form.cleaned_data['prenom']
                )
                clnt.save()
                print("after clnt.save()")
                client_grp = Group.objects.get(name='client_group')
                client_grp.user_set.add(user)
                print("after addded to client_grp")

            elif form.cleaned_data['user_type'] == "Admin":
                print("after == Admin")
                user.is_staff=True
                print("after is_staff")
                user.save()
                print("after user.save()")
                adm = Admininstrateur.objects.create(
                    email=form.cleaned_data['email'],
                    user_type=form.cleaned_data['user_type'],
                    addresse=form.cleaned_data['addresse'],
                    nom=form.cleaned_data['nom'],
                    prenom=form.cleaned_data['prenom']
                )
                adm.save()
                print("after adm.save()")
                admin_grp = Group.objects.get(name='admin_group')
                admin_grp.user_set.add(user)
                print("after addded to admin_grp")

            elif form.cleaned_data['user_type'] == "Organisateur":
                print("after == Organisateur")
                user.is_staff=True
                print("after is_staff")
                user.save()
                org = Organisateur.objects.create(
                    email=form.cleaned_data['email'],
                    user_type=form.cleaned_data['user_type'],
                    addresse=form.cleaned_data['addresse'],
                    nom=form.cleaned_data['nom'],
                    prenom=form.cleaned_data['prenom'],
                    lieu=form.cleaned_data['lieu'],
                    description=form.cleaned_data['description'],
                    categorie=form.cleaned_data['categorie']
                )
                org.save()
                print("after org.save()")
                org_grp = Group.objects.get(name='organisateur_group')
                org_grp.user_set.add(user)
                print("after addded to org_grp")

            # log in l'utilisateur:
            login(request, user)
            return redirect('event_index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users_app/signup.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('event_index')



def ajouter_match(request):
    if request.method == 'POST':
        print("after == POST ajouter_match()")
        match = request.POST.get('match_event')
        date = request.POST.get('date_event')
        lieu = request.POST.get('lieu_event')
        org_1 = request.POST.get('organisateur_event')
        org = Organisateur.objects.get(categorie=org_1)

        image_file = request.FILES.get('image_event')
        if image_file:
            evnt = Events(match=match, date=date, lieu=lieu, organisateur=org,image=image_file)
        else:
            evnt = Events(match=match, date=date, lieu=lieu, organisateur=org)
        evnt.save()

        print("after evnt.save()")
        return redirect('event_index')
    organisateurs = Organisateur.objects.all()
    return render(request, 'events_app/event_ajouter.html', {'organisateurs':organisateurs})



def to_dashboard (request):  
    return redirect('/admin/')

def to_dashboard_clnts (request):  
    return redirect('/admin/users_app/client/')

def to_dashboard_events (request):  
    return redirect('/admin/events_app/events/')

def profile_view(request, id):
    profile = Client.objects.get(id = id)
    return render(request, 'users_app/profile_user.html', {'profile':profile})




from django.shortcuts import get_object_or_404
def modifier_profil_view(request, id_user):
    if request.method == 'POST':
        # mise a jour les donnees de l'utilisateur dans la table User Django
        user = get_object_or_404(User, id=id_user)
        user.nom = request.POST.get('nom')
        user.prenom = request.POST.get('prenom')
        user.email = request.POST.get('email')
        user.addresse = request.POST.get('addresse')
        user.save()
        print("----------------after user.save()")

        # mise a jour les donnees de l'utilisateur dans la table Clients
        clnt = get_object_or_404(Client, id=id_user)
        clnt.nom = request.POST.get('nom')
        clnt.prenom = request.POST.get('prenom')
        clnt.email = request.POST.get('email')
        clnt.addresse = request.POST.get('addresse')
        clnt.save()
        print("---------------after clnt.save()")

        return redirect('profile', id_user)

    return render(request, 'users_app/modifier_profil.html')


