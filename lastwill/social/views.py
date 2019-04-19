import requests
import hashlib
import hmac

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount import app_settings, providers
from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter
from allauth.socialaccount.providers.facebook.provider import GRAPH_API_URL, GRAPH_API_VERSION, FacebookProvider
from rest_auth.registration.views import SocialLoginView
from rest_auth.registration.serializers import SocialLoginSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework import serializers
from lastwill.profile.serializers import init_profile
from lastwill.profile.helpers import valid_totp


def compute_appsecret_proof(app, token):
    msg = token.token.encode('utf-8')
    key = app.secret.encode('utf-8')
    appsecret_proof = hmac.new(
        key,
        msg,
        digestmod=hashlib.sha256).hexdigest()
    return appsecret_proof


def fb_complete_login(request, app, token):
    provider = providers.registry.by_id(FacebookProvider.id, request)
    print('provider fields', provider.get_fields(), flush=True)
    resp = requests.get(
        GRAPH_API_URL + '/me',
        params={
            'fields': ','.join(provider.get_fields()),
            'access_token': token.token,
            'appsecret_proof': compute_appsecret_proof(app, token)
        })
    print('requests params')
    print(GRAPH_API_URL + '/me', flush=True)
    print(token.token, flush=True)
    print(compute_appsecret_proof(app, token), flush=True)
    print('resp', resp, flush=True)
    resp.raise_for_status()
    extra_data = resp.json()
    print('try login', flush=True)
    login = provider.sociallogin_from_response(request, extra_data)
    return login


class FacebookOAuth2Adapter(OAuth2Adapter):
    provider_id = FacebookProvider.id
    # print('provider id', provider_id, flush=True)
    provider_default_auth_url = (
        'https://www.facebook.com/{}/dialog/oauth'.format(
            GRAPH_API_VERSION))

    settings = app_settings.PROVIDERS.get(provider_id, {})
    # print('settings', settings, flush=True)
    authorize_url = settings.get('AUTHORIZE_URL', provider_default_auth_url)
    # print('authorize_url', authorize_url, flush=True)
    access_token_url = GRAPH_API_URL + '/oauth/access_token'
    # print('access_token_url', access_token_url, flush=True)
    expires_in_key = 'expires_in'

    def complete_login(self, request, app, access_token, **kwargs):
        print('complete login', request, app, access_token, flush=True)
        return fb_complete_login(request, app, access_token)


class SocialLoginSerializer2FA(SocialLoginSerializer):
    email = serializers.CharField(required=False, allow_blank=True)
    totp = serializers.CharField(required=False, allow_blank=True)


class ProfileAndTotpSocialLoginView(SocialLoginView):
    serializer_class = SocialLoginSerializer2FA

    def login(self):
        self.user = self.serializer.validated_data['user']
        try:
            p = self.user.profile
        except ObjectDoesNotExist:
            print('try create user', flush=True)
            self.user.username = str(self.user.id)
            init_profile(self.user, is_social=True, lang=self.serializer.context['request'].COOKIES.get('lang', 'en'))
            self.user.save()
            print('user_created', flush=True)
        if self.user.profile.use_totp:
            totp = self.serializer.validated_data.get('totp', None)
            if not totp:
                logout(self.request)
                raise PermissionDenied(1032)
            if not valid_totp(self.user, totp):
                logout(self.request)
                raise PermissionDenied(1033)
        return super().login()
        

class FacebookLogin(ProfileAndTotpSocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class GoogleLogin(ProfileAndTotpSocialLoginView):
    adapter_class = GoogleOAuth2Adapter
