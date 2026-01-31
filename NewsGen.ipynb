# ============================================
# 🇳🇵 ULTIMATE TikTok & Instagram News Generator
# Google Colab Version with ALL Features
# ============================================
import subprocess
import sys
import os
import requests
import re
import random
import csv
from datetime import datetime
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from bs4 import BeautifulSoup

# ============================================
# INSTALLATION & SETUP
# ============================================

def install_dependencies_and_fonts():
    """Install all required dependencies and fonts"""
    packages = ["moviepy", "requests", "beautifulsoup4", "pillow"]
    print("📦 Installing required packages...")
    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "-q"])
            print(f"✅ {package} installed.")
        except Exception as e:
            print(f"❌ Failed to install {package}: {e}")

    # Download Nepali Font
    font_url = "https://github.com/googlefonts/noto-fonts/raw/main/hinted/ttf/NotoSansDevanagari/NotoSansDevanagari-Bold.ttf"
    font_path = "NepaliFont.ttf"
    if not os.path.exists(font_path):
        print("📥 Downloading Nepali font...")
        try:
            r = requests.get(font_url, allow_redirects=True)
            with open(font_path, 'wb') as f:
                f.write(r.content)
            print("✅ Nepali font downloaded successfully.")
        except Exception as e:
            print(f"❌ Failed to download font: {e}")
    return font_path

# --- Environment Setup ---
try:
    import google.colab
    NEPALI_FONT_PATH = install_dependencies_and_fonts()
    from google.colab import drive
    drive.mount('/content/drive')
    OUTPUT_FOLDER = '/content/drive/MyDrive/TikTok_Videos'
    IS_COLAB = True
except ImportError:
    NEPALI_FONT_PATH = "NepaliFont.ttf"
    OUTPUT_FOLDER = 'output_videos'
    IS_COLAB = False

# --- MoviePy Imports ---
MOVIEPY_V2 = False
try:
    from moviepy.video.VideoClip import ImageClip
    MOVIEPY_V2 = True
    print("ℹ️ Detected MoviePy v2.x")
except ImportError:
    try:
        from moviepy.editor import ImageClip
        MOVIEPY_V2 = False
        print("ℹ️ Detected MoviePy v1.x")
    except ImportError:
        print("❌ Error: Could not import MoviePy.")
        sys.exit(1)

# ============================================
# CONFIGURATION
# ============================================
TARGET_WIDTH = 1080 
TARGET_HEIGHT = 1920
VIDEO_DURATION_OPTIONS = {
    "1": {"name": "Quick (5s)", "duration": 5},
    "2": {"name": "Short (10s)", "duration": 10},
    "3": {"name": "Medium (15s)", "duration": 15},
    "4": {"name": "Long (30s)", "duration": 30}
}

# Multiple Color Themes
COLOR_THEMES = {
    "1": {"name": "Nepal Red", "color": "#E31E24", "title_color": "#E31E24"},
    "2": {"name": "Blue", "color": "#1E90FF", "title_color": "#1E90FF"},
    "3": {"name": "Green", "color": "#32CD32", "title_color": "#32CD32"},
    "4": {"name": "Orange", "color": "#FF8C00", "title_color": "#FF8C00"},
    "5": {"name": "Purple", "color": "#9370DB", "title_color": "#9370DB"},
    "6": {"name": "Pink", "color": "#FF1493", "title_color": "#FF1493"},
    "7": {"name": "Gold", "color": "#FFD700", "title_color": "#FFD700"},
    "8": {"name": "Teal", "color": "#20B2AA", "title_color": "#20B2AA"},
}

# News Sources by Category
NEWS_SOURCES = {
    "all": [
        "https://www.onlinekhabar.com/",
        "https://ekantipur.com/",
        "https://www.setopati.com/",
        "https://ratopati.com/",
        "https://www.deshsanchar.com/",
    ],
    "politics": [
        "https://www.onlinekhabar.com/content/politics",
        "https://ekantipur.com/politics",
    ],
    "sports": [
        "https://www.onlinekhabar.com/content/sports",
        "https://ekantipur.com/sports",
    ],
    "entertainment": [
        "https://www.onlinekhabar.com/content/entertainment",
        "https://ekantipur.com/entertainment",
    ],
}

# Analytics Log
ANALYTICS_FILE = os.path.join(OUTPUT_FOLDER, "analytics_log.csv")

# ============================================
# UTILITY FUNCTIONS
# ============================================

def log_analytics(data):
    """Log content generation to CSV"""
    file_exists = os.path.exists(ANALYTICS_FILE)
    try:
        with open(ANALYTICS_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['timestamp', 'title', 'source', 'color', 'duration', 'layout', 'hashtags'])
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)
    except Exception as e:
        print(f"⚠️ Could not log analytics: {e}")

def extract_article_content(url):
    """Extract title, description, and image from a news URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title = None
        og_title = soup.find('meta', property='og:title')
        if og_title: 
            title = og_title.get('content')
        if not title:
            h1 = soup.find('h1')
            if h1: 
                title = h1.get_text(strip=True)
        if not title:
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.get_text(strip=True)
        title = title if title else "News Update"

        # Extract image
        image_url = None
        og_image = soup.find('meta', property='og:image')
        if og_image: 
            image_url = og_image.get('content')
        if not image_url:
            twitter_image = soup.find('meta', attrs={'name': 'twitter:image'})
            if twitter_image:
                image_url = twitter_image.get('content')
        if not image_url:
            images = soup.find_all('img')
            for img in images:
                src = img.get('src')
                if src and (src.startswith('http') or src.startswith('//')):
                    if 'logo' not in src.lower() and 'icon' not in src.lower():
                        image_url = src if src.startswith('http') else 'https:' + src
                        break

        # Extract description
        description = None
        og_desc = soup.find('meta', property='og:description')
        if og_desc: 
            description = og_desc.get('content')
        if not description:
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                description = meta_desc.get('content')
        if not description:
            paragraphs = soup.find_all('p')
            for p in paragraphs:
                text = p.get_text(strip=True)
                if len(text) > 50:
                    description = text
                    break
        
        description = description if description else ""
        
        return {
            'title': title, 
            'description': description, 
            'image_url': image_url
        }
    except Exception as e:
        print(f"⚠️ Extraction error: {e}")
        return None

def scrape_articles(category="all", limit=20):
    """Scrape articles from news sources"""
    print(f"\n🔍 Scanning {category} news...")
    articles = []
    sources = NEWS_SOURCES.get(category, NEWS_SOURCES["all"])
    
    for source in sources:
        try:
            print(f"📰 Checking: {source}")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(source, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            links = soup.find_all('a', href=True)
            
            for link in links[:limit]:
                href = link.get('href')
                
                if not href.startswith('http'):
                    if href.startswith('/'):
                        href = source.rstrip('/') + href
                    else:
                        continue
                
                if any(skip in href.lower() for skip in ['category', 'tag', 'author', 'page', 'search', '#', 'javascript']):
                    continue
                
                title = link.get_text(strip=True)
                
                if title and len(title) > 20:
                    articles.append({
                        'url': href,
                        'title': title,
                        'source': source
                    })
                    
        except Exception as e:
            print(f"⚠️ Error: {e}")
            continue
    
    # Remove duplicates
    seen = set()
    unique_articles = []
    for article in articles:
        if article['url'] not in seen:
            seen.add(article['url'])
            unique_articles.append(article)
    
    print(f"✅ Found {len(unique_articles)} articles")
    return unique_articles

def generate_trending_hashtags(platform="tiktok", topic=""):
    """Generate trending hashtags"""
    base_tags = {
        "tiktok": ["#NepalNews", "#TrendingNepal", "#NewsUpdate", "#TikTokNepal", "#ViralNews",
                   "#BreakingNews", "#Samachar", "#LatestUpdate", "#Nepal", "#DailyNews"],
        "instagram": ["#NepalNews", "#NewsNepal", "#Nepal", "#Kathmandu", "#NepalToday",
                      "#BreakingNews", "#Samachar", "#LatestNews", "#NewsUpdate", "#CurrentAffairs", 
                      "#NepalUpdates", "#NepalDaily", "#InstagramNepal", "#NepalGram", "#NepaliBlogger"]
    }
    
    tags = base_tags.get(platform, base_tags["tiktok"])
    
    # Add topic-specific tags
    if "politics" in topic.lower():
        tags.extend(["#NepalPolitics", "#राजनीति"])
    elif "sports" in topic.lower():
        tags.extend(["#NepalSports", "#खेलकुद"])
    elif "entertainment" in topic.lower():
        tags.extend(["#NepalEntertainment", "#मनोरञ्जन"])
    
    return " ".join(random.sample(tags, min(8 if platform == "instagram" else 5, len(tags))))

def download_image(url):
    """Download and return image from URL"""
    try:
        if not url: 
            return None
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        img = Image.open(BytesIO(res.content)).convert('RGB')
        return img
    except Exception as e:
        print(f"⚠️ Failed to download image: {e}")
        return None

def wrap_text(text, font, max_width, draw):
    """Wrap text to fit within max_width"""
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] > max_width:
            if current_line: 
                lines.append(' '.join(current_line))
            current_line = [word]
        else:
            current_line.append(word)
    
    if current_line: 
        lines.append(' '.join(current_line))
    
    return lines

def add_watermark(image, watermark_text, position="bottom-right"):
    """Add watermark to image"""
    draw = ImageDraw.Draw(image)
    
    try:
        # Use a smaller font for watermark
        font = ImageFont.truetype(NEPALI_FONT_PATH, 30)
    except:
        font = ImageFont.load_default()
    
    # Calculate position
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    margin = 20
    
    if position == "bottom-right":
        x = TARGET_WIDTH - text_width - margin
        y = TARGET_HEIGHT - text_height - margin
    elif position == "bottom-left":
        x = margin
        y = TARGET_HEIGHT - text_height - margin
    elif position == "top-right":
        x = TARGET_WIDTH - text_width - margin
        y = margin
    else:  # top-left
        x = margin
        y = margin
    
    # Add semi-transparent background
    padding = 10
    draw.rectangle([x - padding, y - padding, x + text_width + padding, y + text_height + padding],
                   fill=(0, 0, 0, 180))
    
    # Draw watermark
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 255))
    
    return image

# ============================================
# LAYOUT FUNCTIONS
# ============================================

def create_layout_1(content, news_image, color_scheme, watermark=""):
    """Layout 1: Image top, text bottom (Elegant)"""
    canvas = Image.new('RGB', (TARGET_WIDTH, TARGET_HEIGHT), '#000000')
    
    if news_image:
        bg = news_image.copy().resize((TARGET_WIDTH, TARGET_HEIGHT), Image.Resampling.LANCZOS)
        bg = bg.filter(ImageFilter.GaussianBlur(radius=50))
        bg = ImageEnhance.Brightness(bg).enhance(0.15)
        canvas.paste(bg, (0, 0))
    
    draw = ImageDraw.Draw(canvas)
    top_margin = 80
    sidebar_start = int(TARGET_HEIGHT * 0.65)
    
    if news_image:
        img_w, img_h = news_image.size
        available_h = sidebar_start - top_margin - 100
        target_w = TARGET_WIDTH - 80
        target_h = int(target_w * (img_h / img_w))
        
        if target_h > available_h:
            target_h = available_h
            target_w = int(target_h * (img_w / img_h))
        
        news_img = news_image.resize((target_w, target_h), Image.Resampling.LANCZOS)
        img_x = (TARGET_WIDTH - target_w) // 2
        img_y = top_margin
        
        border_width = 8
        border_img = Image.new('RGB', (target_w + border_width*2, target_h + border_width*2), 'white')
        border_img.paste(news_img, (border_width, border_width))
        canvas.paste(border_img, (img_x - border_width, img_y - border_width))

    sidebar_x = 80
    sidebar_width = 12
    sidebar_height = 280
    
    shadow_offset = 3
    draw.rectangle([sidebar_x + shadow_offset, sidebar_start + shadow_offset, 
                   sidebar_x + sidebar_width + shadow_offset, 
                   sidebar_start + sidebar_height + shadow_offset], fill="#00000088")
    
    draw.rectangle([sidebar_x, sidebar_start, sidebar_x + sidebar_width, 
                   sidebar_start + sidebar_height // 2], fill=color_scheme['color'])
    draw.rectangle([sidebar_x, sidebar_start + sidebar_height // 2, 
                   sidebar_x + sidebar_width, sidebar_start + sidebar_height], fill="white")
    
    text_x_start = sidebar_x + 50
    max_text_width = TARGET_WIDTH - text_x_start - 80
    
    try:
        title_size, desc_size = 68, 42
        if os.path.exists(NEPALI_FONT_PATH):
            title_font = ImageFont.truetype(NEPALI_FONT_PATH, title_size)
            desc_font = ImageFont.truetype(NEPALI_FONT_PATH, desc_size)
        else:
            title_font = ImageFont.load_default()
            desc_font = ImageFont.load_default()
    except:
        title_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
    
    title_lines = wrap_text(content['title'], title_font, max_text_width, draw)
    y_cursor = sidebar_start - 20
    
    shadow_offset = 2
    for line in title_lines:
        draw.text((text_x_start + shadow_offset, y_cursor + shadow_offset), 
                 line, font=title_font, fill="#00000088")
        draw.text((text_x_start, y_cursor), 
                 line, font=title_font, fill=color_scheme['title_color'])
        y_cursor += int(title_size * 1.3)
    
    y_cursor += 40
    desc_text = content['description']
    desc_words = desc_text.split()[:30]
    desc_display = ' '.join(desc_words) + ("..." if len(content['description'].split()) > 30 else "")
    desc_lines = wrap_text(desc_display, desc_font, max_text_width, draw)
    
    for line in desc_lines:
        draw.text((text_x_start + 1, y_cursor + 1), 
                 line, font=desc_font, fill="#00000066")
        draw.text((text_x_start, y_cursor), 
                 line, font=desc_font, fill="white")
        y_cursor += int(desc_size * 1.4)
    
    # Add watermark
    if watermark:
        canvas = add_watermark(canvas, watermark, "bottom-right")
        
    return canvas

def create_layout_2(content, news_image, color_scheme, watermark=""):
    """Layout 2: Full background image with overlay text"""
    canvas = Image.new('RGB', (TARGET_WIDTH, TARGET_HEIGHT), '#000000')
    
    if news_image:
        bg = news_image.copy().resize((TARGET_WIDTH, TARGET_HEIGHT), Image.Resampling.LANCZOS)
        bg = ImageEnhance.Brightness(bg).enhance(0.4)
        canvas.paste(bg, (0, 0))
    
    # Add gradient overlay
    overlay = Image.new('RGBA', (TARGET_WIDTH, TARGET_HEIGHT), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    for i in range(TARGET_HEIGHT):
        alpha = int(255 * (i / TARGET_HEIGHT) * 0.7)
        draw_overlay.rectangle([0, i, TARGET_WIDTH, i+1], fill=(0, 0, 0, alpha))
    canvas.paste(overlay, (0, 0), overlay)
    
    draw = ImageDraw.Draw(canvas)
    
    try:
        title_size, desc_size = 72, 48
        if os.path.exists(NEPALI_FONT_PATH):
            title_font = ImageFont.truetype(NEPALI_FONT_PATH, title_size)
            desc_font = ImageFont.truetype(NEPALI_FONT_PATH, desc_size)
        else:
            title_font = ImageFont.load_default()
            desc_font = ImageFont.load_default()
    except:
        title_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
    
    # Center text vertically
    text_start_y = int(TARGET_HEIGHT * 0.6)
    margin = 60
    max_text_width = TARGET_WIDTH - (margin * 2)
    
    title_lines = wrap_text(content['title'], title_font, max_text_width, draw)
    y_cursor = text_start_y
    
    for line in title_lines:
        # Shadow
        draw.text((margin + 3, y_cursor + 3), line, font=title_font, fill="#000000")
        # Text
        draw.text((margin, y_cursor), line, font=title_font, fill=color_scheme['title_color'])
        y_cursor += int(title_size * 1.3)
    
    y_cursor += 40
    desc_text = ' '.join(content['description'].split()[:25]) + "..."
    desc_lines = wrap_text(desc_text, desc_font, max_text_width, draw)
    
    for line in desc_lines:
        draw.text((margin + 2, y_cursor + 2), line, font=desc_font, fill="#000000")
        draw.text((margin, y_cursor), line, font=desc_font, fill="white")
        y_cursor += int(desc_size * 1.4)
    
    if watermark:
        canvas = add_watermark(canvas, watermark, "bottom-right")
        
    return canvas

def create_layout_3(content, news_image, color_scheme, watermark=""):
    """Layout 3: Minimalist - Clean text with small image"""
    canvas = Image.new('RGB', (TARGET_WIDTH, TARGET_HEIGHT), '#1a1a1a')
    
    draw = ImageDraw.Draw(canvas)
    
    # Add small image at top if available
    if news_image:
        img_size = 400
        news_img = news_image.copy()
        news_img.thumbnail((img_size, img_size), Image.Resampling.LANCZOS)
        
        img_x = (TARGET_WIDTH - news_img.width) // 2
        img_y = 150
        
        # Circular mask
        mask = Image.new('L', (news_img.width, news_img.height), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse([0, 0, news_img.width, news_img.height], fill=255)
        
        canvas.paste(news_img, (img_x, img_y), mask)
    
    try:
        title_size, desc_size = 65, 40
        if os.path.exists(NEPALI_FONT_PATH):
            title_font = ImageFont.truetype(NEPALI_FONT_PATH, title_size)
            desc_font = ImageFont.truetype(NEPALI_FONT_PATH, desc_size)
        else:
            title_font = ImageFont.load_default()
            desc_font = ImageFont.load_default()
    except:
        title_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
    
    # Draw colored line
    line_y = 650
    draw.rectangle([100, line_y, TARGET_WIDTH - 100, line_y + 5], fill=color_scheme['color'])
    
    # Title
    text_start_y = line_y + 60
    margin = 80
    max_text_width = TARGET_WIDTH - (margin * 2)
    
    title_lines = wrap_text(content['title'], title_font, max_text_width, draw)
    y_cursor = text_start_y
    
    for line in title_lines:
        draw.text((margin, y_cursor), line, font=title_font, fill=color_scheme['title_color'])
        y_cursor += int(title_size * 1.3)
    
    # Description
    y_cursor += 50
    desc_text = ' '.join(content['description'].split()[:35]) + "..."
    desc_lines = wrap_text(desc_text, desc_font, max_text_width, draw)
    
    for line in desc_lines:
        draw.text((margin, y_cursor), line, font=desc_font, fill="#cccccc")
        y_cursor += int(desc_size * 1.4)
    
    if watermark:
        canvas = add_watermark(canvas, watermark, "bottom-right")
        
    return canvas

LAYOUTS = {
    "1": {"name": "Elegant (Image Top)", "function": create_layout_1},
    "2": {"name": "Full Background", "function": create_layout_2},
    "3": {"name": "Minimalist Clean", "function": create_layout_3},
}

# ============================================
# CONTENT GENERATION
# ============================================

def generate_content(article, color_scheme, video_duration, layout_func, watermark, output_folder):
    """Generate video and image from article"""
    print(f"\n{'='*70}")
    print(f"📰 Processing: {article['title'][:60]}...")
    print(f"{'='*70}")
    
    content = extract_article_content(article['url'])
    if not content:
        print("❌ Failed to extract content")
        return None
    
    print(f"✅ Extracted content")
    
    img = download_image(content['image_url'])
    
    print(f"🖼️ Creating frame with {layout_func.__name__}...")
    frame = layout_func(content, img, color_scheme, watermark)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save JPG for Instagram
    jpg_filename = f"news_instagram_{timestamp}.jpg"
    jpg_path = os.path.join(output_folder, jpg_filename)
    frame.save(jpg_path, quality=95, optimize=True)
    print(f"✅ Instagram JPG: {jpg_filename}")
    
    # Save temp frame for video
    temp_frame = f"temp_frame_{timestamp}.jpg"
    frame.save(temp_frame, quality=95)
    
    # Create video
    print(f"🎬 Rendering {video_duration}s video...")
    try:
        if MOVIEPY_V2:
            video = ImageClip(temp_frame, duration=video_duration)
        else:
            video = ImageClip(temp_frame).set_duration(video_duration)
        
        video_filename = f"news_tiktok_{timestamp}.mp4"
        video_path = os.path.join(output_folder, video_filename)
        
        logger_val = None if MOVIEPY_V2 else 'bar'
        video.write_videofile(video_path, fps=30, codec='libx264', 
                            bitrate="4000k", logger=logger_val, verbose=False, audio=False)
        video.close()
        print(f"✅ TikTok video: {video_filename}")
    except Exception as e:
        print(f"❌ Video creation failed: {e}")
        if os.path.exists(temp_frame):
            os.remove(temp_frame)
        return None
    
    # Generate captions
    tiktok_hashtags = generate_trending_hashtags("tiktok", content['title'])
    instagram_hashtags = generate_trending_hashtags("instagram", content['title'])
    
    desc_tiktok = ' '.join(content['description'].split()[:40])
    desc_instagram = ' '.join(content['description'].split()[:30])
    
    caption_text = f"""{'='*70}
📱 SOCIAL MEDIA CAPTIONS
{'='*70}

🎵 TIKTOK CAPTION:
{content['title']}

{desc_tiktok}...

{tiktok_hashtags}

{'─'*70}

📸 INSTAGRAM CAPTION:
{content['title']}

{desc_instagram}...

{instagram_hashtags}

{'='*70}
"""
    
    # Save caption file
    caption_filename = f"news_{timestamp}_CAPTIONS.txt"
    caption_path = os.path.join(output_folder, caption_filename)
    with open(caption_path, 'w', encoding='utf-8') as f:
        f.write(caption_text)
    print(f"✅ Captions: {caption_filename}")
    
    # Cleanup
    if os.path.exists(temp_frame):
        os.remove(temp_frame)
    
    # Log analytics
    log_analytics({
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'title': content['title'][:100],
        'source': article['source'],
        'color': color_scheme['name'],
        'duration': video_duration,
        'layout': layout_func.__name__,
        'hashtags': tiktok_hashtags
    })
    
    return {
        'video': video_path,
        'image': jpg_path,
        'caption': caption_path,
        'tiktok_caption': f"{content['title']}\n\n{desc_tiktok}...\n\n{tiktok_hashtags}",
        'instagram_caption': f"{content['title']}\n\n{desc_instagram}...\n\n{instagram_hashtags}"
    }

# ============================================
# MAIN MENU & WORKFLOW
# ============================================

def main():
    """Main execution function"""
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    print("\n" + "="*70)
    print("🇳🇵 ULTIMATE TikTok & Instagram News Generator")
    print("="*70 + "\n")
    
    # Step 1: Choose category
    print("📂 STEP 1: Choose News Category")
    print("="*70)
    print("1. All News (Default)")
    print("2. Politics")
    print("3. Sports")
    print("4. Entertainment")
    print("="*70)
    category_choice = input("\nChoose category (1-4) [default: 1]: ").strip() or "1"
    category_map = {"1": "all", "2": "politics", "3": "sports", "4": "entertainment"}
    category = category_map.get(category_choice, "all")
    
    # Step 2: Scrape and select articles
    articles = scrape_articles(category, limit=30)
    
    if not articles:
        print("❌ No articles found")
        return
    
    print(f"\n📰 STEP 2: Select Articles")
    print("="*70)
    for i, article in enumerate(articles[:20], 1):
        print(f"{i}. {article['title'][:70]}...")
    print("="*70)
    
    selection = input("\nEnter article numbers (e.g., 1,3,5 or 1-5 or 'all' for first 5): ").strip()
    
    selected_articles = []
    if selection.lower() == 'all':
        selected_articles = articles[:5]
    elif '-' in selection:
        start, end = map(int, selection.split('-'))
        selected_articles = articles[start-1:end]
    else:
        indices = [int(x.strip())-1 for x in selection.split(',')]
        selected_articles = [articles[i] for i in indices if i < len(articles)]
    
    print(f"\n✅ Selected {len(selected_articles)} articles")
    
    # Step 3: Choose color theme
    print(f"\n🎨 STEP 3: Choose Color Theme")
    print("="*70)
    for key, theme in COLOR_THEMES.items():
        print(f"{key}. {theme['name']}")
    print("9. Use different color for each article")
    print("="*70)
    color_choice = input("\nChoose color (1-9) [default: 1]: ").strip() or "1"
    
    use_different_colors = color_choice == "9"
    default_color = COLOR_THEMES.get(color_choice, COLOR_THEMES["1"])
    
    # Step 4: Choose video duration
    print(f"\n⏱️ STEP 4: Choose Video Duration")
    print("="*70)
    for key, duration in VIDEO_DURATION_OPTIONS.items():
        print(f"{key}. {duration['name']}")
    print("="*70)
    duration_choice = input("\nChoose duration (1-4) [default: 2]: ").strip() or "2"
    video_duration = VIDEO_DURATION_OPTIONS.get(duration_choice, VIDEO_DURATION_OPTIONS["2"])['duration']
    
    # Step 5: Choose layout
    print(f"\n🎨 STEP 5: Choose Layout Style")
    print("="*70)
    for key, layout in LAYOUTS.items():
        print(f"{key}. {layout['name']}")
    print("4. Use different layout for each article")
    print("="*70)
    layout_choice = input("\nChoose layout (1-4) [default: 1]: ").strip() or "1"
    
    use_different_layouts = layout_choice == "4"
    default_layout = LAYOUTS.get(layout_choice, LAYOUTS["1"])['function']
    
    # Step 6: Watermark
    print(f"\n💧 STEP 6: Add Watermark (Optional)")
    print("="*70)
    watermark = input("Enter watermark text (or press Enter to skip): ").strip()
    
    # Generate content
    print(f"\n🚀 GENERATING CONTENT...")
    print("="*70)
    
    results = []
    for i, article in enumerate(selected_articles):
        print(f"\n[{i+1}/{len(selected_articles)}] Processing...")
        
        # Select color
        if use_different_colors:
            color = random.choice(list(COLOR_THEMES.values()))
        else:
            color = default_color
        
        # Select layout
        if use_different_layouts:
            layout = random.choice(list(LAYOUTS.values()))['function']
        else:
            layout = default_layout
        
        result = generate_content(article, color, video_duration, layout, watermark, OUTPUT_FOLDER)
        if result:
            results.append(result)
    
    # Summary
    print(f"\n" + "="*70)
    print(f"✅ GENERATION COMPLETE!")
    print("="*70)
    print(f"\n📊 Summary:")
    print(f"   ✅ Generated: {len(results)} videos")
    print(f"   📁 Location: {OUTPUT_FOLDER}")
    print(f"   📈 Analytics: {ANALYTICS_FILE}")
    
    print(f"\n📝 Files Generated:")
    for i, result in enumerate(results, 1):
        print(f"\n   [{i}]")
        print(f"   🎬 Video: {os.path.basename(result['video'])}")
        print(f"   📸 Image: {os.path.basename(result['image'])}")
        print(f"   📝 Caption: {os.path.basename(result['caption'])}")
    
    print(f"\n" + "="*70)
    print("🎉 All files saved to Google Drive!")
    print("="*70 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Process interrupted by user")
    except Exception as e:
        print(f"\n\n❌ An error occurred: {e}")
        import traceback
        traceback.print_exc()