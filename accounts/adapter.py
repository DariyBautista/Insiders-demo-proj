from allauth.account.adapter import DefaultAccountAdapter # type: ignore
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter # type: ignore

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)

        user.email = data.get('email') or user.email
        user.username = data.get('email').split('@')[0]
        user.first_name = data.get('first_name', '')
        user.last_name = data.get('last_name', '')

        return user
