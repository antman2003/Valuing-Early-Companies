"""
Generate a simple ebook cover for:

Title:  Valuing Early Companies
Subtitle: A practical guide for startup and early company investors

The script creates a JPEG file `cover_valuing_early_companies.jpg` in the
project root, sized appropriately for Kindle/ebook use.
"""

import os

from PIL import Image, ImageDraw, ImageFont


def get_project_root() -> str:
    """Return the project root directory (one level above this script)."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_font(preferred: str, size: int) -> ImageFont.FreeTypeFont:
    """
    Try to load a TrueType font, fall back to the default bitmap font if needed.
    """
    try:
        return ImageFont.truetype(preferred, size)
    except Exception:
        return ImageFont.load_default()


def create_cover() -> str:
    """
    Create the cover image and return the output path.
    """
    root = get_project_root()
    width, height = 2560, 1600  # 16:10 landscape commonly accepted by KDP

    # Background: dark blue gradient-style block
    base_color = (10, 34, 64)  # deep blue
    accent_color = (32, 102, 148)  # lighter blue accent

    img = Image.new("RGB", (width, height), color=base_color)
    draw = ImageDraw.Draw(img)

    # Simple diagonal accent band on the right
    draw.rectangle(
        [int(width * 0.55), 0, width, height], fill=accent_color
    )

    # Add a stylised "growth chart" motif in the accent area to evoke early companies
    # Position the chart lower and more to the right so it does not clash
    # with the title/subtitle area on the left.
    chart_margin_x = int(width * 0.65)
    chart_margin_y = int(height * 0.30)
    chart_width = int(width * 0.40)
    chart_height = int(height * 0.40)

    # Axes
    axis_color = (220, 235, 250)
    draw.line(
        [(chart_margin_x, chart_margin_y + chart_height),
         (chart_margin_x, chart_margin_y)],
        fill=axis_color,
        width=4,
    )
    draw.line(
        [(chart_margin_x, chart_margin_y + chart_height),
         (chart_margin_x + chart_width, chart_margin_y + chart_height)],
        fill=axis_color,
        width=4,
    )

    # Stylised revenue bars (early low bars, then higher growth bars)
    num_bars = 5
    bar_spacing = chart_width // (num_bars + 2)
    bar_width = int(bar_spacing * 0.6)
    max_bar_height = int(chart_height * 0.85)
    bar_base_y = chart_margin_y + chart_height

    bar_colors = [
        (190, 210, 240),
        (175, 205, 235),
        (160, 200, 230),
        (145, 195, 225),
        (130, 190, 220),
    ]

    # Bar heights roughly increasing in a convex fashion (representing acceleration)
    bar_height_factors = [0.15, 0.30, 0.50, 0.72, 0.92]

    bar_centers = []
    for i in range(num_bars):
        center_x = chart_margin_x + bar_spacing * (i + 1)
        bar_centers.append(center_x)
        bh = int(max_bar_height * bar_height_factors[i])
        x0 = center_x - bar_width // 2
        y0 = bar_base_y - bh
        x1 = center_x + bar_width // 2
        y1 = bar_base_y
        draw.rectangle([x0, y0, x1, y1], fill=bar_colors[i])

    # A smooth growth line running over the tops of the bars
    line_points = []
    for i, center_x in enumerate(bar_centers):
        bh = int(max_bar_height * bar_height_factors[i])
        y = bar_base_y - bh
        # Lift the last point slightly to emphasise upside
        if i == len(bar_centers) - 1:
            y = int(y - chart_height * 0.06)
        line_points.append((center_x, y))

    growth_line_color = (255, 255, 255)
    if len(line_points) >= 2:
        draw.line(line_points, fill=growth_line_color, width=4)
        # Add small markers at each point
        for (cx, cy) in line_points:
            r = 10
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=growth_line_color)

    title = "Valuing Early Companies"
    subtitle = "A practical guide for startup and early company investors"
    author = "Silicon Valley Wolf"  # Optional: add your name here later if you wish

    # Load fonts (fall back to default if specific fonts are not available)
    title_font = load_font("arial.ttf", 120)
    subtitle_font = load_font("arial.ttf", 60)
    author_font = load_font("arial.ttf", 48)

    # Compute text positions
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]

    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_height = subtitle_bbox[3] - subtitle_bbox[1]

    # Center text in the left two-thirds of the cover
    center_x = int(width * 0.35)
    title_x = center_x - title_width // 2
    title_y = int(height * 0.30) - title_height // 2

    subtitle_x = center_x - subtitle_width // 2
    subtitle_y = title_y + title_height + 60

    # Text colors
    main_text_color = (240, 245, 250)  # near-white
    subtitle_text_color = (210, 225, 240)

    # Draw text with a very subtle shadow for legibility
    shadow_offset = 3
    shadow_color = (0, 0, 0)

    # Title shadow and text
    draw.text(
        (title_x + shadow_offset, title_y + shadow_offset),
        title,
        font=title_font,
        fill=shadow_color,
    )
    draw.text(
        (title_x, title_y),
        title,
        font=title_font,
        fill=main_text_color,
    )

    # Subtitle shadow and text
    draw.text(
        (subtitle_x + shadow_offset, subtitle_y + shadow_offset),
        subtitle,
        font=subtitle_font,
        fill=shadow_color,
    )
    draw.text(
        (subtitle_x, subtitle_y),
        subtitle,
        font=subtitle_font,
        fill=subtitle_text_color,
    )

    # Optional author name at the bottom-left (empty for now)
    if author:
        author_bbox = draw.textbbox((0, 0), author, font=author_font)
        author_width = author_bbox[2] - author_bbox[0]
        author_height = author_bbox[3] - author_bbox[1]
        author_x = int(width * 0.08)
        author_y = height - author_height - 120
        draw.text(
            (author_x + shadow_offset, author_y + shadow_offset),
            author,
            font=author_font,
            fill=shadow_color,
        )
        draw.text(
            (author_x, author_y),
            author,
            font=author_font,
            fill=main_text_color,
        )

    output_path = os.path.join(root, "cover_valuing_early_companies.jpg")
    img.save(output_path, format="JPEG", quality=95)
    return output_path


def main() -> None:
    path = create_cover()
    print(f"Cover image saved to: {path}")


if __name__ == "__main__":
    main()


