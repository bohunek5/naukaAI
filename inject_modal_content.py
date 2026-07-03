import os
import re

base_dir = '/Users/karolbohdanowicz/my-ai-agents/naukaAI'
files = ['CLOUDeindex.html', 'ANTIGRAVITYindex.html', 'HERMEsindex.html']

for fname in files:
    filepath = os.path.join(base_dir, fname)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Update modal HTML structure
    old_modal_html = """    <div class="t-modal-body">
      <div class="t-modal-section">
        <h3>Plan Działania</h3>"""
        
    new_modal_html = """    <div class="t-modal-body">
      <div class="t-modal-section">
        <h3 style="margin-bottom: 12px; font-size: 18px;">Co będziemy robić i dlaczego?</h3>
        <p id="modalDesc" style="color: var(--text); font-size: 15px; line-height: 1.7; padding: 18px 24px; background: rgba(120, 120, 120, 0.05); border-left: 4px solid var(--claude); border-radius: 0 12px 12px 0; margin-bottom: 32px; box-shadow: 0 2px 10px rgba(0,0,0,0.02);">
        </p>
      </div>
      <div class="t-modal-section">
        <h3>Plan Działania</h3>"""
        
    content = content.replace(old_modal_html, new_modal_html)
    
    # Increase modal width
    content = content.replace("max-width: 680px;", "max-width: 760px;")
    
    # 2. Update openModal JS
    old_open_modal = """  function openModal(num, title, items) {
    modalTag.textContent = "Lekcja " + num;
    modalTitle.textContent = title;"""
    
    new_open_modal = """  function openModal(num, title, items) {
    modalTag.textContent = "Lekcja " + num;
    modalTitle.textContent = title;
    
    const descEl = document.getElementById('modalDesc');
    if (descEl) {
      descEl.innerHTML = `W tej lekcji skupimy się na zagadnieniu <strong>${title}</strong>. Pokażę Ci dokładnie, co musimy zrobić krok po kroku i dlaczego jest to absolutnie kluczowe dla Twojego sukcesu. Dzięki temu zaoszczędzisz mnóstwo czasu i unikniesz typowych błędów, od razu wdrażając najlepsze praktyki w swoim środowisku pracy.`;
    }"""
    
    content = content.replace(old_open_modal, new_open_modal)
    
    # 3. Update BRANDS array to use domains instead of emojis where possible
    # And update chip() function
    
    old_chip = """  function chip(b) {
    if (b.emoji) return `<span class="brand-chip"><span class="em">${b.emoji}</span>${b.name}</span>`;
    if (b.local) return `<span class="brand-chip"><img src="${b.local}" alt="${b.name}" loading="lazy" />${b.name}</span>`;
    return `<span class="brand-chip"><img src="https://cdn.simpleicons.org/${b.slug}/${b.color}" alt="${b.name}" loading="lazy" />${b.name}</span>`;
  }"""
  
    new_chip = """  function chip(b) {
    if (b.emoji) return `<span class="brand-chip"><span class="em">${b.emoji}</span>${b.name}</span>`;
    if (b.local) return `<span class="brand-chip"><img src="${b.local}" alt="${b.name}" loading="lazy" />${b.name}</span>`;
    if (b.domain) return `<span class="brand-chip"><img src="https://www.google.com/s2/favicons?domain=${b.domain}&sz=128" alt="${b.name}" loading="lazy" />${b.name}</span>`;
    return `<span class="brand-chip"><img src="https://cdn.simpleicons.org/${b.slug}/${b.color}" alt="${b.name}" loading="lazy" />${b.name}</span>`;
  }"""
  
    content = content.replace(old_chip, new_chip)
    
    # Replace emojis with domains
    replacements = {
        '{ name: "Pinecone",    emoji: "🌲" }': '{ name: "Pinecone",    domain: "pinecone.io" }',
        '{ name: "NotebookLM",  emoji: "📔" }': '{ name: "NotebookLM",  domain: "notebooklm.google.com" }',
        '{ name: "Higgsfield",  emoji: "🎬" }': '{ name: "Higgsfield",  domain: "higgsfield.ai" }',
        '{ name: "Firecrawl",   emoji: "🔥" }': '{ name: "Firecrawl",   domain: "firecrawl.dev" }',
        '{ name: "GoHighLevel", emoji: "🎯" }': '{ name: "GoHighLevel", domain: "gohighlevel.com" }',
        '{ name: "Instantly",   emoji: "⚡" }': '{ name: "Instantly",   domain: "instantly.ai" }',
        '{ name: "Granola",     emoji: "🎙" }': '{ name: "Granola",     domain: "granola.so" }'
    }
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done updating HTML files.")
