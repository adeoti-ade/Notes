from django.test import TestCase
from django.contrib.auth import get_user_model
# from account.models import CustomUser


class UserManagersTests(TestCase):
    """
    This class test all the user manager
    """

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="user@user.com", password="foo")
        print("jkbjhvquywhvuhjavw", user)
        self.assertEqual(user.email, "user@user.com")  # test if user email is same as email passed
        self.assertTrue(user.is_active)  # check if user is active
        self.assertFalse(user.is_staff)  # check is user isn't created as a staff
        self.assertFalse(user.is_superuser)  # check if user isn't created as a superuser
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="foo")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)

