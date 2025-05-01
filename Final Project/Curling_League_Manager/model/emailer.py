import yagmail


class Emailer:
    """Singleton emailer class."""

    sender_address = None
    """Sender address"""

    _sole_instance = None
    """The only instance of Emailer"""

    @classmethod
    def configure(cls, sender_address):
        """
        Sets the sender email address to send emails.
        Args:
            sender_address: String with sender email address.

        Returns:

        """
        cls.sender_address = sender_address

    @classmethod
    def instance(cls):
        """
        Returns the only instance of the Emailer class.
        Returns:
            The only instance of the Emailer class.
        """
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    def send_plain_email(self, recipients, subject, message):
        """
        Temp emailer for Curling League Manager.  The only output for the email is the message that it is emailing each
        email in recipients.
        Args:
            recipients: list of String representing the emails of everyone to email
            subject: String representing the subject of the email
            message: String representing the body of the email

        Returns:
            Sends emails to all recipients in the list.
        """
        if len(recipients) != 0:

            for recipient in recipients:
                yag = yagmail.SMTP('ds1.testing.001@gmail.com')
                yag.send(to=recipient, subject=subject, contents=message)
                print(f"sent email to {recipient}")
                yag.close()
