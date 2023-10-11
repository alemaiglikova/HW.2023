from django.contrib.messages import get_messages
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Message

class ChatTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')

    def test_chat_room_view(self):
        self.client.login(username='user1', password='password123')
        response = self.client.get(reverse('chat_room', args=[self.user2.username]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/chat_room.html')

    def test_send_message_view(self):
        self.client.login(username='user1', password='password123')
        response = self.client.post(reverse('send_message', args=[self.user2.username]), {'content': 'Hello!'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})

    def test_message_model(self):
        message = Message.objects.create(sender=self.user1, receiver=self.user2, content='Hello!')
        self.assertEqual(message.sender, self.user1)
        self.assertEqual(message.receiver, self.user2)
        self.assertEqual(message.content, 'Hello!')

class NotificationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='password123')

    def test_send_notification(self):
        self.client.login(username='user1', password='password123')
        response = self.client.get(reverse('some_view_that_generates_notification'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Notification message text')

    def test_notification_template(self):
        self.client.login(username='user1', password='password123')
        response = self.client.get(reverse('some_view_that_generates_notification'))
        self.assertContains(response, 'Notification message text')