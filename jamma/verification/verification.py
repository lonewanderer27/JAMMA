import pyotp
import datetime


class Verification():

    def generate_code(self, digits: int = 4, interval=90):
        secret = pyotp.random_base32()
        totp = pyotp.TOTP(s=secret, digits=digits, interval=interval)
        code = totp.now()
        time_remaining = totp.interval - datetime.datetime.now().timestamp() % totp.interval
        print('Code: %r' % code)
        print('Time Remaining: %r' % time_remaining)
        return secret, code, time_remaining

    def verify_code(self, OTP, secret, digits: int = 4, interval=90):
        print("Secret: %r" % secret)
        totp = pyotp.TOTP(secret, digits, interval=interval)
        print("OTP from TOTP: %r" % totp.now())
        print("OTP from User: %r" % OTP)
        is_valid = totp.verify(OTP)
        print('Is %r valid code? %r' % (OTP, is_valid))
        return is_valid
