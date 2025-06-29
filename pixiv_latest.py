# pixiv_latest.py

from pixivpy3 import AppPixivAPI
import json

# Your Pixiv refresh token (get via gppt or other tool)
REFRESH_TOKEN = "YOUR_REFRESH_TOKEN"
USER_ID = "YOUR_USER_ID"  # Replace with your actual Pixiv numeric user ID

# Initialize Pixiv API
api = AppPixivAPI()
api.auth(refresh_token=REFRESH_TOKEN)

# Get latest public bookmark
result = api.user_bookmarks_illust(user_id=USER_ID, restrict="public")
if result.illusts:
    illust = result.illusts[0]
    data = {
        "title": illust.title,
        "artist": illust.user.name,
        "url": f"https://www.pixiv.net/en/artworks/{illust.id}",
        "image": illust.image_urls.medium
    }

    # Save to JSON for web access
    with open("static/latest_pixiv.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
