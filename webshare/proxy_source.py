import logging
from .api import WebShareAPI
from async_web_scrapper.proxy import ProxySource


class WebShareSource(ProxySource):
    def __init__(self, api_key):
        self.proxies_set = set()
        self.api_key = api_key

    async def update_list(self):
        api = WebShareAPI(self.api_key)
        # logging.info()
        res = await api.list_proxies()
        for proxy in res:
            self.proxies_set.add(proxy)

    async def get_proxies(self):
        await self.update_list()
        return list(self.proxies_set)
