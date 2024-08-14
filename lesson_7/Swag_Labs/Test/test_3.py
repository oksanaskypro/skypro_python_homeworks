from lesson_7.Swag_Labs.Pages.Shopmain import ShopmainPage
from lesson_7.Swag_Labs.Pages.Shopcontainer import ShopContainer

def test_shop (chrome_browser):
    expected_total = "58.29"

    shopmain = ShopmainPage (chrome_browser)
    shopmain.regisration_fieds()
    shopmain.buy_issue()
    shopmain.click_issue()
    shopmain.info_container()

    container = ShopContainer (chrome_browser)
    container.checkout()
    container.info()
    container.price()
    assert expected_total in container.price()
    print (f"Итоговая сумма равна ${container.price()}")