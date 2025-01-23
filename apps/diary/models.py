from django.db import models

# 日記モデル
class EntryModel(models.Model):
  user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  content = models.TextField()
  tags = models.JSONField(blank=True, null=True)
  date = models.DateField()
  time = models.TimeField()
  public = models.BooleanField(default=False)

  def __str__(self) -> str:
    return self.title
