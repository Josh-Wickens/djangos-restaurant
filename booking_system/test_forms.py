from django.test import TestCase, SimpleTestCase
from .forms import ReserveTableForm


# Create your tests here.

class TestReserveForm(SimpleTestCase):
    def test_item_name_is_required(self):
        form = ReserveTableForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ReserveTableForm()
        self.assertNotEqual(form.Meta.fields, ['user', 'table', 'status'])
