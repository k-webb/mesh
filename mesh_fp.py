import requests, json, ssl, re

requests.packages.urllib3.disable_warnings()

class footpatrol(object):
    def __init__(self):
        self.s = requests.Session()
        self.cart_id = 'CART ID HERE'

    def add(self,sku):
        print ('adding %s'%sku)
        self.headers = {
            'Host': 'commerce.mesh.mx',
            'Content-Type': 'application/json',
            'X-API-Key': '5F9D749B65CD44479C1BA2AA21991925',
            'Accept': '*/*',
            'X-Debug': '1',
            'Accept-Language': 'en-us',
            'User-Agent': 'FootPatrol/2.0 CFNetwork/811.5.4 Darwin/16.6.0',
            'MESH-Commerce-Channel': 'iphone-app',
        }

        data = '{"quantity":1}'

        add = self.s.put('https://commerce.mesh.mx/stores/footpatrol/carts/%s/%s'%(self.cart_id,sku),verify=False, headers=self.headers, data=data)
        if 200 <= add.status_code < 400:
            print ('Added to your Iphone cart %s'%sku)
            return True
        else:
            print (add.text)

    def view_cart(self,cart_id):
        page = self.s.get('https://commerce.mesh.mx/stores/footpatrol/carts/%s'%self.cart_id, headers=self.headers)
        jsontxt = json.loads(page.text)
        print ('Items in your Cart\n\n')
        for info in jsontxt[u'products']:
            sku = info[u'SKU']
            name = info[u'name']
            qty = info[u'totalQuantity']
            message = 'SKU: %s\nItem Name: %s\nTotal Products: %s\n'%(sku,name,qty)
            print (message)

def main():
    fp = footpatrol()
    fp.add(input("PLEASE ENTER PID "))
    fp.view_cart(fp.cart_id)

if __name__ == '__main__':
    main()
