Vortex X1 Iris Throttle Body — 3D Visualization

🚀 Kickstarter Pre-Launch Landing Page

Creator: Douglas Owens Jr. — OwenSonicInfinity
Location: Cleveland, OH 44089
Contact: owensonicinfinity@gmail.com
Website: owensonicinfinity.netlify.app
Phone: 440-281-6270

---

📋 Project Overview

A hyper-realistic, engineering-accurate 3D product visualization of the Vortex X1 Iris Throttle Body — a revolutionary 12-blade iris diaphragm mechanism designed to replace traditional butterfly valves on LS1–LS6 engines.

The live page serves as a Kickstarter pre-launch landing page with fully interactive 3D controls, engine audio, and a Telegram-powered AI chatbot for investor & earlybird inquiries.

---

🔧 Features

Feature Details
3D Engine Three.js — real-time WebGL rendering
LS6 Engine Model Full engine block, intake manifold, valve covers, oil pan, accessory drive
Engine Stand Steel stand with wheels, realistic shop-floor presentation
Iris Blades 12 flat, solid, overlapping plates — zero curvature, zero twist
Blade Mechanics True camera-aperture motion: retract completely into housing at WOT
Zero Shaft Obstruction No center shaft, no butterfly blade — smooth unobstructed bore
WOT Vapor Effect Subtle white vapor particles at 90-100% throttle
Drive-by-Wire Motor External motor housing, side-mounted
Manual Slider 0-100% throttle control with real-time blade animation
Engine Audio Synthesized V8 sound via Web Audio API — idle to 7200 RPM
Auto Cycle Mode Continuous open/close demonstration loop
Wireframe Mode Toggle to inspect blade mechanics
Orbit Controls Drag to rotate, scroll to zoom, right-drag to pan
Keyboard Shortcuts O=Open, C=Close, Space=Cycle, W=Wireframe, M=Mute, R=Reset

---

💬 Telegram Bot Integration

Feature Details
Chat Widget Floating Telegram bubble on the page
Lead Capture Visitors message the bot → forwarded directly to creator's phone
Real-time Replies Creator responds from Telegram, visitor gets reply instantly
Investor Inquiries All messages logged in Telegram chat history
Setup Free — uses @BotFather, no API keys, no paid services

---

⚙️ Setup Instructions

1. Create Your Telegram Bot (2 minutes)

1. Open Telegram, search @BotFather
2. Send /newbot
3. Name it (e.g. "Vortex X1 DaisyAI")
4. Choose a username (e.g. VortexX1Bot)
5. Copy the token BotFather gives you

2. Get Your Chat ID (30 seconds)

1. Send any message to your new bot
2. Visit: https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
3. Find "chat":{"id":123456789} — that's your chat ID

3. Configure the HTML File

Open index.html and find these lines near the top of the script block:

```javascript
const TELEGRAM_BOT_TOKEN = ''; // Paste your bot token here
const CREATOR_CHAT_ID = ''; // Paste your chat ID here
const TELEGRAM_BOT_USERNAME = 'YourBot'; // Your bot's @username
```

Paste your values between the quotes. Save.

---

🚀 Deploy to GitHub Pages (Free)

1. Push index.html to a GitHub repository
2. Go to Settings → Pages
3. Under Branch, select main → Save
4. Your site goes live at: https://yourusername.github.io/repo-name/

---

🎮 Keyboard Controls

Key Action
O Full Open (WOT)
C Full Close (Idle)
Space Toggle Auto Cycle
W Toggle Wireframe
M Mute/Unmute Engine
R Reset Camera

---

🎯 Kickstarter Integration

The green "KICKSTARTER COMING SOON" badge is ready to link to your campaign page. Replace the onclick handler or add your Kickstarter URL when your campaign goes live.

---

📁 File Structure

```
vortex-x1/
├── index.html    ← Everything (3D + sound + bot + legal)
└── README.md     ← This file
```

Single file. No dependencies to install. No build step. Just open and it works.

---

🛡️ Legal

© 2026 Douglas Owens Jr. — OwenSonicInfinity. All Rights Reserved.
All Vortex X1 designs, branding, and 3D assets are proprietary intellectual property.
Trademarks and copyrights reserved. Cleveland, OH 44089.

---

📞 Contact

· Email: owensonicinfinity@gmail.com
· Phone: 440-281-6270
· Website: owensonicinfinity.netlify.app
· Telegram: @YourBot (after setup)

---

Built for Kickstarter. Powered by Three.js. Driven by DaisyOS. 🌼🔥
