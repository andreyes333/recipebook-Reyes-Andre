from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe, RecipeImage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .forms import RecipeForm, RecipeImageForm
from django.urls import reverse_lazy


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe_detail.html"


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_add.html"
    success_url = "/recipes/list/"

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
    

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = "recipe_add.html"

    def get_success_url(self):
        return reverse_lazy('ledger:recipe-detail',
                            kwargs={'pk': self.object.recipe.pk})

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe"] = Recipe.objects.get(pk=self.kwargs['pk'])
        return context
