import  requests
from bs4 import BeautifulSoup
class WebScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve data from {self.url}")
            return None

    def parse(self, html):
        # Placeholder for parsing logic
        soup = BeautifulSoup(html, 'html.parser')
        
        html_body = soup.body

        news_div =  html_body.find('div', {'class':'full-samachar-list'})
        news = []
        for i in news_div.find_all('div', {'class': 'items' }):
            image = i.find('img')['data-src']
            title = i.find('h2').find('a').text.strip()
            
            # print("Title:", title)
            # print("Image URL:", image)

            print("-"*50)
            news.append({
                'title': title,
                'image': image
            })

        return news

# target_url = 'https://www.sidhakura.com/sidhakura-special?page='
target_url = 'https://www.sidhakura.com/society?page='

total_pages = 24
current_page = 1

all_news= []
while current_page <= total_pages:
    url = f"{target_url}{current_page}"
 
    instance = WebScraper(url)
    data = instance.scrape()
    print("Pulled data from page:", current_page, "\n")

    news = instance.parse(data)
    
    all_news.extend(news)

    current_page += 1


import tabulate
print(tabulate.tabulate(all_news, headers="keys", tablefmt="grid"))