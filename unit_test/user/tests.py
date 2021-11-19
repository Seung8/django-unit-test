from django.contrib.auth import get_user_model
from django.test import TestCase


class SignUpTest(TestCase):
    def setUp(self):
        self.model = get_user_model()

    def test_signup_success(self):
        print('\n[회원가입 성공] 정상')

        u = self.model.objects.create_user(
            name='unit_test',
            email='unit_test@tester.com',
            phone='010-0000-0000',
            password='1234qwer',
        )

        self.assertEqual(isinstance(u, self.model), True)

    def test_signup_fail_missing_name(self):
        print('\n[회원가입 실패] 이름(name) 누락')

        error = None

        try:
            self.model.objects.create_user(
                email='unit_test@tester.com',
                phone='010-0000-0000',
                password='1234qwer',
            )
        except Exception as e:
            error = e

        self.assertEqual(isinstance(error, TypeError), True)

    def test_signup_fail_missing_email(self):
        print('\n[회원가입 실패] 이메일(email) 누락')

        error = None

        try:
            self.model.objects.create_user(
                name='unit_tester',
                phone='010-0000-0000',
                password='1234qwer',
            )
        except Exception as e:
            error = e

        self.assertEqual(isinstance(error, TypeError), True)

    def test_signup_fail_invalid_email(self):
        print('\n[회원가입 실패] 이메일(email) 형식 오류')

        error = None

        try:
            self.model.objects.create_user(
                name='unit_tester',
                email='unit_test',
                phone='010-0000-0000',
                password='1234qwer',
            )
        except Exception as e:
            error = e

        self.assertEqual(isinstance(error, TypeError), True)

    def test_signup_fail_missing_phone(self):
        print('\n[회원가입 실패] 전화번호(phone) 누락')

        error = None

        try:
            self.model.objects.create_user(
                name='unit_tester',
                email='tester@test.com',
                password='1234qwer',
            )
        except Exception as e:
            error = e

        self.assertEqual(isinstance(error, TypeError), True)

    def test_signup_fail_invalid_phone(self):
        print('\n[회원가입 실패] 전화번호(phone) 형식 오류')

        error = None

        try:
            self.model.objects.create_user(
                name='unit_tester',
                email='unit_test',
                phone='01000000000',
                password='1234qwer',
            )
        except Exception as e:
            error = e

        self.assertEqual(isinstance(error, TypeError), True)
