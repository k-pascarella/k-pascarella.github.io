# Personal website — Quarto source

A four-page Quarto site: Home, Research, Projects, CV. Free to host on GitHub Pages.

## Before you publish: things to replace

1. **`files/Pascarella-CV.pdf`** — currently a placeholder. Drop in your real CV, keep
   the filename.
2. **`files/JSM2026-poster.pdf`** — currently a placeholder. Drop in your real poster,
   keep the filename.
3. **`index.qmd`** — the GitHub link currently points at
   `https://github.com/YOUR-USERNAME`, which is why it 404s. Either replace
   `YOUR-USERNAME` with your actual GitHub username, or delete
   `[GitHub](https://github.com/YOUR-USERNAME)` from the `.linkrow` block until you
   have repositories worth linking to. A 404 looks worse than no link.
4. **`_quarto.yml`** — nothing required, but you can adjust the site description.

Your phone number and street address appear nowhere in the site. Email is assembled by
a small script at page load rather than sitting in the HTML as plain text, which stops
most casual scrapers. It falls back to `kaylee.pascarella [at] hotmail [dot] com` if
scripting is off.

## Preview locally

Install Quarto from <https://quarto.org/docs/get-started/>, then from this folder:

```
quarto preview
```

That opens the site in a browser and reloads as you edit. To build the final files:

```
quarto render
```

Output lands in `docs/`.

## Publish free on GitHub Pages

1. Create a new **public** repository on GitHub. Naming it `yourusername.github.io`
   gives you `https://yourusername.github.io`. Any other name gives you
   `https://yourusername.github.io/reponame`.
2. Push this whole folder, including the rendered `docs/` directory.
3. On GitHub: **Settings → Pages**. Under "Build and deployment", set Source to
   *Deploy from a branch*, branch `main`, folder `/docs`. Save.
4. Wait a minute or two, then load the URL.

After any edit, run `quarto render` and push again. The `.nojekyll` file is there so
GitHub serves the files as-is; leave it alone.

A custom domain is optional and costs roughly $12–15/year. The `github.io` address is
fine to start and can be pointed at a domain later without rebuilding anything.

## Structure

```
_quarto.yml     site config and navigation
styles.scss     theme: palette, type, the threshold-rule divider
index.qmd       home
research.qmd    dissertation walkthrough, publications
projects.qmd    lead service lines, water treatment fault detection
cv.qmd          CV embed and summary
images/         figures
files/          CV and poster PDFs
docs/           rendered output — do not edit by hand
```

## Design notes

Body text is Public Sans, headings are Newsreader, labels and captions are IBM Plex
Mono. The palette is ink `#16232E`, petrol `#1F6F73`, slate `#5A6B75`, mist `#E8EDEE`,
paper `#FBFCFC`, with amber `#C98A1B` reserved for one thing only: the tick on the
section dividers. Those dividers are meant to read as a threshold marked on the axis of
a distribution, which is the thing the dissertation is actually about. If you add
sections, keep the amber for that and nothing else.

Add a divider with:

```
::: {.threshold data-label="Your label"}
:::
```

### The background

`_background.html` is a generated SVG layer of scattered pastel squares, sitting behind
a near-opaque white reading panel so text stays crisp. To re-roll the arrangement, edit
`SEED` (or `N_SQUARES`, or the `palette` list) in `tools/make_background.py`, then:

```
python3 tools/make_background.py
quarto render
```

The squares thin out behind the middle column on purpose, so they never crowd the text.
On narrow screens the whole layer drops to 55% opacity.

### Reusable content blocks

A definition grid (used at the top of the Research page):

```
<div class="defgrid">
  <div><div class="term">Your term</div><p>Definition.</p></div>
  <div><div class="term">Another</div><p>Definition.</p></div>
</div>
```

A comparison table (used for the two estimators). Give each `<td>` a `data-col`
attribute — it becomes the column label when the table stacks on mobile:

```
<table class="compare">
  <thead><tr><th></th><th>Option A</th><th>Option B</th></tr></thead>
  <tbody>
    <tr><th>Row label</th>
        <td data-col="Option A">...</td>
        <td data-col="Option B">...</td></tr>
  </tbody>
</table>
```

Both go inside a ```` ```{=html} ```` block in a `.qmd` file.
