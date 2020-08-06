from django.test import TestCase
from .forms import InvoiceForm, LineItemFormset
from django.urls import reverse

  
# Create your tests here.
class CreateInvoiceViewTest(TestCase):
    def test_full_form(self):
        data =  {
            'customer':'Xyz Company',
            'customer_email':'customer@company.com',
            'billing_address':'C-7, mg road 25',
            'date':'2020-07-21',
            'due_date':'2020-08-10',
            'message':'some default message',
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '0',
            'form-MIN_NUM_FORMS': '0',
            'form-MAX_NUM_FORMS': '1000',
            'form-0-service': 'Security Guards',
            'form-0-description': '1400 2100 Security Guards',
            'form-0-quantity': '1',
            'form-0-rate': '16.85',
            'form-1-service': 'Security Guards 1',
            'form-1-description': '1400 2100 Security Guards 1',
            'form-1-quantity': '1',
            'form-1-rate': '18.85',
        }
        response = self.client.post(reverse('invoice:invoice-create'),data=data)
        self.assertEqual(response.status_code, 302)


class InvoiceListViewTest(TestCase):
    def test_post_method(self):
        data = {
            'invoice_id': ['2','3'],
            'status': '1',
        }

        response = self.client.post(reverse('invoice:invoice-list'), data=data)
        self.assertEqual(response.status_code, 302)                    