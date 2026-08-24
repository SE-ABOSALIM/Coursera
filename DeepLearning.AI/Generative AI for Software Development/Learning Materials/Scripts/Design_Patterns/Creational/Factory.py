from abc import ABC, abstractmethod


# 1. Product
class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


# 2. Concrete Products
class EmailNotification(Notification):

    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"SMS sent: {message}")


class PushNotification(Notification):

    def send(self, message):
        print(f"Push notification sent: {message}")


# 3. Factory
class NotificationFactory:

    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()

        elif notification_type == "sms":
            return SMSNotification()

        elif notification_type == "push":
            return PushNotification()

        else:
            raise ValueError("Invalid notification type!")


# 4. Usage
notification = NotificationFactory.create_notification("email")
notification.send("Hello, welcome!")

notification = NotificationFactory.create_notification("sms")
notification.send("Your verification code is: 1234")

notification = NotificationFactory.create_notification("push")
notification.send("You have a new message!")