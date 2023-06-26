from django.shortcuts import render

from insurance.services import get_adults_and_children_from_user, get_premium_prices


def calculate_insurance(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    sum_insured = int(request.POST['sum_insured'])
    tier_id = int(request.POST['city'][0])
    tenure_id = int(request.POST['tenure'][0])

    adults, children = get_adults_and_children_from_user(request.POST)

    result, total_rate = get_premium_prices(adults=adults, children=children, sum_insured=sum_insured, tier_id=tier_id,
                                            tenure_id=tenure_id)

    return render(request, 'result.html', context={"data": result, "total_rate": total_rate})
