from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from .models import EntryModel

def index(request):
  if request.user.is_authenticated:
    search_mode = False
    # ログインしているユーザーの日記を取得、日付と時刻で降順ソート
    entry_list = EntryModel.objects.filter(user=request.user).order_by("-date", "-time")

    # 検索(q)がある場合は絞り込み
    q = request.GET.get("q")
    if q:
      search_mode = True
      # キーワードをスペースで分割して、それぞれのキーワードが含まれるエントリーを取得
      keywords = q.split()
      for keyword in keywords:
        entry_list = entry_list.filter(content__icontains=keyword)

    return render(request, "diary/index_home.html", {'entry_list': entry_list, 'search_mode': search_mode})
  else:
    return render(request, "diary/index_entrance.html")

class EntryBaseView(LoginRequiredMixin):
  """編集画面の基底クラス"""

  model = EntryModel
  fields = {"title", "content", "tags", "date", "time"}
  success_url = reverse_lazy("diary:home")

  def get_object(self, queryset=None):
    obj: EntryModel = super().get_object(queryset)

    if obj.user != self.request.user:
      raise PermissionError("この記録を編集する権限がありません")

    # 日付と時刻をHTMLが理解できる文字列に変換
    obj.date = obj.date.strftime("%Y-%m-%d")
    obj.time = obj.time.strftime("%H:%M")

    return obj
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    # データがある場合(UpdateView)のみ処理
    if self.object:
      # タグを変数としてテンプレートに渡す
      context["tags"] = self.object.tags

    return context
  
  def post(self, request, *args, **kwargs):
    # PostされたTagたちを適切な形式(リスト)に変換する
    request.POST = request.POST.copy()
    request.POST["tags"] = request.POST.getlist("tags")

    return super().post(request, *args, **kwargs)
  
  def form_valid(self, form):
    # ユーザー情報をセット
    form.instance.user = self.request.user

    return super().form_valid(form)
  
class CreateEntryView(EntryBaseView, CreateView):
    template_name = "diary/editor.html"

class UpdateEntryView(EntryBaseView, UpdateView):
    template_name = "diary/editor.html"

@require_POST
def delete_entry(request, pk):
  entry = EntryModel.objects.get(pk=pk)
  entry.delete()
  return redirect("diary:home")