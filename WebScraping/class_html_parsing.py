
import re

from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''

class ParsedItemLocators:

    """
    Locators for an item in the HTML page
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'

class ParsedItems:

    """"
    A class to take in an HTML Page (or part of it) and find properties
    """
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator2 = ParsedItemLocators.LINK_LOCATOR
        item_link2 = self.soup.select_one(locator2)
        item_name2 = item_link2.attrs['href']
        return item_name2

    @property
    def price(self):
        locator3 = ParsedItemLocators.PRICE_LOCATOR
        item_price = self.soup.select_one(locator3).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1)) # 51.77

    @property
    def rating(self):
        locator4 = ParsedItemLocators.RATING_LOCATOR
        star_item_rating = self.soup.select_one(locator4)
        classes = star_item_rating.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        return rating_classes[0]

item = ParsedItems(ITEM_HTML)
print(item.name)





