import urllib.request
import json
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    "https://houseofmassagechairs.com/products/svago-zgr-zero-gravity-recliner.json",
    "https://houseofmassagechairs.com/products/ogawa-active-xl-3d-massage-chair.json",
    "https://houseofmassagechairs.com/products/infinity-smart-chair-x3-4d-massage-chair.json",
    "https://houseofmassagechairs.com/products/cozzia-qi-xe-pro-duo-massage-chair.json"
]

os.makedirs("assets/real", exist_ok=True)

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        response = urllib.request.urlopen(req, context=ctx)
        data = json.loads(response.read())
        product = data.get('product', {})
        images = product.get('images', [])
        if images:
            img_url = images[0].get('src')
            if img_url:
                filename = url.split('/')[-1].replace('.json', '.jpg')
                urllib.request.urlretrieve(img_url, f"assets/real/{filename}")
                print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed {url}: {e}")
