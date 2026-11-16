import os
import shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ==============================================================================
# 1. GENERATE OPEN GRAPH PREVIEW IMAGE (1200 x 630 px)
# ==============================================================================
def generate_og_image():
    W, H = 1200, 630

    # Base background: luxurious warm cream / blush ivory (#fffcf9)
    base = Image.new('RGBA', (W, H), (255, 252, 249, 255))

    # Soft romantic glowing halos
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow)
    # Warm golden backlight behind couple
    g_draw.ellipse([690, 40, 1170, 600], fill=(255, 244, 222, 190))
    g_draw.ellipse([760, 90, 1100, 550], fill=(255, 250, 238, 230))
    # Soft rose blush glow behind left typography
    g_draw.ellipse([60, 60, 720, 570], fill=(253, 242, 243, 170))
    glow = glow.filter(ImageFilter.GaussianBlur(50))
    base = Image.alpha_composite(base, glow)

    # Double Gold & Rose Border with Rosettes (drawn before couple for depth)
    border_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(border_layer)
    gold_outer = (201, 155, 66, 210)    # #c99b42
    gold_inner = (223, 190, 126, 140)   # #dfbe7e
    rose_accent = (155, 34, 52, 190)    # #9b2234

    b_draw.rectangle([24, 24, W - 24, H - 24], outline=gold_outer, width=2)
    b_draw.rectangle([32, 32, W - 32, H - 32], outline=gold_inner, width=1)

    # Corner rosettes
    for cx, cy in [(24, 24), (W - 24, 24), (24, H - 24), (W - 24, H - 24)]:
        b_draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=gold_outer)
        b_draw.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=rose_accent)

    base = Image.alpha_composite(base, border_layer)

    # Floral corner accents
    try:
        corner = Image.open('editable/assets/floral-corner.png').convert('RGBA')
        c_tl = corner.resize((190, 190), Image.Resampling.LANCZOS)
        base.paste(c_tl, (8, 8), c_tl)
    except Exception as e:
        print('Floral corner note:', e)

    # Composite Bride & Groom illustration on the right side
    try:
        couple_raw = Image.open('seashell-vows/editable/assets/couple-walking.png').convert('RGBA')
        aspect = couple_raw.width / couple_raw.height
        c_h = 560
        c_w = int(c_h * aspect)
        couple = couple_raw.resize((c_w, c_h), Image.Resampling.LANCZOS)

        # Soft drop shadow underneath couple
        c_shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        s_draw = ImageDraw.Draw(c_shadow)
        s_draw.ellipse([W - c_w - 70, H - 85, W - 20, H - 35], fill=(74, 44, 53, 60))
        c_shadow = c_shadow.filter(ImageFilter.GaussianBlur(16))
        base = Image.alpha_composite(base, c_shadow)

        # Paste couple
        couple_x = W - c_w - 35
        couple_y = H - c_h - 26
        base.paste(couple, (couple_x, couple_y), couple)
    except Exception as e:
        print('Couple image note:', e)

    # Re-stamp bottom-right border corner cleanly over bottom hem if needed
    corner_clip = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    cc_draw = ImageDraw.Draw(corner_clip)
    # Right border segment
    cc_draw.line([W - 24, H - 60, W - 24, H - 24], fill=gold_outer, width=2)
    cc_draw.line([W - 60, H - 24, W - 24, H - 24], fill=gold_outer, width=2)
    cc_draw.ellipse([W - 29, H - 29, W - 19, H - 19], fill=gold_outer)
    cc_draw.ellipse([W - 26, H - 26, W - 22, H - 22], fill=rose_accent)
    base = Image.alpha_composite(base, corner_clip)

    # Left content panel drawing
    draw = ImageDraw.Draw(base)

    # Fonts
    f_tagline = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 14)
    f_names = ImageFont.truetype('C:/Windows/Fonts/palab.ttf', 52)
    f_weds = ImageFont.truetype('C:/Windows/Fonts/palabi.ttf', 36)
    f_event_hdr = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 15)
    f_event_time = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 16)
    f_event_sub = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 13)
    f_badge = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 13)

    # Colors
    c_dark = (34, 20, 23, 255)         # #221417 (High-contrast dark rosewood)
    c_ruby = (139, 30, 46, 255)        # #8b1e2e (Deep luxury ruby)
    c_gold = (168, 126, 42, 255)       # #a87e2a (Warm antique gold)
    c_muted = (74, 44, 53, 255)        # #4a2c35 (Crisp secondary text)

    left_cx = 390

    def draw_centered(y, text, font, color):
        bbox = draw.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        draw.text((left_cx - w // 2, y), text, fill=color, font=font)

    # 1. Eyebrow Tagline
    draw_centered(62, "T O G E T H E R   W I T H   O U R   F A M I L I E S", f_tagline, c_gold)

    # Decorative mini divider line
    draw.line([left_cx - 80, 90, left_cx + 80, 90], fill=gold_inner, width=1)
    draw.polygon([(left_cx, 87), (left_cx + 4, 90), (left_cx, 93), (left_cx - 4, 90)], fill=c_ruby)

    # 2. Grand Couple Names
    draw_centered(110, "Joyel Paul", f_names, c_dark)
    draw_centered(168, "weds", f_weds, c_ruby)
    draw_centered(210, "Dr. Binshi Biju", f_names, c_dark)

    # 3. Golden Divider Flourish
    try:
        div = Image.open('gilded-hall/editable/assets/divider.png').convert('RGBA')
        div_w = 190
        div_h = int(div_w * div.height / div.width)
        div_resized = div.resize((div_w, div_h), Image.Resampling.LANCZOS)
        base.paste(div_resized, (left_cx - div_w // 2, 274), div_resized)
    except Exception as e:
        draw.line([left_cx - 90, 285, left_cx + 90, 285], fill=gold_inner, width=1)

    # 4. Ceremony 1: Engagement Card Box
    card1_y = 310
    c1_box = [left_cx - 295, card1_y, left_cx + 295, card1_y + 94]
    draw.rounded_rectangle(c1_box, radius=8, fill=(255, 255, 255, 235), outline=(237, 210, 215, 255), width=1)
    draw.rounded_rectangle([c1_box[0], c1_box[1], c1_box[0] + 5, c1_box[3]], radius=3, fill=c_ruby)

    draw.text((c1_box[0] + 18, card1_y + 12), "RING EXCHANGE & FEAST  ·  THURSDAY, 14 JAN 2027", fill=c_ruby, font=f_event_hdr)
    draw.text((c1_box[0] + 18, card1_y + 36), "11:30 AM  ·  Pavithram Convention Centre", fill=c_dark, font=f_event_time)
    draw.text((c1_box[0] + 18, card1_y + 62), "Kundara, Bharanikavu - Kollam Road, Mulavana PO, Kollam", fill=c_muted, font=f_event_sub)

    # 5. Ceremony 2: Holy Matrimony & Reception Card Box
    card2_y = 416
    c2_box = [left_cx - 295, card2_y, left_cx + 295, card2_y + 98]
    draw.rounded_rectangle(c2_box, radius=8, fill=(255, 255, 255, 235), outline=(237, 210, 215, 255), width=1)
    draw.rounded_rectangle([c2_box[0], c2_box[1], c2_box[0] + 5, c2_box[3]], radius=3, fill=c_gold)

    draw.text((c2_box[0] + 18, card2_y + 12), "HOLY MATRIMONY & RECEPTION  ·  MONDAY, 18 JAN 2027", fill=c_ruby, font=f_event_hdr)
    draw.text((c2_box[0] + 18, card2_y + 36), "10:30 AM Mass at St. Antony's Church, Kanakamala", fill=c_dark, font=f_event_time)
    draw.text((c2_box[0] + 18, card2_y + 62), "12:30 PM Reception at Kizhakuden's HeartLand, Chalakudy", fill=c_muted, font=f_event_sub)

    # 6. Bottom Invitation Callout Tag (using standard bullet separator to prevent font box glyphs)
    draw_centered(542, "•   WEDDING & ENGAGEMENT INVITATION   •", f_badge, c_gold)

    # Save images
    base.save('og-image.png', 'PNG', optimize=True)
    rgb_base = base.convert('RGB')
    rgb_base.save('og-image.jpg', 'JPEG', quality=95, optimize=True, progressive=True)
    print("Generated og-image.png and og-image.jpg successfully!")


# ==============================================================================
# 2. GENERATE OG LOGO & MONOGRAM SUITE (512x512, 180x180, 32x32, 16x16, ICO)
# ==============================================================================
def generate_og_logo():
    S = 512
    logo = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    draw = ImageDraw.Draw(logo)

    cx, cy = S // 2, S // 2

    # Circular luxury seal
    r_outer = 244
    r_inner = 236
    r_gold = 224

    draw.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer], fill=(255, 250, 245, 255), outline=(201, 155, 66, 230), width=4)
    draw.ellipse([cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner], fill=None, outline=(237, 210, 215, 200), width=2)
    draw.ellipse([cx - r_gold, cy - r_gold, cx + r_gold, cy + r_gold], fill=None, outline=(223, 190, 126, 180), width=1)

    # Top rose garland accent
    try:
        rose = Image.open('editable/assets/rose-garland.png').convert('RGBA')
        r_w = 210
        r_h = int(r_w * rose.height / rose.width)
        rose_top = rose.resize((r_w, r_h), Image.Resampling.LANCZOS)
        logo.paste(rose_top, (cx - r_w // 2, 44), rose_top)
    except Exception as e:
        print('Logo garland note:', e)

    # Fonts
    f_initials = ImageFont.truetype('C:/Windows/Fonts/palab.ttf', 130)
    f_amp = ImageFont.truetype('C:/Windows/Fonts/palabi.ttf', 86)
    f_names = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 20)
    f_date = ImageFont.truetype('C:/Windows/Fonts/georgia.ttf', 15)

    c_ruby = (139, 30, 46, 255)   # #8b1e2e
    c_gold = (184, 142, 47, 255)  # #b88e2f
    c_dark = (34, 20, 23, 255)    # #221417

    # Measure exact bounding boxes for initials
    bbox_j = draw.textbbox((0, 0), 'J', font=f_initials)
    bbox_amp = draw.textbbox((0, 0), '&', font=f_amp)
    bbox_b = draw.textbbox((0, 0), 'B', font=f_initials)

    w_j = bbox_j[2] - bbox_j[0]
    w_amp = bbox_amp[2] - bbox_amp[0]
    w_b = bbox_b[2] - bbox_b[0]

    gap = 14
    total_w = w_j + gap + w_amp + gap + w_b
    start_x = (S - total_w) // 2

    # Vertical alignment: Cap-height alignment so tops of J and B match
    target_top = 160
    y_j = target_top - bbox_j[1]
    y_b = target_top - bbox_b[1]
    # Center '&' vertically within cap height
    cap_h = bbox_b[3] - bbox_b[1]
    amp_h = bbox_amp[3] - bbox_amp[1]
    y_amp = target_top + (cap_h - amp_h) // 2 - bbox_amp[1]

    # Draw J & B
    x_j = start_x
    x_amp = x_j + w_j + gap
    x_b = x_amp + w_amp + gap

    draw.text((x_j, y_j), 'J', fill=c_ruby, font=f_initials)
    draw.text((x_amp, y_amp), '&', fill=c_gold, font=f_amp)
    draw.text((x_b, y_b), 'B', fill=c_ruby, font=f_initials)

    # Dividing flourish line
    draw.line([cx - 85, 335, cx + 85, 335], fill=(201, 155, 66, 180), width=1)
    draw.polygon([(cx, 332), (cx + 4, 335), (cx, 338), (cx - 4, 335)], fill=c_ruby)

    # Names and dates
    def draw_centered_logo(y, text, font, color):
        bbox = draw.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        draw.text((cx - w // 2, y), text, fill=color, font=font)

    draw_centered_logo(355, "JOYEL   ·   BINSHI", f_names, c_dark)
    draw_centered_logo(395, "·   14  &  18  JANUARY  2027   ·", f_date, c_gold)

    # Save 512x512 og-logo.png and logo.png
    logo.save('og-logo.png', 'PNG', optimize=True)
    logo.save('logo.png', 'PNG', optimize=True)

    # Apple Touch Icon 180x180
    apple_icon = logo.resize((180, 180), Image.Resampling.LANCZOS)
    apple_icon.save('apple-touch-icon.png', 'PNG', optimize=True)

    # Favicons
    fav32 = logo.resize((32, 32), Image.Resampling.LANCZOS)
    fav32.save('favicon-32x32.png', 'PNG', optimize=True)
    fav16 = logo.resize((16, 16), Image.Resampling.LANCZOS)
    fav16.save('favicon-16x16.png', 'PNG', optimize=True)

    # Multi-resolution favicon.ico
    logo.save('favicon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])

    print("Generated og-logo.png, logo.png, apple-touch-icon.png, and multi-res favicon.ico successfully!")

if __name__ == '__main__':
    generate_og_image()
    generate_og_logo()
    
    # Copy to artifact directory for previewing
    art_dir = r'C:\Users\mhdsi\.gemini\antigravity\brain\2d0d8ef8-f227-4f46-be7f-169497d3f1a7'
    if os.path.exists(art_dir):
        shutil.copy('og-image.jpg', os.path.join(art_dir, 'og-image.jpg'))
        shutil.copy('og-logo.png', os.path.join(art_dir, 'og-logo.png'))
