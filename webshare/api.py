import httpx
from async_web_scrapper.proxy.proxy_types import HTTPProxy


class WebShareAPI:
    def __init__(self, api_key):
        self.api_key = api_key
    
    def _auth_headers(self):
        return {
            'Authorization': f'Token {self.api_key.token}'
        }
    
    async def list_proxies(self):
        res = []
        endpoint_url = 'https://proxy.webshare.io/api/proxy/list/'
        
        while True:
            async with httpx.AsyncClient(headers=self._auth_headers()) as client:
                r = await client.get(endpoint_url)
            
            r.raise_for_status()
            resp_obj = r.json()

            for raw_proxy in resp_obj['results']:
                proxy = HTTPProxy(
                    raw_proxy['proxy_address'], # ip
                    raw_proxy['ports']['http'], # port
                    username=raw_proxy['username'],
                    password=raw_proxy['password'],
                )
                res.append(proxy)

            if not resp_obj['next']:
                break
            endpoint_url = resp_obj['next']

        return res
