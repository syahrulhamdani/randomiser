from dataclasses import dataclass, field, asdict

from randomiser.resources.address import Address
from randomiser.resources.employment import Employment
from randomiser.resources.subscription import Subscription


@dataclass
class User:
    id: str = field(default_factory=str)
    uid: str = field(default_factory=str)
    password: str = field(default_factory=str)
    first_name: str = field(default_factory=str)
    last_name: str = field(default_factory=str)
    email: str = field(default_factory=str)
    avatar: str = field(default_factory=str)
    gender: str = field(default_factory=str)
    phone_number: str = field(default_factory=str)
    social_insurance_number: str = field(default_factory=str)
    date_of_birth: str = field(default_factory=str)
    employment: Employment = field(default_factory=Employment)
    address: Address = field(default_factory=Address)
    cc_number: str = field(default_factory=str)
    subscription: Subscription = field(default_factory=Subscription)

    def to_dict(self):
        user = asdict(self)
        user.update({
            "address_" + key: value
            for key, value in user["address"].items()
        })
        user.update({
            "employment_" + key: value
            for key, value in user["employment"].items()
        })
        user.update({
            "subscription_" + key: value
            for key, value in user["subscription"].items()
        })
        user.pop("address")
        user.pop("employment")
        user.pop("subscription")

        return user
