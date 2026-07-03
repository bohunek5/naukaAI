import os

files = [
    '/Users/karolbohdanowicz/my-ai-agents/naukaAI/CLOUDeindex.html',
    '/Users/karolbohdanowicz/my-ai-agents/naukaAI/HERMEsindex.html',
    '/Users/karolbohdanowicz/my-ai-agents/naukaAI/ANTIGRAVITYindex.html'
]

old_footer = """    <div class="t-modal-footer">
      <div class="btn" style="width: 100%; text-align: center;" onclick="closeModal()">Rozumiem, do dzieła!</div>
    </div>"""

new_footer = """    <div class="t-modal-footer">
      <div class="btn" id="copyBtn" style="width: 100%; text-align: center; cursor: pointer;" onclick="copyLesson()">Kopiuj lekcję</div>
    </div>"""

old_desc = """    const descEl = document.getElementById('modalDesc');
    if (descEl) {
      descEl.innerHTML = `W tej lekcji skupimy się na zagadnieniu <strong>${title}</strong>. Pokażę Ci dokładnie, co musimy zrobić krok po kroku i dlaczego jest to absolutnie kluczowe dla Twojego sukcesu. Dzięki temu zaoszczędzisz mnóstwo czasu i unikniesz typowych błędów, od razu wdrażając najlepsze praktyki w swoim środowisku pracy.`;
    }"""

new_desc = """    const descEl = document.getElementById('modalDesc');
    if (descEl) {
      const bullets = items.map(i => `<strong>${i}</strong>`).join(', ');
      descEl.innerHTML = `W tej lekcji omówimy szczegółowo takie zagadnienia jak: ${bullets}. Dowiesz się kilku kluczowych rzeczy na ten temat, co pozwoli Ci oszczędzić mnóstwo czasu i wdrożyć najlepsze praktyki w Twoim środowisku pracy.`;
    }"""

copy_function = """
  function copyLesson() {
    const title = document.getElementById('modalTitle').innerText;
    const tag = document.getElementById('modalTag').innerText;
    const items = Array.from(document.querySelectorAll('#modalList li div:last-child')).map(el => el.innerText);
    
    const textToCopy = `Przygotuj materiał / lekcję dla:
Temat: ${tag} - ${title}

Plan Działania:
${items.map((item, i) => `${i+1}. ${item}`).join('\\n')}

Cel Biznesowy:
Opanowanie tych umiejętności pozwoli zaoszczędzić godziny pracy manualnej i wejść na wyższy poziom automatyzacji z wykorzystaniem AI.`;

    navigator.clipboard.writeText(textToCopy).then(() => {
      const btn = document.getElementById('copyBtn');
      const oldText = btn.innerText;
      btn.innerText = "Skopiowano!";
      btn.style.background = "#10b981"; // zielony sukces
      btn.style.color = "white";
      
      setTimeout(() => {
        btn.innerText = oldText;
        btn.style.background = "";
        btn.style.color = "";
        closeModal();
      }, 1500);
    }).catch(err => {
      console.error('Failed to copy text: ', err);
    });
  }
"""

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(old_footer, new_footer)
        content = content.replace(old_desc, new_desc)
        
        # Insert copy function before closeModal
        if "function closeModal()" in content and "function copyLesson()" not in content:
            content = content.replace("function closeModal()", copy_function + "\n  function closeModal()")
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
