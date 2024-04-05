# import requests
# res=requests.get("https://www.ebay.com/itm/355344090794?_trkparms=amclksrc%3DITM%26aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D262136%26meid%3Dd4ea8949208e49f6b8784fd7d90fd3dc%26pid%3D101506%26rk%3D1%26rkt%3D10%26sd%3D325880951172%26itm%3D355344090794%26pmt%3D1%26noa%3D1%26pg%3D4247815%26algv%3DDefaultOrganicWebWithV11WebTrimmedV3VisualRankerWithKnnV3AndUltBRecall%26brand%3DNew%2BBalance&_trksid=p4247815.c101506.m1851").text
# # print(res)
#
#
# res=res.split('<div class=fdbk-container__details__comment>')
#
# print(len(res))
#
# for i in range(1,len(res)):
#     txt=res[i].split('<span>')[1].split('</span>')
#     print(txt[0])




# import requests
# res=requests.get("https://www.nykaafashion.com/adidas-vs-pace-2-0-men-green-skateboarding-shoes/p/12662106?designCode=ADIDA00061984").text
# print(res)


# import requests
# from bs4 import BeautifulSoup
#
#
# def scrape_amazon_reviews(product_url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
#     response = requests.get(product_url, headers=headers)
#     print(response.text)
#     # soup = BeautifulSoup(response.text, 'html.parser')
#     #
#     # reviews = []
#     # for review in soup.find_all('div', {'data-hook': 'review'}):
#     #     review_text = review.find('span', {'data-hook': 'review-body'}).text.strip()
#     #     reviews.append(review_text)
#     #
#     # return reviews
#
#
# def main():
#     amazon_url = "https://www.flipkart.com/apple-iphone-15-blue-128-gb/product-reviews/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOBGTAGPAQNVFZZYO7HQ2L&marketplace=FLIPKART&page=2"
#
#     amazon_reviews = scrape_amazon_reviews(amazon_url)
#     print("\nAmazon Reviews:")
#     for review in amazon_reviews:
#         print(review)
#
#
# if __name__ == "__main__":
#     main()


# import requests
# from bs4 import BeautifulSoup
#
#
# def scrape_flipkart_reviews(product_url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
#
#     reviews = []
#     response = requests.get(product_url, headers=headers)
#     print(response.text)
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     review_containers = soup.find_all('div', class_='_27M-vq')
#     for review in review_containers:
#         review_text = review.find('div', class_='t-ZTKy').text.strip()
#         reviews.append(review_text)
#
#     return reviews
#
#
# def main():
#     flipkart_url = "https://www.flipkart.com/apple-iphone-15-blue-128-gb/product-reviews/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOBGTAGPAQNVFZZYO7HQ2L&marketplace=FLIPKART&page=2"
#
#     flipkart_reviews = scrape_flipkart_reviews(flipkart_url)
#     print("\nFlipkart Reviews:")
#     for idx, review in enumerate(flipkart_reviews, start=1):
#         print(f"Review {idx}: {review}")
#         print()
#
#
# if __name__ == "__main__":
#     main()
#


# import requests
#
# def save_html_page(url, filename):
#     response = requests.get(url)
#     if response.status_code == 200:
#         with open(filename, 'w', encoding='utf-8') as file:
#             file.write(response.text)
#         print(f"Page saved successfully as '{filename}'")
#     else:
#         print(f"Failed to fetch page. Status code: {response.status_code}")
#
# def main():
#     url = "https://www.flipkart.com/apple-iphone-15-blue-128-gb/product-reviews/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOBGTAGPAQNVFZZYO7HQ2L&marketplace=FLIPKART"  # Replace this with the URL you want to save
#     filename = "example.html"  # Choose the filename you want to save the HTML as
#     save_html_page(url, filename)
#
# if __name__ == "__main__":
#     main()

#
import requests
from bs4 import BeautifulSoup
from apkupload import sent
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def scrape_amazon_reviews(product_url, num_reviews=20):
    pro = []
    page_number = 1

    while len(pro) < num_reviews:
        url = f"{product_url}&pageNumber={page_number}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # review_containers = soup.find_all('div', class_='a-section review aok-relative')
        product_con = soup.find('span', class_='a-size-large product-title-word-break')
        print(product_con,"hhhhhhhhhhhhhhhh")
        print(product_con,"hhhhhhhhhhhhhhhh")
        print(product_con,"hhhhhhhhhhhhhhhh")
        if not product_con:
            break
        review_text = product_con.text

        # Get the text inside the span element
        # text_inside_span = review_text.text

        # review_text = product_con[0].find('span', class_='a-size-large product-title-word-break').text.strip()
        print(review_text,"-------------------------------------------")
        # for review in product_con:
        #     review_text = review.find('span', class_='a-size-large product-title-word-break').text.strip()
        #     pro.append(review_text)
        #
        #     if len(pro) >= num_reviews:
        #         break

        page_number += 1

    return pro


def main():
    amazon_url = "https://www.amazon.com/Apple-iPhone-13-Pro-Sierra/dp/B09LPB9SQH/ref=sr_1_3?crid=2555X7AEBS65C&dib=eyJ2IjoiMSJ9._mV3wgG2FFjltXE6Se_0wnuXYv1WKPavBiU75wg2uITc-5W_zduVVt8qxYD9n6EZb1h8yyQytWYDMB9R6kYmvwQkYnaFIqEXiJOlbtqoufw3Scf2SrGn6IOz04GJLexiV6flyepQ7o-uPJUKKiZ6mcYsU9MTFqcpR7PHWNspr1cy5Uxsez-7r1ghyBcdB-KTYIC5ghLflI3VCJQi5IEytI-m6byBdAce7iJr5pzwkNE.QKQQuizwF7ywMcTkI9xLvAWSrKgo1lyb_PJqNwHwryk&dib_tag=se&keywords=iphone&qid=1712045872&sprefix=ipho%2Caps%2C1085&sr=8-3"
    x = []
    y = []
    z = []
    amazon_reviews = scrape_amazon_reviews(amazon_url, num_reviews=20)

    print("\nAmazon Reviews:")
    for idx, review in enumerate(amazon_reviews, start=1):
        review = review.replace('Read more', "")
        print(f"Review {idx}: {review}")

        res = sent(review)
        x.append(idx)
        y.append(float(res[0]))
        z.append(float(res[1]))
        requests.get(
            "http://127.0.0.1:8000/insert_review?p=gshock&r=" + review + "&po=" + res[0] + "&ne=" + res[1] + "&nu=" +
            res[2])

    # Bar plot showing positive vs negative sentiment
    plt.figure(figsize=(8, 6))
    plt.bar(['Positive', 'Negative'], [sum(y), sum(z)], color=['green', 'red'])
    plt.title('Positive vs Negative Sentiment')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

    # Scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color='green', label='Positive')
    plt.scatter(x, z, color='red', label='Negative')
    plt.title('Sentiment Analysis')
    plt.xlabel('Review Index')
    plt.ylabel('Sentiment Score')
    plt.legend()
    plt.show()

    # Word cloud
    text = ' '.join(amazon_reviews)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud of Amazon Reviews')
    plt.show()


if __name__ == "__main__":
    main()


