from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.client = self.scope['url_route']['kwargs']['client']
        self.client_group_name = 'chat_%s' % self.client

        async_to_sync(self.channel_layer.group_add)(
            self.client_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.client_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['type'] == 'Response':
            async_to_sync(self.channel_layer.group_send)(
                self.client_group_name,
                {
                    'type': 'processing_response',
                    'payload': text_data_json['payload'],
                }
            )
        if text_data_json['type'] == 'Request':
            async_to_sync(self.channel_layer.group_send)(
                self.client_group_name,
                {
                    'type': 'processing_request',
                    'payload': text_data_json['payload'],
                }
            )

    def processing_response(self, event):
        print(event)

    def processing_request(self, event):
        print(event)





        # self.send(text_data=json.dumps({
        # #     'event': "Send",
        # #     'message': message,
        # #     'username': username
        # # })
        #     print(event)
        # })
