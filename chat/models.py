from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
import uuid

User = get_user_model()


class Conversation(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, blank=False)
    participant_1 = models.ForeignKey(User, blank=False, related_name='participant_1', on_delete=models.CASCADE)
    participant_2 = models.ForeignKey(User, blank=False, related_name='participant_2', on_delete=models.CASCADE)
    last_interaction = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.participant_1.last_name + " & " + self.participant_2.last_name


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.first_name


class Notification(models.Model):
    sender = models.ForeignKey(User, blank=False, related_name='sender', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, blank=False, related_name='recipient', on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, default=None)


def update_conversation_interaction(conversation):
    conversation.last_interaction = now()
    conversation.save(update_fields=['last_interaction'])


def get_notifications():
    return Notification.objects.all()


def delete_notification(recipient, conversation):
    recipient = User.objects.get(id=recipient.id)
    conversation = Conversation.objects.get(id=conversation.id)
    notifications = Notification.objects.filter(recipient=recipient, conversation=conversation)
    for notification in notifications:
        notification.delete()
    return


def get_last_10_messages(user_id, conversation_uuid):
    user = User.objects.get(id=user_id)
    conversation = Conversation.objects.get(uuid=conversation_uuid)
    participants = [conversation.participant_1, conversation.participant_2]
    if user not in participants:
        return None
    else:
        return Message.objects.filter(conversation=conversation).order_by('-timestamp')[:10][::-1]


def get_all_messages(user_id, conversation_id):
    user = User.objects.get(id=user_id)
    conversation = Conversation.objects.get(id=conversation_id)
    participants = [conversation.participant_1, conversation.participant_2]
    if user not in participants:
        return None
    else:
        return Message.objects.filter(conversation=conversation).order_by('-timestamp')[::-1]