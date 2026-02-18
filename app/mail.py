from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_contact_notification(contact):
    """
    Sends inquiry email to admin without external template
    """

    subject = f"New Inquiry from {contact.name}"

    html_content = f"""
    <div style="font-family:Arial; background:#f4f6f8; padding:20px;">
        <div style="max-width:600px; margin:auto; background:white;
                    padding:25px; border-radius:10px;
                    box-shadow:0 4px 10px rgba(0,0,0,0.08);">

            <h2 style="color:#0b3c6f;">📩 New Inquiry Received From Website</h2>

            <p><strong>Name:</strong> {contact.name}</p>
            <p><strong>Phone:</strong> {contact.phone}</p>
            <p><strong>Course:</strong> {contact.course}</p>
            <p><strong>Location:</strong> {contact.location}</p>
            <p><strong>Message:</strong> {contact.message}</p>
            <p><strong>Date:</strong> {contact.created_at}</p>

            <hr style="margin:20px 0">

            <p style="font-size:12px;color:#777;">
                Learncare Education Hub
            </p>

        </div>
    </div>
    """

    msg = EmailMultiAlternatives(
        subject=subject,
        body="New inquiry received.",   # fallback text
        from_email=settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER],
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()
