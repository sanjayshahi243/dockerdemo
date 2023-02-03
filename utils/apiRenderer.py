from rest_framework.renderers import BaseRenderer
from rest_framework.utils import json


class ApiRenderer(BaseRenderer):
    media_type = 'application/json'
    format = 'json'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_dict = {
            'status': 'failure',
            'data': {},
            'message': '',
        }
        if renderer_context['response'].data:
            response_dict['data'] = renderer_context['response'].data
        if renderer_context['response'].status_code:
            response_dict['status'] = renderer_context['response'].status_code
        if 'message' in renderer_context['response']:
            response_dict['message'] = renderer_context['response'].message
        data = response_dict
        return json.dumps(data)
