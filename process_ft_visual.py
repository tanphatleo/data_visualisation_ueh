import os
import re

root = r'd:\projects\datat_visualisation\day_1\ft_visual_vacab'

color_replace_map = {
    '#E5B023': '#0D1A63', '#E4AF23': '#0D1A63', '#9C9D94': '#0D1A63', 
    '#E0CBDB': '#F68048', '#F26522': '#0D1A63', '#0054A6': '#0D1A63', 
    '#A3488C': '#0D1A63', '#C9A0BD': '#F68048', '#008EB0': '#0D1A63', 
    '#977348': '#0D1A63', '#ABBD67': '#0D1A63', '#28903B': '#0D1A63'
}

slides_md = ""

categories = [
    'deviation', 'correlation', 'change_v_time', 'ranking', 
    'distribution', 'part_of_whole', 'magnitude', 'spatial', 'flow'
]

for cat_dir in categories:
    dir_path = os.path.join(root, cat_dir)
    html_path = os.path.join(dir_path, 'Visual Vocabulary.html')
    if not os.path.exists(html_path):
        continue
    
    html = open(html_path, encoding='utf-8').read()
    
    # Extract charts
    # HTML structure: 
    # <div class="chart" style="max-width: ...">
    #   <div class="chart" style="height:55px">Chart Name</div>
    #   <img class="chart" ... src="icons/chart.svg" ...>
    #   <div class="chartDesc">Chart Desc</div>
    # </div>
    
    # First, let's just get the raw chart blocks
    # Looking at the dump, the outer div is <div class="chart" style="max-width: 156.667px;">
    # Inside it there are 3 things: 
    # <div class="chart" style="height: 55px;">line</div>
    # <img class="chart" style="..." src="icons/line.svg" ...>
    # <div class="chartDesc">...</div>
    
    # We can split the HTML by '<div class="chart" style="max-width:'
    parts = html.split('<div class="chart" style="max-width:')
    chart_blocks = parts[1:] # discard the first part
    
    charts = []
    for block in chart_blocks:
        name_match = re.search(r'<div class="chart" style="height:\s*55px;">(.*?)</div>', block)
        img_match = re.search(r'<img.*?src=".*?([^/]+\.svg)".*?>', block)
        desc_match = re.search(r'<div class="chartDesc">(.*?)</div>', block)
        
        if name_match and img_match:
            name = name_match.group(1).strip()
            svg_file = img_match.group(1).strip()
            desc = desc_match.group(1).strip() if desc_match else ""
            charts.append({"name": name, "svg": svg_file, "desc": desc})

            
    # Process SVGs to update colors
    svg_dir = os.path.join(dir_path, 'Visual Vocabulary_files')
    if os.path.exists(svg_dir):
        for f in os.listdir(svg_dir):
            if f.endswith('.svg'):
                svg_path = os.path.join(svg_dir, f)
                with open(svg_path, 'r', encoding='utf-8') as svg_f:
                    svg_content = svg_f.read()
                
                # Replace colors
                for old_color, new_color in color_replace_map.items():
                    svg_content = re.sub(old_color, new_color, svg_content, flags=re.IGNORECASE)
                    
                with open(svg_path, 'w', encoding='utf-8') as svg_f:
                    svg_f.write(svg_content)
    
    # Get category description. It is usually inside an infoText class, or we can get it from v2-data.js.download.
    # Let's extract from HTML infoText. The first infoText is description, the second is example.
    info_texts = re.findall(r'<div class="infoText">(.*?)</div>', html)
    cat_desc = info_texts[0].strip() if len(info_texts) > 0 else ""
    cat_name = cat_dir.replace('_', ' ').title()
    
    # Generate Markdown
    # We will split charts into chunks of 8
    chunk_size = 8
    for i in range(0, len(charts), chunk_size):
        chunk = charts[i:i+chunk_size]
        
        slides_md += f"\n---\n\n## {cat_name} {'(cont.)' if i > 0 else ''}\n\n"
        if i == 0 and cat_desc:
            slides_md += f"{cat_desc}\n\n"
            
        slides_md += '<div class="cols4">\n'
        for chart in chunk:
            img_src = f"ft_visual_vacab/{cat_dir}/Visual Vocabulary_files/{chart['svg']}"
            slides_md += f'<div class="chart-thumb-sm">\n<p>{chart["name"]}</p>\n<img src="{img_src}" title="{chart["desc"]}">\n</div>\n'
        slides_md += '</div>\n'

print("Generated markdown length:", len(slides_md))

# Now insert into day1.md
day1_path = r'd:\projects\datat_visualisation\day_1\day1.md'
with open(day1_path, 'r', encoding='utf-8') as f:
    day1_content = f.read()

insert_marker = "## The Data-Type Decision Tree"
# Find the end of this slide to insert after
# The slide ends before the next `---`
insert_pos = day1_content.find('---', day1_content.find(insert_marker))

if insert_pos != -1:
    # Insert right before the next ---, actually we should insert AFTER the next ---
    # So we find the '---' that ends the Data-Type Decision Tree slide, and insert right after it.
    insert_pos_after = insert_pos + 3
    new_day1_content = day1_content[:insert_pos_after] + slides_md + "\n" + day1_content[insert_pos_after:]
    with open(day1_path, 'w', encoding='utf-8') as f:
        f.write(new_day1_content)
    print("Successfully updated day1.md")
else:
    print("Could not find insertion point!")
