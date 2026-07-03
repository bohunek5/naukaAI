import os
import re

files = [
    '/Users/karolbohdanowicz/my-ai-agents/naukaAI/CLOUDeindex.html',
    '/Users/karolbohdanowicz/my-ai-agents/naukaAI/HERMEsindex.html',
    '/Users/karolbohdanowicz/my-ai-agents/naukaAI/ANTIGRAVITYindex.html'
]

old_media = """  @media (max-width: 720px) {
    .part-head { flex-wrap: wrap; }
    .part-tools { max-width: 100%; justify-content: flex-start; margin-top: 8px; }
  }"""

new_media = """  @media (max-width: 720px) {
    .part-head { 
      flex-direction: column; 
      align-items: flex-start; 
      gap: 12px; 
      padding: 20px;
    }
    .part-num {
      min-width: auto;
      margin-bottom: -4px;
    }
    .part-info {
      width: 100%;
    }
    .part-tools { 
      max-width: 100%; 
      justify-content: flex-start; 
      margin-top: 4px; 
      flex-wrap: wrap;
    }
  }"""

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_media in content:
            content = content.replace(old_media, new_media)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {os.path.basename(filepath)}")
        else:
            print(f"Could not find exact old_media in {os.path.basename(filepath)}, trying regex...")
            # Try regex if exact match fails due to formatting
            pattern = re.compile(r'@media\s*\(max-width:\s*720px\)\s*\{\s*\.part-head\s*\{\s*flex-wrap:\s*wrap;\s*\}\s*\.part-tools\s*\{[^}]+\}\s*\}', re.MULTILINE)
            if pattern.search(content):
                content = pattern.sub(new_media, content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed {os.path.basename(filepath)} with regex")
            else:
                print(f"Could NOT fix {os.path.basename(filepath)} - pattern not found")
