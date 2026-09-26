from playwright.sync_api import Page, expect

def test_verify_logo(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    expect(page.locator("img[alt='Tricentis Demo Web Shop']")).to_be_visible()

    products = page.locator("h2.product-title>a[href*='computer']")

    products_count = products.count()
    print("Total products:", products_count)

    expect(products).to_have_count(products_count)

    # text.content will return only text of single element
    print("First product:", products.first.text_content())
    print("First product:", products.last.text_content())
    print("First product:", products.nth(2).text_content())

    # to get all the contents from the used locator
    products_titles=products.all_text_contents()
    print("product tiles are:", products_titles)
    for i in products_titles:
        print(i)

    # using starts-with()
    build_product = page.locator("//h2//a[starts-with(@href,'/build')]")
    print("build products:",build_product.count())
    expect(build_product).to_have_count(build_product.count())


    #XPATH with last()
    youtube = page.locator("//div[@class='column follow-us']//li[4]")
    youtube_text=youtube.text_content()
    print(youtube_text)
    expect(youtube).to_have_text(youtube_text)

    last = page.locator("//div[@class='column follow-us']//li[last()]")
    last_text = last.text_content()
    print(last_text)
    expect(last).to_have_text(last_text)


    #CSS tag and attribute value
    register = page.locator("//a[@class='ico-register']")
    expect(register).to_be_visible()
    register.click()
    page.wait_for_timeout(5000)







# h2>a[href*='computer']