import pyotp
from datetime import datetime, timedelta
from .func import send_email_to_client


def send_otp(request):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=60)
    otp = totp.now()
    request.session["otp_secret_key"] = totp.secret
    valid_date = datetime.now() + timedelta(minutes=1)
    request.session["otp_valid_date"] = str(valid_date)

    # send via email
    user_email = request.session.get("email")
    # user_email = "vyshnav.m345@gmail.com"
    subject = "Password Reset OTP"
    message = f"Your OTP for cybershopping is {otp}"
    send_email_to_client(subject, message, user_email)
    print(f"Your OTP is {otp}")
    return otp
