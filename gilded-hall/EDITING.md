# Customer Editing Guide — gilded-hall

Gilded palace hall wedding invitation featuring an animated tap-to-open cover video, rain-of-light particle animations, multi-event itinerary timeline, Google Map embed, and calendar synchronization.

---

## Normal Customer Changes

All routine customer edits are configured in:
→ `editable/wedding-data.js`

### 1. Couple Names & Header
Edit in `editable/wedding-data.js`:
- `bride`: Bride's first name (e.g. `"Ananya"`)
- `groom`: Groom's first name (e.g. `"Aarav"`)
- `invitationLine`: Formal invitation line above names
- `closing`: Signoff message at the bottom

### 2. Dates & Countdown
Edit in `editable/wedding-data.js`:
- `dateLabel`: Formatted wedding date string (e.g. `"Saturday, 12 December 2026"`)
- `shortDate`: Compact date display (e.g. `"12 . 12 . 2026"`)
- `countdownTarget`: ISO date-time string (`YYYY-MM-DDTHH:MM:SS+05:30`), drives live countdown timer & `.ics` calendar generation

### 3. Love Story
Edit `story` array in `editable/wedding-data.js`:
- Array of narrative paragraphs detailing how the couple met and their journey.

### 4. Itinerary & Events
Edit `events` array in `editable/wedding-data.js`:
- Each event has:
  - `name`: Event name (Haldi, Mehendi, Sangeet, Wedding, Reception)
  - `date`: Event date
  - `time`: Event time
  - `venue`: Specific hall or room
  - `note`: Short festive description

### 5. Venue & Maps
Edit `venue` in `editable/wedding-data.js`:
- `name`: Main palace/hall name
- `address`: Street address
- `hint`: Distance / transit landmark
- `mapsUrl`: Google Maps link
- `mapEmbed`: Google Maps iframe embed URL

### 6. Media & Video
Replace files in `editable/assets/` or update paths in `wedding-data.js`:
- `cover`: Envelope cover illustration (`cover.png`)
- `introVideo`: Entrance opening animation (`intro.mp4`)
- `coupleVideo`: Couple loop video (`couple.mp4`)
- `hall`: Hall background architecture (`hall.png`)
- `petals`, `divider`, `floral`: Decorative ornaments

---

## Rules for Future Agents

1. Make edits in `editable/wedding-data.js` and swap media files in `editable/assets/`.
2. Do not modify production files in `assets/` unless structural changes are requested.
3. Verify syntax with `node --check editable/wedding-data.js`.
