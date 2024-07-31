from django.test import TestCase

from .forms import DriverCreationForm


class TestDriverCreationForm(TestCase):
    def setUp(self):
        self.base_driver_dict = {
            "username": "test",
            "password1": "s3cur3 p4ssw0rd",
            "password2": "s3cur3 p4ssw0rd",
        }

    def test_correct_license_number(self):
        self.base_driver_dict["license_number"] = "ABC04308"
        form = DriverCreationForm(self.base_driver_dict)
        self.assertTrue(form.is_valid())

    def test_too_short_license_number(self):
        self.base_driver_dict["license_number"] = "ABC4308"
        form = DriverCreationForm(self.base_driver_dict)
        self.assertFalse(form.is_valid())

    def test_too_long_license_number(self):
        self.base_driver_dict["license_number"] = "ABC043081"
        form = DriverCreationForm(self.base_driver_dict)
        self.assertFalse(form.is_valid())

    def test_numeric_license_number(self):
        self.base_driver_dict["license_number"] = "12345678"
        form = DriverCreationForm(self.base_driver_dict)
        self.assertFalse(form.is_valid())

    def test_license_number_with_two_letters(self):
        self.base_driver_dict["license_number"] = "AB304308"
        form = DriverCreationForm(self.base_driver_dict)
        self.assertFalse(form.is_valid())

    def test_license_number_with_swapped_parts(self):
        self.base_driver_dict["license_number"] = "04308ABC"
        form = DriverCreationForm(self.base_driver_dict)
        self.assertFalse(form.is_valid())

    def test_license_number_with_only_letters(self):
        self.base_driver_dict["license_number"] = "ABCDEFGH"
        form = DriverCreationForm(self.base_driver_dict)
        self.assertFalse(form.is_valid())
