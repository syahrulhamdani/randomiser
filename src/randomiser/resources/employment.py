from dataclasses import dataclass, field, asdict


@dataclass
class Employment:
    title: str = field(default_factory=str)
    key_skill: str = field(default_factory=str)

    def to_dict(self):
        return asdict(self)
