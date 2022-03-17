from django.test import TestCase

from api.models import Company

from .factories import CompanyFactory


class CompanyTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        company_factory = CompanyFactory()
        company = Company()
        self.assertEqual(str(company_factory), company.name)
