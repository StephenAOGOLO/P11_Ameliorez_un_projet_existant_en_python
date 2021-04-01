""" This module using creating, formatting and sending an activation account mail """
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.http import HttpResponse


def send_confirmation(request, user, usermail):
    """ This function is called to concentrate data into a mail and to send it """
    check_user(user)
    confirmation = set_confirmation(request, user, "registration/confirmation.html")
    subject = "Test de confirmation - django"
    body = confirmation
    destination = usermail
    source = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, body, source, [destination])
    msg.content_subtype = "html"
    msg.send()
    print("\n", "Confirmation sent", "\n")


def check_user(user):
    """ This function is called to disable a the concerned user """
    print("Checking user...")
    user.is_active = False
    user.save()
    print("User checked...")
    print("User id = {}".format(user.id))
    print("User pk = {}".format(user.pk))


def set_confirmation(request, user, template):
    """ This function is called to formatting the activation link and the mail content """
    link = get_current_site(request)
    uid = urlsafe_base64_encode(force_bytes(user.id))
    token = account_activation_token.make_token(user)
    context = {"link": link.domain,
               "user": user,
               "uid": uid,
               "token": token
               }
    confirmation = render_to_string(template, context)
    print("before sending mail, user_id = {}".format(user.id))
    print("before sending mail, uid = {}".format(uid))
    return confirmation


class Tokenizer(PasswordResetTokenGenerator):
    """ This method is a native private 'PasswordResetTokenGenerator' one.
    It is called to secure the activation link"""
    def _make_hash_value(self, user, timestamp):
        login_timestamp = '' if user.last_login is None else user.last_login.replace(microsecond=0, tzinfo=None)
        return str(user.pk) + user.password + str(login_timestamp) + str(timestamp)


account_activation_token = Tokenizer()
