from django.contrib.sitemaps import Sitemap
from .models.shop import Shop


class ShopSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Shop.objects.all()





