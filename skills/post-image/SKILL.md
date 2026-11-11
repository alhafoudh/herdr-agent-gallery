---
name: post-image
description: Show an image to the user by posting it to the Images panel of the herdr app. Use when the user says "show me", "let me see it", "post it", "show me the screenshots/images/chart", or otherwise wants to see an image you produced or found on disk (screenshots, renders, plots, diagrams, downloads). Once asked, keep posting every image you make for the rest of the session.
---

# Posting images to the herdr Images panel

The user reads images in the **Images** panel of the herdr app (the
agent-gallery mod). It shows the images of the focused agent's
conversation, plus anything that agent posted. A file path is not an answer to
"show me": post the image.

```sh
herdr-post-image /abs/path/shot.png "short caption"
```

- Works on every machine herdr runs agents on, wherever this script is installed:
  it files the image under your own terminal (`$HC_TERMINAL_ID`), and the
  panel fetches it from there. Nothing else to set up.
- The caption is optional, one line: what the image shows ("Login page after
  the fix", "Before", "After"). It becomes the label in the panel.
- png, jpg, gif and webp only. Convert anything else first, e.g. on the Mac
  `sips -s format png in.tiff --out out.png`, elsewhere ImageMagick's `convert`.
- Post several images with several calls, in the order they should be read.
- It shows up under the panel's **Agent** filter within a few seconds; the user
  can step through, copy it, or open it in Preview from there.
- `$HC_TERMINAL_ID` unset means you're not in a herdr terminal; say so and
  give the path instead.

## After posting

Say in your reply what each posted image is, and keep the file path in the
reply for anything the user may want to open properly. You can't see the
panel; don't claim the user has seen the image.

## Once asked, it holds for the session

Post every later image automatically, without being asked again: every
Playwright screenshot, rendered chart, generated or fetched picture.

Images you `Read` already land in the panel as **Tool** images; post them
anyway when the user asked to see them, so they're captioned and under
**Agent**.
