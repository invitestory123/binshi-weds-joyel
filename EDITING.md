# Customer Editing & Deployment Guide — Binshi weds Joyel

Wedding & Engagement Invitation website for **Dr Binshi Biju** and **Joyel Paul**.

This website harmoniously unites two luxury themes:
1. **Seashell Vows (Engagement Ceremony)**:
   - Tap-to-open video opener gate (`wedding-opener.mp4`)
   - Watercolor beach arch hero & couple walking illustration
   - Parentage blessings & residences
   - Live Engagement countdown timer (14 Jan 2027, 11:30 AM)
   - Engagement celebration card at Pavithram Convention Centre, Kundara
   - Venue map & Google Maps directions
   - Save our date calendar export (`.ics`)
2. **Gilded Hall (Wedding & Reception)**:
   - Starts directly after the curtain reveal with the grand palace hall architecture backdrop
   - Streaming rain-of-light golden particle beams & floating gold petals
   - Shimmering gold couple typography
   - Embedded couple loop video in golden filigree frame (`couple.mp4`)
   - Live Wedding countdown timer (18 Jan 2027, 10:30 AM)
   - Holy Mass Ceremony at St. Antony's shrine, Kanakamala
   - Wedding Reception at Kizhakuden's HeartLand Convention Centre, Chalakudy
   - Dual venue navigation & Add Wedding to Calendar export (`.ics`)
3. **Interactive RSVP Section**:
   - Guest name, phone, attendance options (Both, Engagement, Wedding & Reception, Unable to attend)
   - Interactive guest count selector (+ / -)
   - Direct "Send RSVP via WhatsApp" integration
   - Family contact details & addresses for both the Bride's and Groom's families
   - Copy invitation link utility

---

## Couple & Celebration Details

### The Bride:
- **Dr Binshi Biju**
- Daughter of Biju Yohannan and Shini Biju
- Address: Manthottathil House, Elampalloor, Kundara, Kollam, Kerala — 691501

### The Groom:
- **Joyel Paul**
- Son of Poulose Padinjarakaran Rappai and Siji Devasia
- Address: Padinjarakaran House, Kanakamala (Near Panampilly Memorial Govt. College Ground), Potta, Chalakudy, Kerala

### Engagement Ceremony:
- Date: Thursday, 14 January 2027 (11:30 AM onwards)
- Venue: Pavithram Convention Centre, Kundara, Bharanikavu - Kollam Road, Mulavana - PO, Kollam — 691503
- Maps Link: https://share.google/eKgdNtTLRLDoC2pMJ

### Wedding Nuptial Ceremony & Holy Mass:
- Date: Monday, 18 January 2027 (10:30 AM onwards)
- Church: St. Antony's shrine, Kanakamala, Mechira - Kanakamala Rd, Perambra, Keralam

### Wedding Reception:
- Date: Monday, 18 January 2027 (12:30 PM onwards)
- Venue: Kizhakuden's HeartLand Convention Centre, Athirapilly road, Koodapuzha, Chalakudy, Keralam — 680721
- Maps Link: https://share.google/Os4UVfy3K6uJ26IiD

---

## File Structure

```text
├── index.html                   # Combined responsive invitation
├── assets/
│   └── main.css                 # Combined responsive stylesheet
├── editable/
│   └── assets/
│       └── bgm.mp3              # Ambient background music track
├── seashell-vows/               # Seashell vows template assets & data
│   ├── editable/
│   │   ├── assets/
│   │   └── wedding-data.js
│   └── external/
├── gilded-hall/                 # Gilded hall template assets & data
│   ├── editable/
│   │   ├── assets/
│   │   └── wedding-data.js
│   └── external/
├── favicon.ico
└── EDITING.md
```
