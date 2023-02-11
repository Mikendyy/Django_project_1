def fun_send_mail_to_active(active_link, active_mail):
    from django.core.mail import send_mail
    send_mail(
        "Link to activate an account.",
        f"Hi, your link to activate - {active_link}",
        'testim0313@gmail.com',
        [active_mail],
        fail_silently=False,
    )
