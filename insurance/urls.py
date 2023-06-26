

from django.urls import path,include


from insurance.views import calculate_insurance

urlpatterns = [
    path('', calculate_insurance),

]
