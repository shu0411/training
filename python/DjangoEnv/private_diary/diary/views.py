import logging

from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404

from .forms import InquiryForm, DiaryCreateForm
from .models import Diary

logger = logging.getLogger(__name__)    # ロガーの取得

class IndexView(generic.TemplateView):
    template_name = 'index.html'    # 使用するテンプレート

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    #オーバーライド
    
    def test_func(self):
        # ログインユーザーと日記のユーザーが一致するか判定
        diary = get_object_or_404(Diary, pk=self.kwargs['pk'])
        return diary.user == self.request.user

class InquiryView(generic.FormView):
    template_name = 'inquiry.html'  # 使用するテンプレート
    form_class = InquiryForm    # formのクラスを指定
    success_url = reverse_lazy('diary:inquiry') # 送信完了時のリダイレクト先

    # フォームのバリデーションを通過したときに呼ばれるメソッド(オーバーライド)
    def form_valid(self, form):
        form.send_email()   # メール送信
        messages.success(self.request, 'メッセージを送信しました。')    # メッセージを画面に表示
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))   # ログ出力
        return super().form_valid(form)   # 元のform_validメソッドを呼び出し

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'   # 使用するテンプレート
    paginate_by = 2  # 1ページに表示するレコードの件数

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries
    
class DiaryDetailView(LoginRequiredMixin, OnlyYouMixin, generic.DetailView):
    model = Diary
    template_name = 'diary_detail.html' # 使用するテンプレート

class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Diary
    template_name = 'diary_create.html'
    form_class = DiaryCreateForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '日記の作成に失敗しました。')
        return super().form_invalid(form)

class DiaryUpdateView(LoginRequiredMixin, OnlyYouMixin, generic.UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    form_class = DiaryCreateForm

    def get_success_url(self):
        return reverse_lazy('diary:diary_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '日記を更新しました。')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '日記の更新に失敗しました。')
        return super().form_invalid(form)

class DiaryDeleteView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('diary:diary_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '日記を削除しました。')
        return super().delete(request, *args, **kwargs)
