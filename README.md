# felt

> My friend sent me an audio of a riff he made and I had so many specific feelings about different moments that I built a tool to send them back.

A tiny, self-contained tool for annotating audio with timestamped thoughts — and sending them as a gift.

No backend. No dependencies. No account. One HTML file that works in any browser, including offline.

---

## demo

Open [`demo.html`](demo.html) — audio and annotations already baked in. Press play and watch the thoughts appear.

---

## how it works

**annotating (you)**
1. Open `annotator.html` in any browser
2. Drop in an audio file
3. Press play and listen
4. Hit **pin this moment** (or press `P`) whenever you feel something — it drops a pin at that exact timestamp
5. Type your thought and save
6. Hit **export json** when you're done

**receiving (them)**
1. Open `annotator.html`
2. Drop in the audio file
3. Drop in the json file you sent them
4. Press play — your thoughts appear as the music plays, one at a time, fading in at the exact moment you felt them

**or: bake it all into one file**

If you want to send a single self-contained file with everything already inside — audio, annotations, no setup — you can embed them using the approach in [`bake.py`](bake.py).

```bash
python3 bake.py your_audio.mp3 annotations.json
# outputs: for_u.html — one file, send it and they just open it
```

---

## files

```
annotator.html   — the blank tool, use this yourself
demo.html        — live demo with audio + annotations baked in
bake.py          — script to bake audio + json into a single html file
```

---

## why

I wanted to respond to a piece of music my friend made with more than words. I wanted him to hear exactly what I was thinking at exactly the moment I was thinking it.

There's no good tool for this. Music annotation software is for producers and academics. This is for friends.

Built in an afternoon instead of working. Worth it.

---

*made with love by [pragya](https://github.com/pragueyerrr)*
