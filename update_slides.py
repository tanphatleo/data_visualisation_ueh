import os
import re

root = r'd:\projects\datat_visualisation\day_1\ft_visual_vacab'
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
    
    with open(html_path, encoding='utf-8') as f:
        html = f.read()
    
    parts = html.split('<div class="chart" style="max-width:')
    chart_blocks = parts[1:]
    
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

    info_texts = re.findall(r'<div class="infoText">(.*?)</div>', html)
    cat_desc = info_texts[0].strip() if len(info_texts) > 0 else ""
    
    # Update 1: Change title to include "FT Visual Vocab - "
    cat_name = f"FT Visual Vocab - {cat_dir.replace('_', ' ').title()}"
    
    # Update 2: Maximum 4 charts per slide
    chunk_size = 4
    for i in range(0, len(charts), chunk_size):
        chunk = charts[i:i+chunk_size]
        
        slides_md += f"---\n\n## {cat_name} {'(cont.)' if i > 0 else ''}\n\n"
        if i == 0 and cat_desc:
            slides_md += f"{cat_desc}\n\n"
            
        slides_md += '<div class="cols4">\n'
        for chart in chunk:
            img_src = f"ft_visual_vacab/{cat_dir}/Visual Vocabulary_files/{chart['svg']}"
            
            # Update 3: Include the explanation from the HTML below each chart image
            # Using a span/div to avoid inheriting the uppercase styling applied to `.chart-thumb-sm p`
            desc_html = f'<div style="font-size: 0.6em; font-weight: normal; color: var(--gray); text-transform: none; letter-spacing: normal; line-height: 1.4; margin: 8px auto 0; width: 75%; text-align: justify;">{chart["desc"]}</div>'
            
            slides_md += f'<div class="chart-thumb-sm">\n<p>{chart["name"]}</p>\n<img src="{img_src}">\n{desc_html}\n</div>\n'
        slides_md += '</div>\n\n'
        
        # Add the reference citation to the bottom right of each slide
        slides_md += '<p style="font-size:0.45em; color:#7e7e7e; text-align:right; margin-top:16px;">Financial Times. (n.d.). <em>Visual vocabulary</em>. <a href="https://ft-interactive.github.io/visual-vocabulary/">https://ft-interactive.github.io/visual-vocabulary/</a></p>\n\n'

day1_path = r'd:\projects\datat_visualisation\day_1\day1.md'
with open(day1_path, 'r', encoding='utf-8') as f:
    day1_content = f.read()

# Locate the block we injected previously.
# It starts at "## FT Visual Vocab - Deviation" (which we will now replace).
# It ends right before "## Dex01.02".
dev_pos = day1_content.find('## FT Visual Vocab - Deviation')
dex_pos = day1_content.find('## Dex01.02')

if dev_pos != -1 and dex_pos != -1:
    # Find the slide divider '---' right before ## Deviation
    start_idx = day1_content.rfind('---', 0, dev_pos)
    if start_idx == -1:
        start_idx = dev_pos
        
    # Re-inject the new slides, making sure the slide transition for Dex01.02 is properly added since
    # it was accidentally stripped in the last run.
    new_content = day1_content[:start_idx] + slides_md.strip() + "\n\n---\n\n" + day1_content[dex_pos:]
    with open(day1_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated day1.md successfully!")
else:
    print("Error: Could not find markers ## Deviation or ## Dex01.02 in day1.md")
