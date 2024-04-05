import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from apkupload import sent
from wordcloud import WordCloud


def scrape_amazon_reviews(product_url, num_reviews=20):
    reviews = []
    page_number = 1

    while len(reviews) < num_reviews:
        url = f"{product_url}&pageNumber={page_number}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        review_containers = soup.find_all('div', class_='a-section review aok-relative')
        if not review_containers:
            break

        for review in review_containers:
            review_text = review.find('span', class_='review-text').text.strip()
            reviews.append(review_text)

            if len(reviews) >= num_reviews:
                break

        page_number += 1

    return reviews


def main():
    amazon_url = "https://www.amazon.com/Casio-Shock-Quartz-Resin-Casual/dp/B073ZJVXMS/ref=sr_1_8?crid=33ZATLP40G9XD&dib=eyJ2IjoiMSJ9.FEFIrYi_6t6hbmiS2bJ-wAJljodaQfmJQBr-SzOtDFFhUfMc8LayaLmxAnZCxudy-9E8ECobDrLtfxQTkDBMeipLMgkGFstIc5QWjV2zxxyWoRuRYrb3aUwp8hm-KxYx077qJsj4oRIDBMkqPZzb2DLp9h2mQeA0knMlwN-FYwpStYTTXZRGkkbjXdxJ1fc7N4AA3WYnn0uHPPhv7R_ZEhzmtH2GVE2mEzavJ7c62v8ehtuHetnrMa2NTt3jnuvjpya6JvnDXSFqRNHLyjybR1CWpKQKxqLzte_PQvSpphQ.QiEN6KA1zyWXxhJ-vDecHN_E6fj_Ylu7XY4wpybO0QI&dib_tag=se&keywords=gshock&qid=1711992480&sprefix=gshock%2Caps%2C532&sr=8-8&th=1"
    x = []
    y = []
    z = []
    amazon_reviews = scrape_amazon_reviews(amazon_url, num_reviews=10)
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

    # Plotting sentiment analysis results
    plt.bar(x, y, color='green', label='Positive')
    plt.bar(x, z, color='red', label='Negative')
    plt.xlabel('Review Index')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Analysis of Amazon Reviews')
    plt.legend()
    plt.show()

    # Generate word cloud
    text = ' '.join(amazon_reviews)
    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=None,
                          min_font_size=10).generate(text)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

    # Display most positive and negative comments
    sorted_reviews = sorted(zip(amazon_reviews, y), key=lambda x: x[1], reverse=True)
    print("\nMost Positive Comment:")
    print(sorted_reviews[0][0])
    print("\nMost Negative Comment:")
    print(sorted_reviews[-1][0])


if __name__ == "__main__":
    main()


