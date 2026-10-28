# Timmy Grable's portfolio

Public portfolio at https://timmygrable.github.io/.

The site is static HTML and CSS, with no client-side JavaScript, third-party analytics, or runtime dependencies. GitHub Pages publishes the root of the `main` branch.

## Update the profile

Edit `content/timmy.md`, then run:

```sh
python3 build.py
```

This generates both the page content and the public `timmy.md` from the same Markdown source. It also writes `llms.txt`, `robots.txt`, and `sitemap.xml`. The renderer supports the small Markdown subset used in this profile: headings, paragraphs, lists, links, and bold text.

Update the date in `content/timmy.md` when reviewing its facts. The build uses that date in the page, structured data, and sitemap. Dates should reflect a content review, not merely a deployment.

Edit `template.html` or `style.css` for layout changes. Replace `Timmy_Grable_Resume.pdf` to update the résumé.

## Preview

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765. Check the desktop and mobile layouts, document links, and project links before committing the generated files.

## Publishing

Commit the source and generated files to `main`. GitHub Pages is configured to publish from `/`. `.nojekyll` keeps the files static, including the raw Markdown profile. No automatic content negotiation is required: the HTML page links directly to `timmy.md` and advertises it with `rel="alternate"`.

Only material intended for public display belongs in this repository. Keep private notes and source code from other projects elsewhere.

The public-profile approach was inspired by [Lauren Lee's profile](https://lauren.md/index.md). This site's content and implementation are Timmy's own.
