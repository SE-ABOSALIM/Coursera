from abc import ABC, abstractmethod


# 1. Product
class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


# 2. Concrete Products
class EmailNotification(Notification):

    def send(self, message):
        print(f"Email gönderildi: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"SMS gönderildi: {message}")


class PushNotification(Notification):

    def send(self, message):
        print(f"Push bildirimi gönderildi: {message}")


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
            raise ValueError("Geçersiz bildirim türü!")


# 4. Kullanım
notification = NotificationFactory.create_notification("email")
notification.send("Merhaba, hoş geldin!")

notification = NotificationFactory.create_notification("sms")
notification.send("Doğrulama kodunuz: 1234")

notification = NotificationFactory.create_notification("push")
notification.send("Yeni bir mesajınız var!")