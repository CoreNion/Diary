from django.db import models

# 日記モデル
class EntryModel(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  tags = models.JSONField(blank=True, null=True)
  date = models.DateTimeField()

  def __str__(self) -> str:
    return self.title
