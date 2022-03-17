from django.test import TestCase

from api.serializers import CompanySerializer

from .factories import CompanyFactory


class CompanySerializerTest(TestCase):
    def test_model_fields(self):
        """Serializer data matches the Company object for each field."""
        company = CompanyFactory()
        serializer = CompanySerializer
        for field_name in [
            "id",
            "name",
            "description",
            "website",
            "street_line_1",
            "street_line_2",
            "city",
            "state",
            "zipcode",
        ]:
            self.assertEqual(serializer.data[field_name], getattr(company, field_name))
