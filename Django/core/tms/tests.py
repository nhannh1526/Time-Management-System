from datetime import date

# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase
from tms.models import RequestType, Reason, Request


class Test_Create_Request(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_request_type = RequestType.objects.create(
            request_type='Work from home (WFH_Covid19)')
        test_reason = Reason.objects.create(reason='Other')

        testuser1 = User.objects.create_user(
            username='user01', password='Admin@123')
        testuser1.save()

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
        test_request.save()

    def test_request_content(self):
        request_type = RequestType.objects.get(id=1)
        reason = Reason.objects.get(id=1)
        request = Request.objects.get(id=1)
        owner = f'{request.owner}'
        # request_type = f'{request.request_type}'
        # reason = f'{request.reason}'
        supervisor = f'{request.supervisor}'
        approver = f'{request.approver}'
        self.assertEqual(str(request_type), 'Work from home (WFH_Covid19)')
        self.assertEqual(str(reason), 'Other')
        self.assertEqual(owner, 'user01')
        self.assertEqual(supervisor, 'user01')
        self.assertEqual(approver, 'user01')
