import os
import json
from pixivpy3 import AppPixivAPI

USERNAME = os.environ['PIXIV_USERNAME']
PASSWORD = os.environ['PIXIV_PASSWORD']

api = AppPixivAPI()
api.login(USERNAME, PASSWORD)

# get latest bookmark
json_result = api.user_bookmarks_illust(user_id=YOUR_USER_ID, restrict='public')

# Save latest post
if json_result.illusts:
    latest = json_result.illusts[0]
    output = {
        "title": latest.title,
        "image_url": latest.image_urls.large,
        "link": f"https://www.pixiv.net/en/artworks/{latest.id}"
    }

    with open("latest.json", "w") as f:
        json.dump(output, f)
