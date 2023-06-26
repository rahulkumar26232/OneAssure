import redis

from OneAssure import settings
from insurance.models import InsurancePlan

REDIS_INSTANCE = redis.from_url(url=settings.REDIS_URI, decode_responses=True)


class InsuranceAmountCache:
    key = 'sum_insured_{}_tier_{}_tenure_{}_Age_{}'

    @classmethod
    def get(cls, sum_insured: int, tier_id: int, tenure_id: int, age: int) -> int:
        data = REDIS_INSTANCE.get(cls.key.format(sum_insured, tier_id, tenure_id, age))

        if not data:
            plan = InsurancePlan.objects.filter(sum_insured=sum_insured, tier_id=tier_id, tenure=tenure_id,
                                                age=age).first()
            data = plan.rate
            cls.set(sum_insured=sum_insured, tier_id=tier_id, tenure_id=tenure_id, age=age, rate=plan.rate)

        return int(data)

    @classmethod
    def set(cls, sum_insured: int, tier_id: int, tenure_id: int, age: int, rate: int):
        REDIS_INSTANCE.set(cls.key.format(sum_insured, tier_id, tenure_id, age), rate)
