from django.urls import reverse
import json
from rest_framework.test import APITestCase

# Create your tests here.


class LUTestCase(APITestCase):
    def test_lu_correct(self):
        request = {"matrix": [[10, -7, 0], [-3, 6, 2], [5, -1, 5]]}
        result_status = 200

        url = reverse("lu_decomposition")
        response = self.client.post(url, data=json.dumps(request), content_type="application/json")

        self.assertEqual(response.status_code, result_status)
    
    def test_lu_error(self):
        request = {"matrix": [["1", "2", 3], [1, 2, 3], [1, 2, 3], ["","",""]]}
        result_status = 400

        url = reverse("lu_decomposition")
        response = self.client.post(url, data=json.dumps(request), content_type="application/json")

        self.assertEqual(response.status_code, result_status)
    