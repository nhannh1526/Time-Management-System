from datetime import date

from django.contrib.auth.models import User
# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from tms.models import RequestType, Reason, Request


class RequestTests(APITestCase):
    def test_view_requests(self):
        url = reverse('tms_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_account(self):
        self.test_request_type = RequestType.objects.create(
            name='Work from home (WFH_Covid19)')
        self.test_reason = Reason.objects.create(name='Other')

        self.testuser1 = User.objects.create_user(
            username='user01', password='Admin@123')

        data = {"owner": 1,
                "request_type": 1,
                "start_date": str(date.today()),
                "end_date": str(date.today()),
                "partial_day": "ALL",
                "reason": 1,
                "approver": 1,
                "supervisor": 1}
        url = reverse('tms_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 13)
        root = reverse(('tms_api:detailcreate'), kwargs={'pk': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_update(self):
        client = APIClient()

        self.test_request_type = RequestType.objects.create(
            name='Work from home (WFH_Covid19)')
        test_reason = Reason.objects.create(name='Other')
        self.testuser1 = User.objects.create_user(
            username='user01', password='Admin@123')
        self.testuser2 = User.objects.create_user(
            username='user02', password='Admin@123')

        test_request = Request.objects.create(
            owner_id=1,
            request_type_id=1,
            start_date=str(date.today()),
            end_date=str(date.today()),
            partial_day='ALL',
            reason_id=1,
            approver_id=1,
            supervisor_id=1
        )

        client.login(username=self.testuser1.username,
                     password='Admin@123')
        url = reverse(('tms_api:detailcreate'), kwargs={'pk': 1})

        response = client.put(
            url, {"owner": 1,
                  "request_type": 1,
                  "start_date": str(date.today()),
                  "end_date": str(date.today()),
                  "partial_day": "ALL",
                  "reason": 1,
                  "detail_reason": "Other",
                  "approver": 1,
                  "supervisor": 1}, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
