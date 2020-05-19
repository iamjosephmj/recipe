from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """
        This method is used to create a user with email
        address successfully.
        """
        email = 'joseph@123.com'
        password = 'open@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        This method is used to check if the user email is normalized
        """
        email = "josFpj@EFEfFE.COM"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertTrue(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        This method is used to test if a user have created invalid email.
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_if_superuser_is_created(self):
        """
        This class is used to check if the super user is created
        """
        email = "admin@gmail.com"
        password = "password"
        user = get_user_model().objects.create_super_user(
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
