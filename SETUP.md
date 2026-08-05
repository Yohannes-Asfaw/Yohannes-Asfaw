# GitHub Profile README — Setup Guide

## 1. Create the profile repository

1. Go to GitHub and create a **new public repository** named exactly **`Yohannes-Asfaw`** (same as your username).
2. Upload **everything** from this folder — not just `README.md`:

```
Yohannes-Asfaw/
├── README.md
├── assets/                    ← REQUIRED (images live here)
│   ├── about-me.svg
│   ├── github-stats.svg
│   ├── github-streak.svg
│   ├── top-langs.svg
│   └── contribution-snake.svg
└── .github/workflows/
    ├── stats.yml              ← refreshes stats daily
    └── snake.yml              ← generates snake animation
```

3. Your profile appears at: **https://github.com/Yohannes-Asfaw**

> **Important:** If you only upload `README.md` without the `assets/` folder, all images will be broken.

## 2. Customize before publishing

| Item | What to change |
|------|----------------|
| **Email** | Replace `yohannes.asfaw@example.com` with your real email |
| **Featured Work** | Add 2–3 real projects with links and impact metrics |
| **Pin repos** | Pin your best 6 repos on your GitHub profile page |

## 3. Enable auto-updates (optional)

After pushing, go to **Actions** tab and run both workflows once:

1. **Update Profile Stats** — refreshes stat cards daily
2. **Generate Snake Animation** — replaces the snake placeholder with your real contribution grid

## 4. Why images were broken before

External stat APIs (`github-readme-stats.vercel.app`, trophies, etc.) fail often on GitHub. This README now uses **SVG files stored in your repo**, which always load reliably.

## 5. Maximize recruiter impact

- Add **quantified results** to project rows (users, performance, revenue).
- Keep commits and contributions active.
- Ensure LinkedIn matches your GitHub story.
