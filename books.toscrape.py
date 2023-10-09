from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv

url = 'https://books.toscrape.com/'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    driver.get(url)
    driver.maximize_window()

    categories = driver.find_elements('xpath','//div[@class="side_categories"]//li/ul/li/a')
    category_links = [category.get_attribute('href') for category in categories]

    url = 'https://en.wikipedia.org/wiki/Royal_Netherlands_Navy'
    driver.find_element('xpath','//input[@id="p-lang-btn-checkbox"]'

    with open('books_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Availability', 'Category'])

        for link in category_links:
            driver.get(link)
            category = driver.find_element('xpath','//div[@class="page-header action"]/h1').text

            while True:
                books = driver.find_elements('xpath','//article[@class="product_pod"]')
                for book in books:
                    print(book)
                    title = book.find_element('xpath','.//h3/a').get_attribute('title')
                    price = book.find_element('xpath','.//div[@class="product_price"]/p[@class="price_color"]').text
                    availability = book.find_element('xpath','.//div[@class="product_price"]/p[@class="instock availability"]').text
                    print([title, price, availability, category])
                    writer.writerow([title, price, availability, category])

                next_button = driver.find_elements('xpath','//a[normalize-space()="next"]')
                if not next_button:
                    break  
                next_button[0].click()

    print("Дані успішно збережені в 'books_data.csv'")
except Exception as e:
    print(f"Помилка: {e}")

finally:
    driver.quit()
    print("Chrome успішно закрито")


