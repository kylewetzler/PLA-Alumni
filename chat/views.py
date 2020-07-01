from django.shortcuts import render, HttpResponse, redirect
from django.utils.safestring import mark_safe
import json
from .models import Conversation, delete_notification, update_conversation_interaction
from django.contrib.auth import get_user_model

User = get_user_model()


def get_conversations(user):
    return Conversation.objects.filter(participant_1=user).order_by('-last_interaction') | \
           Conversation.objects.filter(participant_2=user).order_by('-last_interaction')


def get_conversation_users():
    return User.objects.filter(is_approved=True).order_by('first_name')


def existing_conversation(user, participant, conversations, errors):
    already_exists = False
    for conv in conversations:
        if participant == conv.participant_1 or participant == conv.participant_2:
            already_exists = True
            errors.append("You already have a conversation with this person")
            return already_exists
    return already_exists


def lobby(request):
    context = {}
    errors = []

    user = request.user
    conversations = (Conversation.objects.filter(participant_1=user) | Conversation.objects.filter(participant_2=user))
    context['conversations'] = conversations
    context['users'] = get_conversation_users()

    if request.POST:
        participant_id = request.POST['participant_id']
        if user.id == int(participant_id):
            errors.append("Hey, I make conversation with myself too, but maybe not online")
        else:
            already_exists = False
            for conv in conversations:
                if int(participant_id) == conv.participant_1.id or int(participant_id) == conv.participant_2.id:
                    already_exists = True
                    errors.append("You already have a conversation with this person")
            if not already_exists:
                new_id = new_conversation(user, participant_id)
                return redirect('room', conversation_uuid=new_id)
    context['errors'] = errors
    context['conversations'] = get_conversations(user)

    return render(request, 'chat/room.html', context)


def room(request, conversation_uuid):
    context = {}
    errors = []

    user = request.user

    context['id'] = str(conversation_uuid)
    context['conversation_id'] = str(mark_safe(json.dumps(conversation_uuid)))

    conversation = Conversation.objects.get(uuid=conversation_uuid)

    update_conversation_interaction(conversation)

    delete_notification(recipient=user, conversation=conversation)

    participants = [conversation.participant_1, conversation.participant_2]
    if user not in participants:
        errors.append("You are not a part of this conversation, ya peeping Tom!")

    else:
        context['users'] = get_conversation_users()

        if user == conversation.participant_1:
            context['recipient'] = conversation.participant_2
        else:
            context['recipient'] = conversation.participant_1

        conversations = Conversation.objects.filter(participant_1=user) | Conversation.objects.filter(participant_2=user)

        if request.POST:
            participant_id = request.POST['participant_id']
            participant = User.objects.get(id=participant_id)
            if user.id == int(participant_id):
                errors.append("Hey, I make conversation with myself too, but maybe not online")
            else:
                if not existing_conversation(user, participant, conversations, errors):
                    new_id = new_conversation(user, participant_id)
                    return redirect('room', conversation_uuid=new_id)
                else:
                    try:
                        existing_convo = Conversation.objects.get(participant_1=user, participant_2=participant)
                    except Conversation.DoesNotExist:
                        existing_convo = Conversation.objects.get(participant_1=participant, participant_2=user)
                    return redirect('room', conversation_uuid=existing_convo.uuid)

    context['errors'] = errors
    context['conversations'] = get_conversations(user)

    return render(request, 'chat/room.html', context)


def start_conversation(request, participant_id):
    user = request.user
    participant = User.objects.get(id=participant_id)
    conversations = get_conversations(user)
    errors = []
    if not existing_conversation(user, participant, conversations, errors):
        new_id = new_conversation(user, participant.id)
        return redirect('room', conversation_uuid=new_id)
    else:
        try:
            existing_convo = Conversation.objects.get(participant_1=user, participant_2=participant)
        except Conversation.DoesNotExist:
            existing_convo = Conversation.objects.get(participant_1=participant, participant_2=user)
        return redirect('room', conversation_uuid=existing_convo.uuid)


def new_conversation(user, participant_id):
    participant = User.objects.get(id=participant_id)
    Conversation.objects.create(participant_1=user, participant_2=participant)
    return Conversation.objects.get(participant_1=user, participant_2=participant).uuid
