from django.test import TestCase

from api.models import Company

from .factories import CompanyFactory


class CompanyTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        company = CompanyFactory()
        self.assertEqual(str(company), company.name)
