
class BillingManager(object):

    def do_billing(self):
        print("Billing completed")


class OrderFullFillmentManager(object):

    def fullfill_order(self):
        print("Order Full filled")


class ShippingManager(object):

    def start_shipping(self):
        print("Shipping Start")


class CustomerService(object):

    def __init__(self, billing_manager, order_fullfilment_manager, shipping_manager):
        self.billing_manager = billing_manager
        self.order_fullfilment_manager = order_fullfilment_manager
        self.shipping_manager = shipping_manager

    def do_billing(self):
        self.billing_manager.do_billing()

    def fullfill_order(self):
        self.order_fullfilment_manager.fullfill_order()

    def start_shipping(self):
        self.shipping_manager.start_shipping()


def main():
    customer_service = CustomerService(BillingManager(),OrderFullFillmentManager(),ShippingManager())

    customer_service.do_billing()
    customer_service.fullfill_order()
    customer_service.start_shipping()


if __name__ == "__main__":
    main()