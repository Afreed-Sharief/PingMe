from django.db import models

# Create your models here.
# class profile(models.Model):
#     name = models.
#
#     def __init__(self, coin_price=None, user=None, *args, **kwargs):
#         if user:
#             self.user = user
#             qs_coin = Portfolio.objects.filter(user=self.user).values('coin').distinct()
#             super(TransactionForm, self).__init__(self.user, *args, **kwargs)
#             self.fields['coin'].queryset = qs_coin
#
#     def __init__(self, coin_price=None, user=None, *args, **kwargs):
#         super(TransactionForm, self).__init__(*args, **kwargs)
#         if user:
#             self.user = user
#             qs_coin = Portfolio.objects.filter(user=self.user).values('coin').distinct()
#             self.fields['coin'].queryset = qs_coin


