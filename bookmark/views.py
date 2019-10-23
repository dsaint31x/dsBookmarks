from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView

from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

    paginate_by = 3

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('bookmark:list')

    # 기본으로 설정된 template 파일 이름 : model_form : CreateView, UpdateView
    # 다음을 통해 model_create로 변경.
    template_name_suffix = '_create'

from django.views.generic.detail import DetailView

class BookmarkDetailView(DetailView):
    model = Bookmark

from django.views.generic.edit import UpdateView

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'


from django.views.generic.edit import DeleteView

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')
