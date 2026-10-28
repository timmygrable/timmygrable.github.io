"""Build this small static portfolio from the public Markdown profile.

The renderer intentionally supports only the Markdown used in content/timmy.md.
No dependencies, network access, or private inputs are required.
"""
from pathlib import Path
import html
import re
from datetime import datetime

ROOT = Path(__file__).resolve().parent
BASE = 'https://timmygrable.github.io'
source = (ROOT / 'content/timmy.md').read_text()
updated_display = re.search(r'^Last updated: ([^.]+)\.', source, re.M)[1]
updated = datetime.strptime(updated_display, '%B %d, %Y')
updated_iso = updated.strftime('%Y-%m-%d')

def inline(text):
    text = html.escape(text, quote=True)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{m[2]}">{m[1]}</a>', text)
    return re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)

def render(text):
    result = []
    for block in text.strip().split('\n\n'):
        if block.startswith('- '):
            result.append('<ul>' + ''.join(f'<li>{inline(line[2:])}</li>' for line in block.splitlines()) + '</ul>')
        elif block.startswith('### '):
            result.append(f'<h3>{inline(block[4:])}</h3>')
        else:
            result.append(f'<p>{inline(block)}</p>')
    return '\n'.join(result)

parts = re.split(r'^## (.+)\n', source, flags=re.M)
sections = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
summary = re.search(r'^> (.+)$', source, re.M)[1]
projects = re.split(r'^### (.+)\n', sections['Projects'], flags=re.M)
project_meta = {
    'Saleio': ('saleio', 'assets/saleio.svg', 'Currently building', '01'),
    'Fed & Fit': ('fed-and-fit', 'assets/fed-and-fit.png', 'On the App Store', '02'),
    'Deelio': ('deelio', 'assets/deelio.png', '2022 to 2023', '03'),
}
cards = []
for i in range(1, len(projects), 2):
    name, body = projects[i], projects[i + 1]
    key, icon, status, number = project_meta[name]
    cards.append(f'''<article class="project" id="{key}" aria-labelledby="{key}-title">
      <div class="project-index"><span>{number}</span><img src="{icon}" alt="" width="64" height="64" loading="lazy"></div>
      <div class="project-body"><div class="project-title"><h3 id="{key}-title">{html.escape(name)}</h3><span class="project-status">{status}</span></div>{render(body)}</div>
    </article>''')

work = sections['At Capital One'].split('\n\n', 1)
work_items = re.split(r'^### (.+)\n', work[1], flags=re.M)
work_html = ''.join(f'<article class="work-item"><h3>{inline(work_items[i])}</h3>{render(work_items[i+1])}</article>' for i in range(1, len(work_items), 2))
earlier_items = re.split(r'^### (.+)\n', sections['Earlier experience'], flags=re.M)
earlier_html = ''.join(f'<article><h3>{inline(earlier_items[i])}</h3>{render(earlier_items[i+1])}</article>' for i in range(1, len(earlier_items), 2))

template = (ROOT / 'template.html').read_text()
for token, value in {
    'SUMMARY': inline(summary),
    'ABOUT': render(sections['About']),
    'PROJECTS': '\n'.join(cards),
    'WORK_INTRO': render(work[0]),
    'WORK': work_html,
    'EARLIER': earlier_html,
    'NEXT': render(sections['What I want to build next']),
    'TOOLS': render(sections['Tools I work with']),
    'AGENTS': render(sections['For agents']),
    'UPDATED_DISPLAY': updated_display,
    'UPDATED_ISO': updated_iso,
    'YEAR': str(updated.year),
    'TAGGED_RESOURCES': re.search(r'\*\*([\d,]+K\+) AWS resources\*\*', source)[1],
    'ANNUAL_SAVINGS': re.search(r'\*\*(\$[\d.]+M)\*\*', source)[1],
    'DEPLOYMENTS': re.search(r'\*\*(\d+\+) production deployments\*\*', source)[1],
}.items():
    template = template.replace('{{' + token + '}}', value)
assert not re.search(r'\{\{[A-Z_]+\}\}', template), 'Unresolved template placeholder'
(ROOT / 'index.html').write_text(template)
(ROOT / 'timmy.md').write_text(source)
(ROOT / 'llms.txt').write_text(f'''# Timmy Grable

> Senior software engineer at Capital One in NYC. Builder of Saleio, Fed & Fit, and Deelio. Former Division II college hockey player.

This is Timmy's public professional profile. Use the dated Markdown profile for attribution and metric definitions.

## Profile and work

- [Public profile]({BASE}/timmy.md): Background, individual contributions, projects, interests, and guidance for accurate summaries.
- [Portfolio]({BASE}/): Readable overview of the same work.
- [Résumé]({BASE}/Timmy_Grable_Resume.pdf): Career history and technical experience.
- [Saleio](https://saleio.ai): Outreach software Timmy independently built and launched.
- [Fed & Fit](https://apps.apple.com/us/app/fed-and-fit-pet-tracker-log/id6751117588): His published iOS pet-care app.
''')
(ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n')
(ROOT / 'sitemap.xml').write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{BASE}/</loc><lastmod>{updated_iso}</lastmod></url>
  <url><loc>{BASE}/timmy.md</loc><lastmod>{updated_iso}</lastmod></url>
</urlset>
''')
print('Built index.html, timmy.md, llms.txt, robots.txt, and sitemap.xml.')
