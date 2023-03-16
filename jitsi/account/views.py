from django.views import View
from django.contrib.auth import login, logout, get_user_model
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm, LoginForm, TeamForm
from .models import Account, Team


class HomeView(View):
    template_name = "home.html"
    context = dict()
    
    def get(self, *args, **kwargs):
        username = getattr(self.request.user, "username", "")
        team_qs = Team.objects.filter(account__username=username)
        if team_qs.exists():
            self.context["team"] = team_qs.first().name
        else:
            self.context['team'] = "None"
        return render(self.request, self.template_name, self.context)
    
    
home = HomeView.as_view()


class SignupView(View):
    template_name = "signup.html"
    context = dict()
    
    def get(self, *args, **kwargs):
        self.context["form"] = SignUpForm()
        return render(self.request, self.template_name, self.context)
    
    def post(self, *args, **kwargs):
        data = SignUpForm(data=self.request.POST)
        if data.is_valid():
            username = data.cleaned_data.get("username")
            data.save(commit=True)
            user = get_user_model().objects.get(username=username)
            login(self.request, user)
            return redirect("team")
        else:
            self.context["form"] = data
            return render(self.request, self.template_name, self.context)
    

signup = SignupView.as_view()


class LoginView(View):
    template_name = "login.html"
    context = dict()
    
    def get(self, *args, **kwargs):
        self.context["form"] = LoginForm()
        return render(self.request, self.template_name, self.context)
    
    def post(self, *args, **kwargs):
        data = LoginForm(data=self.request.POST)
        if data.is_valid():
            username = data.cleaned_data.get("username")
            user_qs = Account.objects.filter(username=username)
            password = data.cleaned_data.get("password")
            if user_qs.exists() and user_qs.first().check_password(password):
                user = get_user_model().objects.get(username=username)
                login(self.request, user)
                return redirect("home")
        return redirect("login")


login_account = LoginView.as_view()


class LogoutView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return redirect("login")


logout_account = LogoutView.as_view()


class JoinOrAddTeam(LoginRequiredMixin, View):
    login_url = reverse_lazy("login")
    template_name = "team.html"
    context = dict()
    
    def get(self, *args, **kwargs):
        team_qs = Team.objects.filter(account__username=self.request.user.username)
        if team_qs.exists():
            return redirect("home")
        self.context["form"] = TeamForm()
        return render(self.request, self.template_name, self.context)
    
    def post(self, *args, **kwargs):
        data = TeamForm(data=self.request.POST)
        if data.is_valid():
            name = data.cleaned_data.get("name")
            team, _ = Team.objects.get_or_create(name=name,
                                                 jitsi_url_path=f"http://meet.jit.si/{name}")
            user = Account.objects.get(username=self.request.user.username)
            user.team = team
            user.save()
        return redirect("home")
                

joinoradd_team = JoinOrAddTeam.as_view()


class ExitTeamView(View):
    def get(self, *args, **kwargs):
        user_qs = (
            Account
            .objects
            .filter(username=self.request.user.username)
        )
        if (
            user_qs.exists() 
            and getattr(user_qs.first(), "team", None) is not None
        ):
            user_qs.update(team=None)
        return redirect("home")    


exit_team = ExitTeamView.as_view()