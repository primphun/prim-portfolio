# prim-portfolio

Prim Phunnapa Supakijsilp's portfolio. A static site with no build step.

- `index.html` is the design portfolio. The Design / Model switch in the top bar also shows the model portfolio.
- `model.html` is the same page opened on the model portfolio, with its own title and share preview. Send this link to agencies and brands.
- **After any change to `index.html`, run `python3 tools/build-model-page.py` and commit `model.html` too.** It is generated from `index.html`.
- Once the site has its final address, change the `og:image` lines in both pages (and the script) to the full address, for example `https://example.com/images/og.jpg`, so link previews show the picture.
