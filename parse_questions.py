import re
import json

file_path = r"c:\Users\nicol\OneDrive\Bureau\projet_mkdocs\docs\NSI_1\extra\question.md"
output_path = r"c:\Users\nicol\OneDrive\Bureau\projet_mkdocs\quiz_app\questions.js"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

questions = []
blocks = re.split(r'^#+\s*question', content, flags=re.MULTILINE)

for block in blocks:
    if not block.strip():
        continue
    
    q = {}
    
    nom_match = re.search(r'^nom\s*:\s*(.*)', block, re.MULTILINE)
    if nom_match:
        q['nom'] = nom_match.group(1).strip()
        
    groupe_match = re.search(r'^groupe\s*:\s*(.*)', block, re.MULTILINE)
    if groupe_match:
        q['groupe'] = groupe_match.group(1).strip()
        
    diff_match = re.search(r'^difficulte\s*:\s*(.*)', block, re.MULTILINE)
    if diff_match:
        q['difficulte'] = diff_match.group(1).strip()
        
    enonce_match = re.search(r'^(?:énoncé|ennoncé)\s*:(.*?)^(?:réponse|reponse)\s*:', block, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if enonce_match:
        q['enonce'] = enonce_match.group(1).strip()
        
    reponse_match = re.search(r'^(?:réponse|reponse)\s*:(.*)', block, re.MULTILINE | re.DOTALL | re.IGNORECASE)
    if reponse_match:
        q['reponse'] = reponse_match.group(1).strip()
        
    if 'enonce' in q and 'reponse' in q:
        # normalize difficulty to lowercase
        if 'difficulte' in q:
            d = q['difficulte'].lower()
            if 'moyen' in d:
                q['difficulte'] = 'moyenne'
            elif 'facil' in d:
                q['difficulte'] = 'facile'
            elif 'difficil' in d:
                q['difficulte'] = 'difficile'
            
        # normalize groupe
        if 'groupe' in q:
            g = q['groupe'].lower().strip()
            if g == '#2bfafa' or g == 'cyan':
                q['groupe'] = 'Cyan'
            elif g == 'rose':
                q['groupe'] = 'Rose'
            elif g == 'vert':
                q['groupe'] = 'Vert'
            elif g == 'rouge':
                q['groupe'] = 'Rouge'
            else:
                q['groupe'] = g.capitalize()
                
        questions.append(q)

import os
os.makedirs(os.path.dirname(output_path), exist_ok=True)

js_content = f"const questionsData = {json.dumps(questions, ensure_ascii=False, indent=2)};"

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Parsed {len(questions)} questions.")
