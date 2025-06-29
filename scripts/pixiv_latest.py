import os
import json
from pixivpy3 import AppPixivAPI

USERNAME = os.environ['PIXIV_USERNAME']
PASSWORD = os.environ['PIXIV_PASSWORD']
USER_ID = 94687683  # <-- Replace this with your actual Pixiv user ID

api = AppPixivAPI()
api.login(USERNAME, PASSWORD)

# Get latest public bookmark
json_result = api.user_bookmarks_illust(user_id=USER_ID, restrict='public')

if json_result.illusts:
    latest = json_result.illusts[0]
    output = {
        "title": latest.title,
        "image_url": latest.image_urls.get('large') or latest.image_urls.get('medium'),
        "link": f"https://www.pixiv.net/en/artworks/{latest.id}"
    }

    with open("latest.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
