from rest_framework import routers
from un.views import *
router = routers.DefaultRouter()

router.register(r'scrolls', ScrollView, basename="scrolls")
router.register(r'products', ProductView, basename="products")
router.register(r'partners', PartnerView, basename="partners")
router.register(r'faqs', FAQView, basename="faqs")
router.register(r'abouts', AboutView, basename="abouts")
router.register(r'blogs', BlogView, basename="blogs")
router.register(r'images', ImageView, basename="images")
