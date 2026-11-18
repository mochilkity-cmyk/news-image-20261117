# news-image-20261117 — build log

## Stories chosen (Tuesday 17 November 2026)

All verified from multiple independent reports (search, 18 Nov 2026):

1. **US strikes Iran as Hormuz war grows** (Middle East) — US warplanes hit
   a missile site on Qeshm Island; a fourth tanker was mined in the Strait
   of Hormuz. Sources: Reuters (via Profile News), AFP (via Pakistan TV
   live blog).
2. **Ukraine strikes Crimean Bridge** (Europe) — Kyiv struck the Crimean
   Bridge; Russian strikes hit Kyiv bridges and Zaporizhzhia, killing 40.
   Sources: AP/Al Jazeera (via news roundups), Profile News, Standard Topic.
3. **Four nations demand Gaza aid access** (Middle East) — UK, Australia,
   Canada and Italy urged Israel to open crossings as winter rains flood
   shelters. Sources: asaspress digest, The Paris Eye, Dawn roundup.
4. **Trump, Xi, Putin to meet in Shenzhen** (Asia-Pacific) — the three
   leaders will hold a first-ever trilateral summit on Thursday, on the
   APEC sidelines. Sources: LinkedIn Daily Buzz, Standard Topic, AFP/Dawn.
5. **US tightens AI chip export ban on China** (Technology) — new rules
   close loopholes letting Chinese firms reach advanced AI chips via
   overseas data centres. Sources: LinkedIn Daily Buzz, Standard Topic.
6. **US loses measles elimination status** (Health) — PAHO: the US lost
   the status after a year of uninterrupted measles transmission.
   Sources: Profile News, PAHO via ABC World News Tonight.

Left out for space (real, but lower priority): France's 17 Nov wage
protests (146,000 per the Interior Ministry), Japan scrambling jets after
a Russian airspace violation, the COP31 draft deal ($120bn climate
finance), Wall Street falling on AI/tech stocks.

## How the image was made

`render.py` (in this repo) draws a 1024×1024 infographic with Python PIL
and DejaVu Sans: a navy header with the date in 56pt bold, six cards
(2 cols × 3 rows) each with a region kicker, a bold headline (≤2 lines)
and a 2–3 line detail, and a footer naming the sources. No starter image
was copied — the kit starter's entry.png is a 512×512 pixel-art globe and
was not used. The final image was viewed and checked: no overlaps, no
garbled text; one headline was shortened during layout ("Hormuz tanker
war" → "Hormuz war") so it fits two lines.

## Validation

- `main.ts` run twice (MAKEFUN_OUTPUT_DIR=/tmp/ni17-a and /tmp/ni17-b):
  byte-identical outputs, both equal to entry.png — DETERMINISM PASS.
- Image: 1024×1024, 120,964 bytes — within the 1 MiB and 1024×1024 caps.
- Kit check: see below (expect only transcripts_present to fail — no
  bundle yet; the parent handles bundling).

## Caveats

- The news picture comes from secondary roundups and digests (asaspress,
  Profile News, LinkedIn Daily Buzz, Standard Topic, Pakistan TV, Le
  Monde) rather than first-hand wire copy; each story was corroborated
  across at least two independent results, but casualty figures (e.g. 40
  killed in Zaporizhzhia) are as reported on the day and may be revised.
- The "fourth tanker mined" and "Qeshm strike" are reported by Reuters/AFP
  via those roundups; the image states them as reported, without hype.
- No local judge grade exists for this bounty — the server grades every
  entry, so no rank is promised.
