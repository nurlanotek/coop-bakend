from django.contrib.auth.tokens import PasswordResetTokenGenerator


class AppTokenGenerator(PasswordResetTokenGenerator):
    pass

token_generator = AppTokenGenerator()