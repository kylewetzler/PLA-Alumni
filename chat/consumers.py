import json
from channels.generic.websocket import WebsocketConsumer
from .models import Conversation, Message, get_last_10_messages, get_all_messages, Notification, \
    update_conversation_interaction
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync

from .models import Message

User = get_user_model()


class ChatConsumer(WebsocketConsumer):

    def fetch_all_messages(self, data):
        messages = get_all_messages(data['user_id'], data['conversation_id'])
        if messages:
            content = {
                'command': 'messages',
                'messages': self.messages_to_json(messages),
                'options': '',
            }
            self.send_message(content)

    def fetch_messages(self, data):
        messages = get_last_10_messages(data['user_id'], data['conversation_id'])
        if messages:
            options = ""
            if len(messages) < 10:
                options = "less_than_10"
            content = {
                'command': 'messages',
                'messages': self.messages_to_json(messages),
                'options': options,
            }
            self.send_message(content)
        else:
            content = {
                'command': 'no_messages',
            }
            self.send_message(content)

    def new_message(self, data):
        conversation_id = data['conversation_id']

        conversation = Conversation.objects.get(uuid=conversation_id)
        update_conversation_interaction(conversation)

        author = data['from']
        author_user = User.objects.get(id=author)

        if author_user == conversation.participant_1:
            recipient = conversation.participant_2
        else:
            recipient = conversation.participant_1

        message = Message.objects.create(
            conversation=conversation,
            author=author_user,
            content=data['message']
        )
        if not Notification.objects.filter(sender=author_user, recipient=recipient, conversation=conversation):
            notification = Notification.objects.create(
                sender=author_user,
                recipient=recipient,
                conversation=conversation
            )

            notification_content = {
                'command': 'new_notification',
                'notification': self.notification_to_json(notification)
            }
            self.send_chat_message(notification_content)

        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def notification_to_json(self, notification):
        return {
            'sender': notification.sender.id,
            'recipient': notification.recipient.id,
            'conversation_id': str(notification.conversation.uuid)
        }

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):

        '''.strftime("%b %d, %-I:%M %p")'''

        return {
            'author': message.author.id,
            'content': message.content,
            'timestamp': str(message.timestamp).replace(" ", "T")
        }

    commands = {
        'fetch_all_messages': fetch_all_messages,
        'fetch_messages': fetch_messages,
        'new_message': new_message
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

