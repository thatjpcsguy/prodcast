def send_email(to, subject, template):
    return client.send_email(
        Source='James & James - The Prodcast <james@theprodcast.io>',
        Destination={'ToAddresses': [to]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Html': {'Data': open(template, 'rU').read()}}
        },
        ReplyToAddresses=['james@theprodcast.io'],
        ReturnPath='james@theprodcast.io',
    )
