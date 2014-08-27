from rapid_response_kit.utils.clients import twilio

from flask import render_template, request, flash, redirect
from rapid_response_kit.utils.helpers import parse_numbers, echo_twimlet, twilio_numbers


def install(app):
    app.config.apps.register('broadcast', 'Broadcast', '/broadcast')

    @app.route('/broadcast', methods=['GET'])
    def show_broadcast():
        numbers = twilio_numbers('phone_number')
        return render_template("broadcast.html", numbers=numbers)


    @app.route('/broadcast', methods=['POST'])
    def do_broadcast():
        numbers = parse_numbers(request.form.get('numbers', ''))
        twiml = "<Response><Say>{}</Say></Response>"
        url = echo_twimlet(twiml.format(request.form.get('message', '')))

        client = twilio()

        for number in numbers:
            try:
                if request.form['method'] == 'sms':
                    client.messages.create(
                        body=request.form['message'],
                        to=number,
                        from_=request.form['twilio_number']
                    )
                else:
                    client.calls.create(
                        url=url,
                        to=number,
                        from_=request.form['twilio_number']
                    )
                flash("Sent {} the message".format(number), 'success')
            except Exception:
                flash("Failed to send to {}".format(number), 'danger')

        return redirect('/broadcast')