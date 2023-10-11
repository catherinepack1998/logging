import logging
from django.http import JsonResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def main(request):
    logger.debug('Лог дебага')
    logger.info('Лог информации')
    logger.warning('Лог предупреждения')
    logger.error('Лог ошибки')
    logger.critical('Лог критической ошибки')
    return JsonResponse({"success": True})