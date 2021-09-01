""" Approval Request State Transition """

import logging

from django.utils.translation import gettext_lazy as _
from main.catalog.models import (
    ApprovalRequest,
    Order,
    OrderItem,
    ProgressMessage,
)
from main.catalog.services.start_order_item import StartOrderItem

logger = logging.getLogger("catalog")


class StartOrder:
    """Start the order"""

    def __init__(self, order):
        self.order = order

    def process(self):
        logger.info("Submitting Order for provisioning...")
        self.order.mark_ordered("Submitting Order for provisioning")

        StartOrderItem(self.order).process()
        return self
