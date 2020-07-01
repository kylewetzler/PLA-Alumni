import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from chat.models import Conversation, Notification, get_notifications, delete_notification


User = get_user_model()


class NotificationConsumer(WebsocketConsumer):

    def new_notification(self, data):
        self.fetch_notifications(data)

    def fetch_notifications(self, data):
        notifications = get_notifications()
        if notifications:
            content = {
                'command': 'notifications',
                'notifications': self.notifications_to_json(notifications),
                'options': '',
            }
            self.send_chat_message(content)

    def delete_notification(self, data):
        recipient = User.objects.get(id=data['recipient_id'])
        conversation = Conversation.objects.get(uuid=data['conversation_id'])
        delete_notification(recipient, conversation)

    def new_message(self, data):
        pass

    def notifications_to_json(self, notifications):
        result = []
        for note in notifications:
            result.append(self.notification_to_json(note))
        return result

    def notification_to_json(self, notification):
        return {
            'sender': notification.sender.id,
            'name': notification.sender.first_name + " " + notification.sender.last_name,
            'recipient': notification.recipient.id,
            'conversation_id': str(notification.conversation.uuid),
        }

    commands = {
        'new_message': new_message,
        'new_notification': new_notification,
        'fetch_notifications': fetch_notifications,
        'delete_notification': delete_notification,
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    async def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps({
            'message': message
        }))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))

