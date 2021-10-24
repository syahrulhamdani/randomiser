from dataclasses import dataclass, field, asdict


@dataclass
class Address:
    id: str = field(default_factory=str)
    uid: str = field(default_factory=str)
    city: str = field(default_factory=str)
    street_name: str = field(default_factory=str)
    street_address: str = field(default_factory=str)
    secondary_address: str = field(default_factory=str)
    building_number: str = field(default_factory=str)
    mail_box: str = field(default_factory=str)
    community: str = field(default_factory=str)
    zip_code: str = field(default_factory=str)
    zip: str = field(default_factory=str)
    postcode: str = field(default_factory=str)
    time_zone: str = field(default_factory=str)
    street_suffix: str = field(default_factory=str)
    city_suffix: str = field(default_factory=str)
    city_prefix: str = field(default_factory=str)
    state: str = field(default_factory=str)
    state_abbr: str = field(default_factory=str)
    country: str = field(default_factory=str)
    country_code: str = field(default_factory=str)
    latitude: str = field(default_factory=str)
    longitude: str = field(default_factory=str)
    full_address: str = field(default_factory=str)

    def to_dict(self):
        return asdict(self)
