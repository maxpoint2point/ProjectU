from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class UTMConsumer(WebsocketConsumer):
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
        # text_data_json = json.loads(text_data)
        # if text_data_json['type'] == 'Response':
        #     async_to_sync(self.channel_layer.group_send)(
        #         self.client_group_name,
        #         {
        #             'type': 'processing_response',
        #             'data': text_data_json,
        #         }
        #     )
        # if text_data_json['type'] == 'Request':
        #     async_to_sync(self.channel_layer.group_send)(
        #         self.client_group_name,
        #         {
        #             'type': 'processing_request',
        #             'data': text_data_json,
        #         }
        #     )
        print(text_data)
        async_to_sync(self.channel_layer.group_send)(
                self.client_group_name,
                {
                    'type': 'processing_response',
                    'data': text_data,
                }
            )

    def processing_response(self, event):
        self.send(text_data=event["data"])

    def processing_request(self, event):
        print(event)
        if event['data']['payload']['operation'] == 'query_tasks':
            self.send(text_data=json.dumps({'tasks': "tasks"}))
