from dataclasses import dataclass, field, asdict


@dataclass
class Subscription:
    id: str = field(default_factory=str)
    uid: str = field(default_factory=str)
    plan: str = field(default_factory=str)
    status: str = field(default_factory=str)
    payment_method: str = field(default_factory=str)
    subscription_term: str = field(default_factory=str)
    payment_term: str = field(default_factory=str)

    def to_dict(self):
        return asdict(self)
