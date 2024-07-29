from django.db import models
from django.forms import ModelForm

class Bargiri(models.Model):
    trans_name=models.CharField(max_length=100)
    F1_1 = models.IntegerField(default=0)
    F1_2 = models.IntegerField(default=0)
    F1_3 = models.IntegerField(default=0)
    F2_1 = models.IntegerField(default=0)
    F2_2 = models.IntegerField(default=0)
    F2_3 = models.IntegerField(default=0)
    F3_1 = models.IntegerField(default=0)
    F3_2 = models.IntegerField(default=0)
    F3_3 = models.IntegerField(default=0)
    F4_1 = models.IntegerField(default=0)
    F4_2 = models.IntegerField(default=0)
    F4_3 = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.trans_name
class BargiriForm(ModelForm):
    class Meta:
        model = Bargiri
        fields = ["trans_name", "F1_1", "F1_2","F1_3","F2_1", "F2_2","F2_3","F3_1", "F3_2","F3_3","F4_1", "F4_2","F4_3"]