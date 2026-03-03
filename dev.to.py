import requests
import os
from dotenv import load_dotenv

load_dotenv()
DEV_TO_API_KEY = os.environ.get("DEV_TO_API_KEY")

if not DEV_TO_API_KEY:
    DEV_TO_API_KEY = input("Enter your Dev.to API key: ").strip()

response = requests.get('https://dev.to/api/articles/me/all',
                        headers={'api-key': DEV_TO_API_KEY})

response.raise_for_status()

articles = response.json()
print(str(len(articles)) + ' articles found')

os.makedirs('posts', exist_ok=True)

for post in articles:
    date_str = post.get('published_at') or post.get('created_at') or post.get('edited_at', 'unknown')
    parsed_date = date_str.split('T')[0]

    # name markdown files with the following convention:
    # 2020-08-20-creating-a-portfolio-site-using-gatsby-trello.md
    filename = parsed_date + "-" + post['slug']

    print('Creating file: ' + filename)

    file = open('posts/' + filename + '.md', "w", encoding="utf-8")
    file.write(post['body_markdown'])
    file.close()

print('Complete!')