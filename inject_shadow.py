import os

index_path = '/Users/karolbohdanowicz/my-ai-agents/naukaAI/index.html'

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

shadow_css = """
      .card-claude img {
        border-radius: 12px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
      }
      body.light-mode .card-claude img {
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
      }
"""

if "body.light-mode .card-claude img" not in content:
    content = content.replace("</style>", shadow_css + "</style>", 1)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Shadow added.")
