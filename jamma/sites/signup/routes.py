from flask import Blueprint, request, jsonify, url_for, render_template
from jamma.verification.verification import Verification

signup_bp = Blueprint('signup', __name__)


@signup_bp.route('/verify', methods=['POST'])
def verify():
    args = request.args
    print(args)

    step = int(args.get('step'))
    print("signup_verify - step: %r" % step)
    if step == 1:
        phone_num = request.get_json('signupPhoneNUm')
        print(phone_num)
        return jsonify({'response': 'ok'})


@signup_bp.route('/otp', methods=['GET', 'POST'])
def otp():
    if request.method == 'GET':
        verification = Verification()
        secret, code, time_remaining = verification.generate_code()

        return jsonify({
            'secret': secret,
            'time_remaining': time_remaining
        })

    elif request.method == 'POST':
        json = request.get_json()
        print(json)
        verification = Verification()
        is_otp_valid = verification.verify_code(json['OTP'], json['secret'])

        if not is_otp_valid:
            return jsonify({
                'response': False,
                'message': 'Invalid or Expired OTP Code'
            })
        else:
            return jsonify({
                'response': True,
                'message': 'OTP Authenticated!'
            })


@signup_bp.route('/')
def signup():
    args = request.args
    print(args)

    step = args.get('step', default='1')
    print(step)
    print(type(step))
    endpoint = url_for('signup.verify') + f"?step={step}"
    next = url_for('signup.signup') + f"?step={int(step)+1}"

    if step == '1':
        return render_template('signup/signup.html',
                               step=step,
                               endpoint=endpoint,
                               next=next,
                               otp_endpoint=url_for('signup.otp'))
    if step == '2':
        return render_template('signup/signup.html',
                               step=step,
                               endpoint=endpoint,
                               next=next)
