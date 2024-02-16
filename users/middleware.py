from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
import logging


class UserLogs(MiddlewareMixin):
    def process_request(self, request):
        if None != request.user.id:
            logger = logging.getLogger(__name__)
            logger.debug(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} | {request.user.username} | URL={request.path}")
