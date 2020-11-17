from unittest import TestCase

from assertpy import assert_that

from main import convert_currency


class TestCurrencyConverter(TestCase):
    def test_0_GBP_EUROS(self):
        euros = convert_currency(
            amount=0,
            from_currency='GBP',
            to_currency='EUR'
        )
        assert_that(euros).is_equal_to(0)

    def test_100_USD_EUROS_date(self):
        euros = convert_currency(
            amount=100,
            from_currency='USD',
            to_currency='EUR'
        )
        assert_that(euros).is_equal_to(85.82)
