from insurance.cache import InsuranceAmountCache
from insurance.data_class import ResultDataclass


def get_adults_and_children_from_user(data: dict):
    adults = []
    children = []

    for key, val in data.items():

        if 'adults_age' in key or "adult_age" in key:
            adults.append(int(val))
        if ('children_age' in key or "child" in key) and val != '':
            children.append(int(val))

    adults.sort(reverse=True)

    return adults, children


def validate_if_floater_discount_applicable(adults) -> bool:
    if len(adults) > 1:
        return True
    return False


def get_adult_premiums(is_floater_discount_applicable: bool, adults: list[int], sum_insured: int, tier_id: int,
                       tenure_id: int):
    adults_rate = 0
    adults_result = []

    for idx, age in enumerate(adults):
        base_rate = InsuranceAmountCache.get(sum_insured=sum_insured, tier_id=tier_id, tenure_id=tenure_id, age=age)
        floater_discount = 0
        discounted_rate = base_rate
        if is_floater_discount_applicable and idx > 0:
            floater_discount = 50
            discounted_rate = base_rate / 2

        temp_result = ResultDataclass(base_rate=base_rate, floater_discount=floater_discount,
                                      discounted_rate=discounted_rate, description=f"Adult {str(idx + 1)}", age=age)

        adults_result.append(temp_result.__dict__)
        adults_rate += discounted_rate

    return adults_result, adults_rate


def get_children_premiums(is_floater_discount_applicable: bool, children: list[int], sum_insured: int, tier_id: int,
                          tenure_id: int):
    children_rate = 0
    children_results = []

    for idx, age in enumerate(children):
        base_rate = InsuranceAmountCache.get(sum_insured=sum_insured, tier_id=tier_id, tenure_id=tenure_id, age=age)
        floater_discount = 0
        discounted_rate = base_rate
        if is_floater_discount_applicable:
            floater_discount = 50
            discounted_rate = base_rate / 2

        temp_result = ResultDataclass(base_rate=base_rate, floater_discount=floater_discount,
                                      discounted_rate=discounted_rate, description=f"Children {str(idx + 1)}", age=age)

        children_results.append(temp_result.__dict__)
        children_rate += discounted_rate

    return children_results, children_rate


def get_premium_prices(adults: list[int], children: list[int], sum_insured: int, tier_id: int, tenure_id: int):
    result = []

    is_floater_discount_applicable = validate_if_floater_discount_applicable(adults)

    adults_result, adults_rate = get_adult_premiums(is_floater_discount_applicable, adults, sum_insured, tier_id,
                                                    tenure_id)
    children_results, children_rate = get_children_premiums(is_floater_discount_applicable, children, sum_insured,
                                                            tier_id, tenure_id)

    result.extend(adults_result)
    result.extend(children_results)

    return result, adults_rate + children_rate
