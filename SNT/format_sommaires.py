import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

snt_dir = r'c:\Users\nicol\OneDrive\Bureau\projet_mkdocs\docs\SNT'
themes = [
    'Donnees_Structurees', 'Geolocalisation', 'Internet', 'Objets_Connectes',
    'Photographie_Numerique', 'Programmation_Python', 'Reseaux_sociaux', 'Web', 'introduction_snt'
]

cat_titles = {
    'cours': 'Cours',
    'tp': 'Travaux Pratiques',
    'exercices': 'Exercices',
    'evaluations': 'Évaluations'
}

emojis_cat = {
    'cours': '📖',
    'tp': '💻',
    'exercices': '✏️',
    'evaluations': '📝'
}

def format_name(filename, cat):
    f_lower = filename.lower()
    name = re.sub(r'\.(md|py|ipynb|pdf|json|jpg|png|gif|csv)$', '', filename, flags=re.I)
    
    name = name.replace('_', ' ')
    words = name.split()
    words = [w.capitalize() if w.lower() not in ['de', 'du', 'des', 'le', 'la', 'les', 'à', 'en', 'et'] else w.lower() for w in words]
    if words:
        words[0] = words[0].capitalize()
    
    formatted = ' '.join(words)
    formatted = formatted.replace('Snt', 'SNT').replace('Tp', 'TP').replace('Td', 'TD').replace('Nmea', 'NMEA').replace('Exif', 'EXIF')
    
    ext = os.path.splitext(filename)[1].lower()
    emoji = emojis_cat[cat]
    prefix = ""
    if ext == '.py':
        emoji = '🐍'
        prefix = 'Script : '
    elif ext == '.pdf':
        emoji = '📄'
        prefix = 'Document : '
    elif ext == '.ipynb':
        emoji = '📓'
        prefix = 'Notebook : '
        
    return f'{emoji} {prefix}{formatted}'

def get_old_display_names(sommaire_path):
    if not os.path.exists(sommaire_path):
        return {}, []
    with open(sommaire_path, 'r', encoding='utf-8') as f:
        old_content = f.read()
        
    display_names = {}
    external_links = []
    
    # regex to find standard markdown links
    for match in re.finditer(r'\[(.*?)\]\((.*?)\)', old_content):
        text = match.group(1).strip()
        link = match.group(2).strip()
        if link.startswith('http'):
            external_links.append(match.group(0))
        else:
            filename = os.path.basename(link)
            if filename:
                display_names[filename] = text
                
    return display_names, external_links

for theme in themes:
    theme_dir = os.path.join(snt_dir, theme)
    if not os.path.exists(theme_dir):
        continue
        
    sommaire_path = os.path.join(theme_dir, 'sommaire.md')
    display_names, external_links = get_old_display_names(sommaire_path)

    title = theme.replace('_', ' ').title()
    title = title.replace('Snt', 'SNT')
    if theme == 'introduction_snt':
        title = 'Introduction SNT'
        
    new_content = f'# {title}\n\n'
    
    for cat in ['cours', 'tp', 'exercices', 'evaluations']:
        cat_dir = os.path.join(theme_dir, cat)
        items = []
        if os.path.isdir(cat_dir):
            for f in os.listdir(cat_dir):
                if os.path.isfile(os.path.join(cat_dir, f)):
                    items.append(f)
                    
        has_items = len(items) > 0
        has_externals = (cat == 'tp' and len(external_links) > 0)
        
        if has_items or has_externals:
            new_content += f'## {cat_titles[cat]}\n\n'
            
            for item in items:
                # Decide if we want to restore old display or use new formatted
                old_disp = display_names.get(item, None)
                
                # If old display has an emoji, let's keep it. 
                # Else generate a fresh one.
                if old_disp and len(old_disp) > 0 and ord(old_disp[0]) > 255:
                    display = old_disp
                elif old_disp and 'TP :' in old_disp:
                    # Keep explicit TP labels
                    display = old_disp
                else:
                    display = format_name(item, cat)
                    
                new_content += f'* [{display}]({cat}/{item})\n'
                
            if cat == 'tp':
                for ext_link in external_links:
                    new_content += f'* {ext_link}\n'
            
            new_content += '\n'

    with open(sommaire_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print('Formatting done.')
