from playwright.sync_api import Page, Route
import json


def test_api(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = "Яблокофон 17 Про Нах"
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route("**/digital-mat**", handle_route)
    page.goto("https://www.apple.com/shop/buy-iphone")
    page.get_by_role("link", name="All Models").click()
    page.locator(".rf-hcard-img-wrapper").locator("nth=0").click()
    new_title = page.locator("#rf-digitalmat-overlay-label-0").locator("nth=0")
    assert new_title.text_content() == "Яблокофон 17 Про Нах"
