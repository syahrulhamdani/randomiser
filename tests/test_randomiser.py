from unittest.mock import patch

import pytest

from randomiser import Randomizer
from randomiser.exception import ResourceNotFound
from randomiser.resources import *


def test_resource_not_found():
    with pytest.raises(ResourceNotFound):
        randomizer = Randomizer("random")

def test_resource_to_dict():
    user = User()
    employment = Employment()
    address = Address()
    subscription = Subscription()

    assert user.to_dict() == {
        "id": "",
        "uid": "",
        "password": "",
        "first_name": "",
        "last_name": "",
        "email": "",
        "avatar": "",
        "gender": "",
        "phone_number": "",
        "social_insurance_number": "",
        "date_of_birth": "",
        "employment_title": "",
        "employment_key_skill": "",
        "address_id": "",
        "address_uid": "",
        "address_city": "",
        "address_street_name": "",
        "address_street_address": "",
        "address_secondary_address": "",
        "address_building_number": "",
        "address_mail_box": "",
        "address_community": "",
        "address_zip_code": "",
        "address_zip": "",
        "address_postcode": "",
        "address_time_zone": "",
        "address_street_suffix": "",
        "address_city_suffix": "",
        "address_city_prefix": "",
        "address_state": "",
        "address_state_abbr": "",
        "address_country": "",
        "address_country_code": "",
        "address_latitude": "",
        "address_longitude": "",
        "address_full_address": "",
        "cc_number": "",
        "subscription_id": "",
        "subscription_uid": "",
        "subscription_plan": "",
        "subscription_status": "",
        "subscription_payment_method": "",
        "subscription_subscription_term": "",
        "subscription_payment_term": "",
    }
    assert employment.to_dict() == {
        "title": "",
        "key_skill": "",
    }
    assert address.to_dict() == {
        "id": "",
        "uid": "",
        "city": "",
        "street_name": "",
        "street_address": "",
        "secondary_address": "",
        "building_number": "",
        "mail_box": "",
        "community": "",
        "zip_code": "",
        "zip": "",
        "postcode": "",
        "time_zone": "",
        "street_suffix": "",
        "city_suffix": "",
        "city_prefix": "",
        "state": "",
        "state_abbr": "",
        "country": "",
        "country_code": "",
        "latitude": "",
        "longitude": "",
        "full_address": "",
    }
    assert subscription.to_dict() == {
        "id": "",
        "uid": "",
        "plan": "",
        "status": "",
        "payment_method": "",
        "subscription_term": "",
        "payment_term": "",
    }
