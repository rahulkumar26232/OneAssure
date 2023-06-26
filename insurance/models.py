from django.db import models


class InsurancePlan(models.Model):

    class TierChoices(models.IntegerChoices):
        tier1 = 1, 'tier-1'
        tier2 = 2, 'tier-2'
        tier3 = 3, 'tier-3'

    class TenureChoices(models.IntegerChoices):
        one_year = 1 ,'1 Year'
        Two_year = 2, '2 Year'
        Three_year = 3, '3 Year'

    product_code = models.CharField(max_length=100)
    tier_id = models.IntegerField(choices=TierChoices.choices, default=TierChoices.tier1)
    plan_code = models.CharField(max_length=100)
    plan_name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    insured_pattern = models.IntegerField()
    sum_insured = models.IntegerField()
    tenure = models.IntegerField(choices=TenureChoices.choices, default=TenureChoices.one_year)
    rate = models.IntegerField()

