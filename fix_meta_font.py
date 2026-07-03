import os
import re

files = [
    '/Users/karolbohdanowicz/my-ai-agents/naukaAI/CLOUDeindex.html',
    '/Users/karolbohdanowicz/my-ai-agents/naukaAI/HERMEsindex.html',
    '/Users/karolbohdanowicz/my-ai-agents/naukaAI/ANTIGRAVITYindex.html'
]

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # We need to inject a mobile font size fix for .meta inside the @media (max-width: 720px) block
        # Let's just find the @media block we just injected and add .part-info .meta rules
        
        target = ".part-info {\n      width: 100%;\n    }"
        replacement = """.part-info {
      width: 100%;
    }
    .part-info .meta {
      font-size: 13px !important;
      line-height: 1.4 !important;
    }"""
        
        if target in content:
            content = content.replace(target, replacement)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed .meta font-size in {os.path.basename(filepath)}")
        else:
            print(f"Could not find target in {os.path.basename(filepath)}")
