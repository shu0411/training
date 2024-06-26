import logging

from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InquiryForm
from .models import Diary

logger = logging.getLogger(__name__)    # ロガーの取得

class IndexView(generic.TemplateView):
    template_name = 'index.html'    # 使用するテンプレート

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

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at')
        return diaries