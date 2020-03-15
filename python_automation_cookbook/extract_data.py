import delorean
from decimal import Decimal
from parse import parse

class PriceLog(object):
    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price
    
    def __repr__(self):
        return '<PriceLog({}, {}, {}>'.format(self.timestamp, self.product_id, self.price)
    
    @classmethod
    def parse(cls, text_log):
        '''
        Parse from a text log with the format
        [<Timestamp>] - SALE - PRODUCT: <product id> - PRICE: $<price>
        to a PriceLog object
        '''
        def price(string):
            return Decimal(string)
        
        def isodate(string):
            return delorean.parse(string)
        
        FORMAT = ('[{timestamp:isodate}] - SALE - PRODUCT: {product:d} - PRICE: ${price:price}')
        formats = {'price': price, 'isodate': isodate}
        result = parse(FORMAT, text_log, formats)
        return cls(timestamp=result['timestamp'], product_id=result['product'], price=result['price'])

log = '[2018-05-06T14:58:59.051545] - SALE - PRODUCT: 827 - PRICE: $22.25'
print(PriceLog.parse(log))
