from django.apps import AppConfig




class InsuranceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insurance'

    def ready(self):
        import pandas as pd
        from insurance.models import InsurancePlan

        df = pd.read_csv('assignment_raw_rate.csv')

        plans = []

        for index, row in df.iterrows():

            obj = InsurancePlan(product_code=row['ProductCode'],tier_id=row['TierID'],
                          plan_code=row['PlanCode'],
                            plan_name=row['PlanName'],
                            age=row['Age'],
                            insured_pattern=row['InsuredPattern'],
                            sum_insured=row['SumInsured'],
                            tenure=row['Tenure'],
                            rate=row['Rate'])

            plans.append(obj)
        if not InsurancePlan.objects.all().exists():
            InsurancePlan.objects.all().delete()
            InsurancePlan.objects.bulk_create(plans)






