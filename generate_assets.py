"""
generate_assets.py - Generates bespoke luxury SVG assets for Floral Flirtss website
Brand palette:
- Cream background: #FFF9F6
- Soft blush: #F8E8ED
- Light pink: #EAB9CA
- Rose: #D98EAA
- Deep mauve: #806477
- Dark text: #292329
"""

import os

os.makedirs("assets/images", exist_ok=True)

# 1. Favicon SVG
favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <radialGradient id="favBg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF9F6"/>
      <stop offset="100%" stop-color="#F8E8ED"/>
    </radialGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EAB9CA"/>
      <stop offset="100%" stop-color="#D98EAA"/>
    </linearGradient>
  </defs>
  <circle cx="32" cy="32" r="30" fill="url(#favBg)" stroke="#D98EAA" stroke-width="2"/>
  <!-- Petals -->
  <g transform="translate(32,32)">
    <path d="M0,0 C-10,-18 10,-18 0,0" fill="url(#roseGrad)" transform="rotate(0)"/>
    <path d="M0,0 C-10,-18 10,-18 0,0" fill="url(#roseGrad)" transform="rotate(60)"/>
    <path d="M0,0 C-10,-18 10,-18 0,0" fill="url(#roseGrad)" transform="rotate(120)"/>
    <path d="M0,0 C-10,-18 10,-18 0,0" fill="url(#roseGrad)" transform="rotate(180)"/>
    <path d="M0,0 C-10,-18 10,-18 0,0" fill="url(#roseGrad)" transform="rotate(240)"/>
    <path d="M0,0 C-10,-18 10,-18 0,0" fill="url(#roseGrad)" transform="rotate(300)"/>
    <circle cx="0" cy="0" r="5" fill="#806477"/>
    <circle cx="0" cy="0" r="2.5" fill="#FFF9F6"/>
  </g>
</svg>'''

with open("assets/images/favicon.svg", "w", encoding="utf-8") as f:
    f.write(favicon_svg)

# Helper function to create SVG placeholder card with aesthetic botanical illustration
def create_editorial_card(filename, width, height, title, subtitle, flower_type, tag="Floral Flirtss"):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF9F6"/>
      <stop offset="50%" stop-color="#F8E8ED"/>
      <stop offset="100%" stop-color="#F3DFE5"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EAB9CA"/>
      <stop offset="100%" stop-color="#D98EAA"/>
    </linearGradient>
    <linearGradient id="mauveGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#9C7E92"/>
      <stop offset="100%" stop-color="#806477"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFE394"/>
      <stop offset="100%" stop-color="#F3B748"/>
    </linearGradient>
    <linearGradient id="creamGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#F8E8ED"/>
    </linearGradient>
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="12" stdDeviation="20" flood-color="#806477" flood-opacity="0.12"/>
    </filter>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="30" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="{width}" height="{height}" fill="url(#bgGrad)"/>
  
  <!-- Subtle decorative background arches / circles -->
  <circle cx="{width*0.8}" cy="{height*0.2}" r="{width*0.35}" fill="#EAB9CA" opacity="0.25" filter="url(#softGlow)"/>
  <circle cx="{width*0.15}" cy="{height*0.75}" r="{width*0.25}" fill="#D98EAA" opacity="0.18" filter="url(#softGlow)"/>
  
  <!-- Outer delicate border frame -->
  <rect x="20" y="20" width="{width-40}" height="{height-40}" fill="none" stroke="#D98EAA" stroke-width="1.2" stroke-opacity="0.35" rx="16"/>
  <rect x="28" y="28" width="{width-56}" height="{height-56}" fill="none" stroke="#806477" stroke-width="0.8" stroke-dasharray="4 4" stroke-opacity="0.2" rx="12"/>

  <!-- Centered Botanical Art Composition -->
  <g transform="translate({width/2}, {height*0.46})">
'''
    # Custom floral art per type
    if flower_type == "tulips":
        svg += '''
    <!-- Stems -->
    <path d="M-40,160 Q-20,60 -10,-10" stroke="#7A8F74" stroke-width="8" stroke-linecap="round" fill="none"/>
    <path d="M0,170 Q5,70 10,-30" stroke="#688062" stroke-width="9" stroke-linecap="round" fill="none"/>
    <path d="M40,160 Q25,80 30,-5" stroke="#7A8F74" stroke-width="8" stroke-linecap="round" fill="none"/>
    <!-- Leaves -->
    <path d="M-15,90 Q-70,50 -60,0 Q-30,40 -12,70" fill="#7A8F74" opacity="0.9"/>
    <path d="M15,100 Q70,60 65,10 Q35,50 18,80" fill="#688062" opacity="0.85"/>
    <path d="M-5,130 Q-50,110 -40,70 Q-20,95 -2,110" fill="#8FA489" opacity="0.9"/>
    <!-- Left Tulip -->
    <g transform="translate(-40,-20) rotate(-14)">
      <path d="M-25,20 C-35,-20 0,-70 0,-70 C0,-70 35,-20 25,20 C20,38 -20,38 -25,20 Z" fill="url(#roseGrad)"/>
      <path d="M-15,18 C-25,-10 0,-60 0,-60 C0,-60 25,-10 15,18 Z" fill="#F8E8ED" opacity="0.85"/>
      <path d="M-28,10 C-35,-15 -10,-55 -10,-55 C-22,-20 -20,5 -28,10 Z" fill="#D98EAA" opacity="0.9"/>
    </g>
    <!-- Right Tulip -->
    <g transform="translate(42,-15) rotate(16)">
      <path d="M-25,20 C-35,-20 0,-70 0,-70 C0,-70 35,-20 25,20 C20,38 -20,38 -25,20 Z" fill="#EAB9CA"/>
      <path d="M-15,18 C-25,-10 0,-60 0,-60 C0,-60 25,-10 15,18 Z" fill="#FFF9F6" opacity="0.9"/>
      <path d="M10,-55 C10,-55 35,-15 28,10 C20,5 22,-20 10,-55 Z" fill="#D98EAA" opacity="0.9"/>
    </g>
    <!-- Center Main Tulip -->
    <g transform="translate(0,-45)">
      <path d="M-32,25 C-45,-25 0,-85 0,-85 C0,-85 45,-25 32,25 C25,48 -25,48 -32,25 Z" fill="url(#roseGrad)" filter="url(#cardShadow)"/>
      <path d="M-20,22 C-32,-15 0,-72 0,-72 C0,-72 32,-15 20,22 C14,35 -14,35 -20,22 Z" fill="#FFF9F6" opacity="0.85"/>
      <path d="M-36,12 C-45,-18 -12,-70 -12,-70 C-28,-25 -25,5 -36,12 Z" fill="#D98EAA"/>
      <path d="M36,12 C45,-18 12,-70 12,-70 C28,-25 25,5 36,12 Z" fill="#D98EAA"/>
    </g>
    <!-- Silk Bow -->
    <g transform="translate(0, 110)">
      <ellipse cx="-26" cy="-4" rx="28" ry="12" fill="#D98EAA" transform="rotate(-15)"/>
      <ellipse cx="26" cy="-4" rx="28" ry="12" fill="#D98EAA" transform="rotate(15)"/>
      <circle cx="0" cy="0" r="9" fill="#806477"/>
      <path d="M-6,6 Q-25,50 -35,80" stroke="#D98EAA" stroke-width="7" stroke-linecap="round" fill="none"/>
      <path d="M6,6 Q25,50 35,80" stroke="#D98EAA" stroke-width="7" stroke-linecap="round" fill="none"/>
    </g>
'''
    elif flower_type == "lilies":
        svg += '''
    <!-- Stems & Foliage -->
    <path d="M-15,170 Q-5,60 0,-10" stroke="#688062" stroke-width="9" stroke-linecap="round" fill="none"/>
    <path d="M-8,80 Q-70,50 -55,-10 Q-25,30 -5,60" fill="#7A8F74"/>
    <path d="M8,95 Q70,60 60,0 Q30,40 10,75" fill="#688062"/>
    <!-- Grand Lily Flower -->
    <g transform="translate(0,-30)">
      <!-- 6 elegant petals radiating -->
      <path d="M0,0 Q-45,-70 0,-120 Q45,-70 0,0" fill="url(#creamGrad)" stroke="#D98EAA" stroke-width="1.5"/>
      <path d="M0,0 Q-70,-35 -115,-40 Q-75,15 0,0" fill="url(#creamGrad)" stroke="#D98EAA" stroke-width="1.5"/>
      <path d="M0,0 Q70,-35 115,-40 Q75,15 0,0" fill="url(#creamGrad)" stroke="#D98EAA" stroke-width="1.5"/>
      <path d="M0,0 Q-65,45 -95,85 Q-35,65 0,0" fill="url(#creamGrad)" stroke="#D98EAA" stroke-width="1.5"/>
      <path d="M0,0 Q65,45 95,85 Q35,65 0,0" fill="url(#creamGrad)" stroke="#D98EAA" stroke-width="1.5"/>
      <path d="M0,0 Q0,80 0,110 Q-15,70 0,0" fill="url(#creamGrad)" stroke="#D98EAA" stroke-width="1.5"/>
      <!-- Soft blush centers & freckles -->
      <path d="M0,0 Q-18,-45 0,-80 Q18,-45 0,0" fill="#EAB9CA" opacity="0.6"/>
      <path d="M0,0 Q-45,-20 -70,-25 Q-45,10 0,0" fill="#EAB9CA" opacity="0.6"/>
      <path d="M0,0 Q45,-20 70,-25 Q45,10 0,0" fill="#EAB9CA" opacity="0.6"/>
      <!-- Delicate Stamens -->
      <path d="M0,0 Q-15,-30 -25,-60" stroke="#806477" stroke-width="2" fill="none"/>
      <ellipse cx="-25" cy="-60" rx="4" ry="2" fill="#D98EAA"/>
      <path d="M0,0 Q0,-35 0,-65" stroke="#806477" stroke-width="2" fill="none"/>
      <ellipse cx="0" cy="-65" rx="4" ry="2" fill="#D98EAA"/>
      <path d="M0,0 Q15,-30 25,-60" stroke="#806477" stroke-width="2" fill="none"/>
      <ellipse cx="25" cy="-60" rx="4" ry="2" fill="#D98EAA"/>
      <circle cx="0" cy="0" r="7" fill="#806477"/>
    </g>
    <!-- Ribbon -->
    <g transform="translate(0, 115)">
      <ellipse cx="-24" cy="-3" rx="26" ry="11" fill="#806477" transform="rotate(-15)"/>
      <ellipse cx="24" cy="-3" rx="26" ry="11" fill="#806477" transform="rotate(15)"/>
      <circle cx="0" cy="0" r="8" fill="#D98EAA"/>
      <path d="M-5,5 Q-20,40 -28,70" stroke="#806477" stroke-width="6" stroke-linecap="round" fill="none"/>
      <path d="M5,5 Q20,40 28,70" stroke="#806477" stroke-width="6" stroke-linecap="round" fill="none"/>
    </g>
'''
    elif flower_type == "sunflowers":
        svg += '''
    <!-- Stems & Foliage -->
    <path d="M0,170 Q-10,70 0,-15" stroke="#5E7457" stroke-width="11" stroke-linecap="round" fill="none"/>
    <path d="M-10,95 Q-80,75 -70,10 Q-30,40 -5,80" fill="#6B8364"/>
    <path d="M10,110 Q85,85 75,20 Q35,50 5,95" fill="#5E7457"/>
    <!-- Giant Radiant Sunflower -->
    <g transform="translate(0,-30)">
      <!-- Outer Petals Layer -->
      <g>
'''
        # 16 petals around
        for deg in range(0, 360, 24):
            svg += f'''        <path d="M0,0 C-14,-35 -16,-90 0,-115 C16,-90 14,-35 0,0" fill="url(#goldGrad)" transform="rotate({deg})"/>\n'''
        svg += '''      </g>
      <!-- Inner Petals Layer offset -->
      <g opacity="0.95">
'''
        for deg in range(12, 360, 24):
            svg += f'''        <path d="M0,0 C-12,-30 -14,-75 0,-98 C14,-75 12,-30 0,0" fill="#FFAE19" transform="rotate({deg})"/>\n'''
        svg += '''      </g>
      <!-- Textured Seed Center -->
      <circle cx="0" cy="0" r="48" fill="#4A3428" filter="url(#cardShadow)"/>
      <circle cx="0" cy="0" r="43" fill="#6B4423"/>
      <circle cx="0" cy="0" r="38" fill="#80532C"/>
      <!-- Concentric stipples/texture -->
      <circle cx="0" cy="0" r="28" fill="none" stroke="#A6703B" stroke-width="3" stroke-dasharray="3 4"/>
      <circle cx="0" cy="0" r="18" fill="none" stroke="#DDA15E" stroke-width="2.5" stroke-dasharray="2 3"/>
      <circle cx="0" cy="0" r="8" fill="#DDA15E"/>
    </g>
    <!-- Rustic Rose Silk Tie -->
    <g transform="translate(0, 115)">
      <ellipse cx="-24" cy="-3" rx="26" ry="11" fill="#D98EAA" transform="rotate(-15)"/>
      <ellipse cx="24" cy="-3" rx="26" ry="11" fill="#D98EAA" transform="rotate(15)"/>
      <circle cx="0" cy="0" r="8" fill="#806477"/>
      <path d="M-5,5 Q-20,40 -28,70" stroke="#D98EAA" stroke-width="6" stroke-linecap="round" fill="none"/>
      <path d="M5,5 Q20,40 28,70" stroke="#D98EAA" stroke-width="6" stroke-linecap="round" fill="none"/>
    </g>
'''
    elif flower_type == "custom":
        svg += '''
    <!-- Mixed Bouquet in Kraft Wrap -->
    <!-- Kraft Wrapping Fold -->
    <path d="M-80,140 L-110,0 L0,-40 L110,0 L80,140 Z" fill="#F8E8ED" stroke="#D98EAA" stroke-width="2"/>
    <path d="M-80,140 L-10,130 L-30,0 L-110,0 Z" fill="#F3DFE5" opacity="0.6"/>
    <!-- Flowers erupting from wrap -->
    <!-- Tulip top left -->
    <g transform="translate(-45,-40) rotate(-15) scale(0.65)">
      <path d="M-25,20 C-35,-20 0,-70 0,-70 C0,-70 35,-20 25,20 C20,38 -20,38 -25,20 Z" fill="url(#roseGrad)"/>
    </g>
    <!-- Sunflower center -->
    <g transform="translate(0,-65) scale(0.55)">
'''
        for deg in range(0, 360, 30):
            svg += f'''      <path d="M0,0 C-14,-35 -16,-90 0,-115 C16,-90 14,-35 0,0" fill="url(#goldGrad)" transform="rotate({deg})"/>\n'''
        svg += '''      <circle cx="0" cy="0" r="42" fill="#5C3D2E"/>
    </g>
    <!-- Lily top right -->
    <g transform="translate(45,-45) rotate(20) scale(0.6)">
      <path d="M0,0 Q-40,-60 0,-100 Q40,-60 0,0" fill="url(#creamGrad)" stroke="#D98EAA"/>
      <path d="M0,0 Q-60,-20 -90,-20 Q-50,20 0,0" fill="url(#creamGrad)" stroke="#D98EAA"/>
      <path d="M0,0 Q60,-20 90,-20 Q50,20 0,0" fill="url(#creamGrad)" stroke="#D98EAA"/>
      <circle cx="0" cy="0" r="8" fill="#806477"/>
    </g>
    <!-- Eucalyptus / Filler Foliage -->
    <circle cx="-65" cy="-10" r="14" fill="#7A8F74" opacity="0.8"/>
    <circle cx="-50" cy="15" r="12" fill="#8FA489" opacity="0.8"/>
    <circle cx="65" cy="-10" r="14" fill="#7A8F74" opacity="0.8"/>
    <circle cx="50" cy="15" r="12" fill="#8FA489" opacity="0.8"/>
    <!-- Giant Mauve Silk Bow around wrap -->
    <g transform="translate(0, 80)">
      <ellipse cx="-32" cy="-4" rx="34" ry="14" fill="#806477" transform="rotate(-15)"/>
      <ellipse cx="32" cy="-4" rx="34" ry="14" fill="#806477" transform="rotate(15)"/>
      <circle cx="0" cy="0" r="11" fill="#D98EAA"/>
      <path d="M-8,8 Q-30,55 -40,90" stroke="#806477" stroke-width="8" stroke-linecap="round" fill="none"/>
      <path d="M8,8 Q30,55 40,90" stroke="#806477" stroke-width="8" stroke-linecap="round" fill="none"/>
    </g>
'''
    elif flower_type == "special":
        svg += '''
    <!-- Luxury Keepsake Bell Jar / Presentation Box -->
    <!-- Pedestal Base -->
    <ellipse cx="0" cy="130" rx="90" ry="24" fill="#806477" filter="url(#cardShadow)"/>
    <ellipse cx="0" cy="126" rx="84" ry="20" fill="#9C7E92"/>
    <ellipse cx="0" cy="120" rx="76" ry="16" fill="#F8E8ED"/>
    <!-- Glass Bell Jar Dome Outline -->
    <path d="M-65,120 L-65,-30 C-65,-100 65,-100 65,-30 L65,120 Z" fill="#FFF9F6" fill-opacity="0.3" stroke="#D98EAA" stroke-width="2.5"/>
    <ellipse cx="0" cy="-90" rx="14" ry="10" fill="#D98EAA"/>
    <!-- Preserved Eternal Arrangement Inside Dome -->
    <!-- Central Statement Rose / Bloom -->
    <g transform="translate(0,25) scale(0.95)">
      <!-- Petal spiral -->
      <path d="M-30,20 C-40,-15 0,-60 0,-60 C0,-60 40,-15 30,20 C20,38 -20,38 -30,20 Z" fill="url(#roseGrad)"/>
      <path d="M-18,15 C-25,-10 0,-50 0,-50 C0,-50 25,-10 18,15 Z" fill="#FFF9F6" opacity="0.9"/>
      <circle cx="0" cy="5" r="12" fill="#806477"/>
      <path d="M-5,7 Q-15,60 -5,95" stroke="#688062" stroke-width="6" fill="none"/>
      <!-- Fallen petals on velvet pedestal -->
      <ellipse cx="-35" cy="95" rx="15" ry="6" fill="#EAB9CA" transform="rotate(-15)"/>
      <ellipse cx="30" cy="98" rx="12" ry="5" fill="#D98EAA" transform="rotate(20)"/>
    </g>
    <!-- Subtle Golden Sparkles -->
    <polygon points="0,-40 3,-30 13,-30 5,-23 8,-13 0,-18 -8,-13 -5,-23 -13,-30 -3,-30" fill="#F3B748" transform="translate(40,-10) scale(0.6)"/>
    <polygon points="0,-40 3,-30 13,-30 5,-23 8,-13 0,-18 -8,-13 -5,-23 -13,-30 -3,-30" fill="#F3B748" transform="translate(-40,-45) scale(0.5)"/>
'''
    elif flower_type == "story":
        svg += '''
    <!-- Artisan Studio / Handcrafting Table Scene -->
    <!-- Wooden Tabletop Base -->
    <rect x="-350" y="80" width="700" height="200" fill="#F8E8ED" rx="12" stroke="#D98EAA" stroke-width="1.5"/>
    <!-- Cutting Mat / Linen Cloth -->
    <rect x="-240" y="40" width="480" height="180" fill="#FFFFFF" rx="8" stroke="#806477" stroke-width="1" stroke-dasharray="3 3"/>
    
    <!-- Artisan Craft Scissors -->
    <g transform="translate(-140, 100) rotate(35) scale(0.8)">
      <circle cx="-25" cy="0" r="18" fill="none" stroke="#806477" stroke-width="5"/>
      <circle cx="25" cy="0" r="18" fill="none" stroke="#806477" stroke-width="5"/>
      <line x1="-15" y1="0" x2="0" y2="45" stroke="#806477" stroke-width="5"/>
      <line x1="15" y1="0" x2="0" y2="45" stroke="#806477" stroke-width="5"/>
      <path d="M0,45 L-12,120 L0,115 L12,120 Z" fill="#D98EAA"/>
    </g>
    
    <!-- Handcrafted Blooms in progress -->
    <g transform="translate(60, 40) rotate(-15)">
      <!-- Tulip stem -->
      <path d="M-10,100 Q15,40 5,-30" stroke="#7A8F74" stroke-width="7" stroke-linecap="round" fill="none"/>
      <!-- Flower head -->
      <path d="M-25,20 C-35,-20 0,-70 0,-70 C0,-70 35,-20 25,20 C20,38 -20,38 -25,20 Z" fill="url(#roseGrad)"/>
      <path d="M-15,18 C-25,-10 0,-60 0,-60 C0,-60 25,-10 15,18 Z" fill="#FFF9F6" opacity="0.9"/>
    </g>

    <!-- Spool of Luxury Silk Ribbon -->
    <g transform="translate(-40, 120)">
      <ellipse cx="0" cy="-15" rx="22" ry="9" fill="#D98EAA"/>
      <rect x="-22" y="-15" width="44" height="28" fill="#EAB9CA"/>
      <ellipse cx="0" cy="13" rx="22" ry="9" fill="#D98EAA"/>
      <path d="M18,5 Q50,45 80,35" stroke="#D98EAA" stroke-width="9" stroke-linecap="round" fill="none"/>
    </g>

    <!-- Handwritten Tag: "With Love, Hyderabad" -->
    <g transform="translate(160, 110) rotate(-8)">
      <polygon points="-40,-25 40,-25 55,0 40,25 -40,25" fill="#FFF9F6" stroke="#806477" stroke-width="1.5"/>
      <circle cx="42" cy="0" r="4" fill="#806477"/>
      <text x="-25" y="4" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="600" fill="#292329" letter-spacing="1">HYDERABAD</text>
    </g>
'''

    # Bottom Typography and Badges
    svg += f'''
  </g>

  <!-- Tag Pill at Top -->
  <g transform="translate({width/2}, 60)">
    <rect x="-110" y="-16" width="220" height="32" rx="16" fill="#FFF9F6" stroke="#D98EAA" stroke-width="1.5" filter="url(#cardShadow)"/>
    <text x="0" y="5" text-anchor="middle" font-family="'Plus Jakarta Sans', -apple-system, sans-serif" font-size="11" font-weight="700" fill="#806477" letter-spacing="2">{tag.upper()}</text>
  </g>

  <!-- Bottom Details & Replaceable Note -->
  <g transform="translate({width/2}, {height - 85})">
    <rect x="-{width*0.42}" y="-45" width="{width*0.84}" height="90" rx="14" fill="#FFFFFF" fill-opacity="0.92" stroke="#D98EAA" stroke-width="1" filter="url(#cardShadow)"/>
    <text x="0" y="-16" text-anchor="middle" font-family="'Cormorant Garamond', Georgia, serif" font-size="24" font-weight="600" fill="#292329" letter-spacing="0.5">{title}</text>
    <text x="0" y="6" text-anchor="middle" font-family="'Plus Jakarta Sans', -apple-system, sans-serif" font-size="12" font-weight="500" fill="#806477" letter-spacing="0.5">{subtitle}</text>
    <text x="0" y="26" text-anchor="middle" font-family="'Plus Jakarta Sans', -apple-system, sans-serif" font-size="10" font-weight="600" fill="#D98EAA" letter-spacing="1.5">REPLACEABLE BRAND PHOTO PLACEHOLDER</text>
  </g>

</svg>'''
    with open(f"assets/images/{filename}", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated assets/images/{filename}")

# Generate Hero Bouquet
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1200" width="1000" height="1200">
  <defs>
    <linearGradient id="heroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF9F6"/>
      <stop offset="50%" stop-color="#F8E8ED"/>
      <stop offset="100%" stop-color="#F2DFE5"/>
    </linearGradient>
    <linearGradient id="heroRose" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EAB9CA"/>
      <stop offset="100%" stop-color="#D98EAA"/>
    </linearGradient>
    <linearGradient id="heroGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFE8A3"/>
      <stop offset="100%" stop-color="#F5B942"/>
    </linearGradient>
    <linearGradient id="heroCream" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#FBF1F3"/>
    </linearGradient>
    <filter id="heroShadow" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#806477" flood-opacity="0.18"/>
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="1000" height="1200" fill="url(#heroBg)"/>
  
  <!-- Subtle decorative circular halos -->
  <circle cx="500" cy="540" r="380" fill="#EAB9CA" opacity="0.3"/>
  <circle cx="500" cy="540" r="280" fill="#FFF9F6" opacity="0.75"/>
  <circle cx="500" cy="540" r="320" fill="none" stroke="#D98EAA" stroke-width="1.5" stroke-dasharray="6 6" opacity="0.5"/>

  <!-- Outer frame -->
  <rect x="25" y="25" width="950" height="1150" fill="none" stroke="#D98EAA" stroke-width="1.5" stroke-opacity="0.4" rx="24"/>
  <rect x="36" y="36" width="928" height="1128" fill="none" stroke="#806477" stroke-width="0.75" stroke-opacity="0.25" rx="18"/>

  <!-- Top Floating Badge -->
  <g transform="translate(500, 90)">
    <rect x="-140" y="-18" width="280" height="36" rx="18" fill="#FFFFFF" stroke="#D98EAA" stroke-width="1.5" filter="url(#heroShadow)"/>
    <text x="0" y="6" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700" fill="#806477" letter-spacing="3">HYDERABAD • HANDMADE</text>
  </g>

  <!-- Grand Floral Bouquet Group -->
  <g transform="translate(500, 560)">
    <!-- Kraft Wrapping Fold at back -->
    <path d="M-180,260 L-260,-20 L0,-90 L260,-20 L180,260 Z" fill="#F8E8ED" stroke="#D98EAA" stroke-width="3" filter="url(#heroShadow)"/>
    <path d="M-180,260 L-20,240 L-60,-20 L-260,-20 Z" fill="#F0D5DE" opacity="0.55"/>

    <!-- Lush Foliage & Eucalyptus -->
    <path d="M-160,20 Q-280,-40 -240,-130 Q-160,-70 -120,0" fill="#6B8364" opacity="0.85"/>
    <path d="M160,20 Q280,-40 240,-130 Q160,-70 120,0" fill="#7A8F74" opacity="0.85"/>
    <circle cx="-190" cy="-60" r="26" fill="#8FA489" opacity="0.7"/>
    <circle cx="-220" cy="-110" r="22" fill="#7A8F74" opacity="0.8"/>
    <circle cx="190" cy="-60" r="26" fill="#8FA489" opacity="0.7"/>
    <circle cx="220" cy="-110" r="22" fill="#7A8F74" opacity="0.8"/>

    <!-- Left Tulip Stems & Flowers -->
    <g transform="translate(-110, -70) rotate(-22)">
      <path d="M-38,30 C-55,-25 0,-100 0,-100 C0,-100 55,-25 38,30 C30,55 -30,55 -38,30 Z" fill="url(#heroRose)"/>
      <path d="M-22,25 C-38,-15 0,-85 0,-85 C0,-85 38,-15 22,25 Z" fill="#FFF9F6" opacity="0.9"/>
      <path d="M-42,15 C-55,-25 -15,-80 -15,-80 C-35,-25 -30,10 -42,15 Z" fill="#D98EAA"/>
    </g>

    <!-- Right Tulip Stems & Flowers -->
    <g transform="translate(120, -60) rotate(24)">
      <path d="M-38,30 C-55,-25 0,-100 0,-100 C0,-100 55,-25 38,30 C30,55 -30,55 -38,30 Z" fill="#EAB9CA"/>
      <path d="M-22,25 C-38,-15 0,-85 0,-85 C0,-85 38,-15 22,25 Z" fill="#FFF9F6" opacity="0.95"/>
      <path d="M15,-80 C15,-80 55,-25 42,15 C30,10 35,-25 15,-80 Z" fill="#D98EAA"/>
    </g>

    <!-- Top Cream Lily -->
    <g transform="translate(0, -170)">
      <path d="M0,0 Q-55,-75 0,-130 Q55,-75 0,0" fill="url(#heroCream)" stroke="#D98EAA" stroke-width="2"/>
      <path d="M0,0 Q-85,-40 -130,-45 Q-85,20 0,0" fill="url(#heroCream)" stroke="#D98EAA" stroke-width="2"/>
      <path d="M0,0 Q85,-40 130,-45 Q85,20 0,0" fill="url(#heroCream)" stroke="#D98EAA" stroke-width="2"/>
      <path d="M0,0 Q-70,55 -105,100 Q-40,75 0,0" fill="url(#heroCream)" stroke="#D98EAA" stroke-width="2"/>
      <path d="M0,0 Q70,55 105,100 Q40,75 0,0" fill="url(#heroCream)" stroke="#D98EAA" stroke-width="2"/>
      <!-- Stamens -->
      <path d="M0,0 Q-20,-35 -30,-70" stroke="#806477" stroke-width="2.5" fill="none"/>
      <ellipse cx="-30" cy="-70" rx="5" ry="3" fill="#D98EAA"/>
      <path d="M0,0 Q0,-40 0,-75" stroke="#806477" stroke-width="2.5" fill="none"/>
      <ellipse cx="0" cy="-75" rx="5" ry="3" fill="#D98EAA"/>
      <path d="M0,0 Q20,-35 30,-70" stroke="#806477" stroke-width="2.5" fill="none"/>
      <ellipse cx="30" cy="-70" rx="5" ry="3" fill="#D98EAA"/>
      <circle cx="0" cy="0" r="10" fill="#806477"/>
    </g>

    <!-- Center Radiant Sunflower -->
    <g transform="translate(0, 10)">
'''
for deg in range(0, 360, 20):
    hero_svg += f'''      <path d="M0,0 C-16,-35 -18,-95 0,-120 C18,-95 16,-35 0,0" fill="url(#heroGold)" transform="rotate({deg})"/>\n'''
for deg in range(10, 360, 20):
    hero_svg += f'''      <path d="M0,0 C-14,-30 -15,-80 0,-102 C15,-80 14,-30 0,0" fill="#FFB72B" transform="rotate({deg})"/>\n'''
hero_svg += '''      <!-- Seed Core -->
      <circle cx="0" cy="0" r="52" fill="#4B3322" filter="url(#heroShadow)"/>
      <circle cx="0" cy="0" r="44" fill="#6A4325"/>
      <circle cx="0" cy="0" r="32" fill="none" stroke="#DDA15E" stroke-width="3" stroke-dasharray="3 4"/>
      <circle cx="0" cy="0" r="18" fill="none" stroke="#FFE394" stroke-width="2.5" stroke-dasharray="2 3"/>
      <circle cx="0" cy="0" r="8" fill="#FFE394"/>
    </g>

    <!-- Front Blush Bouquet Tie / Giant Silk Bow -->
    <g transform="translate(0, 190)">
      <ellipse cx="-45" cy="-6" rx="48" ry="20" fill="#D98EAA" transform="rotate(-15)"/>
      <ellipse cx="45" cy="-6" rx="48" ry="20" fill="#D98EAA" transform="rotate(15)"/>
      <ellipse cx="-42" cy="-6" rx="38" ry="14" fill="#EAB9CA" transform="rotate(-15)"/>
      <ellipse cx="42" cy="-6" rx="38" ry="14" fill="#EAB9CA" transform="rotate(15)"/>
      <circle cx="0" cy="0" r="16" fill="#806477"/>
      <!-- Trailing Silk Tails -->
      <path d="M-10,10 Q-45,90 -65,150" stroke="#D98EAA" stroke-width="12" stroke-linecap="round" fill="none"/>
      <path d="M10,10 Q45,90 65,150" stroke="#D98EAA" stroke-width="12" stroke-linecap="round" fill="none"/>
      <path d="M-10,10 Q-35,80 -50,130" stroke="#806477" stroke-width="6" stroke-linecap="round" fill="none"/>
      <path d="M10,10 Q35,80 50,130" stroke="#806477" stroke-width="6" stroke-linecap="round" fill="none"/>
    </g>

  </g>

  <!-- Editorial Info Card at Bottom -->
  <g transform="translate(500, 1070)">
    <rect x="-420" y="-55" width="840" height="110" rx="18" fill="#FFFFFF" fill-opacity="0.95" stroke="#D98EAA" stroke-width="1.5" filter="url(#heroShadow)"/>
    <text x="0" y="-20" text-anchor="middle" font-family="'Cormorant Garamond', Georgia, serif" font-size="30" font-weight="600" fill="#292329" letter-spacing="1">Signature Forever Bouquet</text>
    <text x="0" y="8" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="500" fill="#806477" letter-spacing="0.5">Handcrafted Petal by Petal in Hyderabad, India</text>
    <text x="0" y="32" text-anchor="middle" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700" fill="#D98EAA" letter-spacing="2">REPLACEABLE BRAND PHOTO PLACEHOLDER • 1000 x 1200</text>
  </g>

</svg>'''

with open("assets/images/hero-bouquet.svg", "w", encoding="utf-8") as f:
    f.write(hero_svg)
print("Generated assets/images/hero-bouquet.svg")

# Collections
create_editorial_card("collection-tulips.svg", 800, 1000, "Handmade Tulips", "Graceful, slender blooms sculpted for timeless elegance", "tulips", "Signature Collection")
create_editorial_card("collection-lilies.svg", 800, 1000, "Handmade Lilies", "Majestic curves, pure devotion, and enduring beauty", "lilies", "Signature Collection")
create_editorial_card("collection-sunflowers.svg", 800, 1000, "Handmade Sunflowers", "Golden radiance, warmth, and joyful handmade charm", "sunflowers", "Signature Collection")
create_editorial_card("collection-custom.svg", 800, 1000, "Custom Bouquets", "Your personal choice of blooms, hues, and wrapping", "custom", "Bespoke Service")
create_editorial_card("collection-special.svg", 800, 1000, "Special Arrangements", "Statement floral keepsakes crafted for unforgettable days", "special", "Exclusive Creations")

# Our Story
create_editorial_card("story-floral.svg", 1000, 800, "The Hyderabad Atelier", "Crafting meaningful forever gifts with love and precision", "story", "Our Hyderabad Story")

# Instagram Gallery (6 square images 800x800)
insta_details = [
    ("insta-1.svg", "Delicate Tulip Petals", "Handmade Pastel Blooms", "tulips", "@floral.flirtss"),
    ("insta-2.svg", "Radiant Golden Sunflowers", "Warmth that Lasts Forever", "sunflowers", "@floral.flirtss"),
    ("insta-3.svg", "Bespoke Mixed Arrangement", "Curated for a Hyderabad Celebration", "custom", "@floral.flirtss"),
    ("insta-4.svg", "Cream & Blush Lilies", "Pure Elegance in Every Petal", "lilies", "@floral.flirtss"),
    ("insta-5.svg", "Gift Packaging Keepsake", "Handmade Details & Wax Seals", "special", "@floral.flirtss"),
    ("insta-6.svg", "Artisan Studio Moments", "Crafted Petal by Petal in Hyderabad", "story", "@floral.flirtss")
]

for filename, title, sub, ftype, tag in insta_details:
    create_editorial_card(filename, 800, 800, title, sub, ftype, tag)

print("All SVG assets successfully generated!")
