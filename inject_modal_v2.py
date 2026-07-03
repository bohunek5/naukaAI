import os

base_dir = '/Users/karolbohdanowicz/my-ai-agents/naukaAI'
files = ['CLOUDeindex.html', 'HERMEsindex.html', 'ANTIGRAVITYindex.html']

modal_html_js = '''
<!-- Modal -->
<div class="training-modal-overlay" id="trainingModal">
  <div class="training-modal">
    <div class="t-modal-header">
      <div class="t-modal-tag" id="modalTag">Lekcja</div>
      <h2 class="t-modal-title" id="modalTitle">Tytuł</h2>
      <div class="t-modal-close-icon" onclick="closeModal()">
        <svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" style="width:24px;height:24px;"><path d="M6 18L18 6M6 6l12 12" stroke-linecap="round" stroke-linejoin="round"></path></svg>
      </div>
    </div>
    <div class="t-modal-body">
      <div class="t-modal-section">
        <h3>Plan Działania</h3>
        <ul id="modalList" style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:12px;"></ul>
      </div>
      <div class="t-modal-section">
        <h3>Cel Biznesowy</h3>
        <p id="modalGoal" style="color:var(--text-dim);margin:0;"></p>
      </div>
      <div class="t-modal-section">
        <h3>Plan</h3>
        <p id="modalPlan" style="color:var(--text-dim);margin:0;"></p>
      </div>
    </div>
    <div class="t-modal-footer">
      <div class="btn" style="width:100%;text-align:center;" onclick="closeModal()">Rozumiem, do dzieła!</div>
    </div>
  </div>
</div>

<script>
  const modal = document.getElementById('trainingModal');
  const modalTitle = document.getElementById('modalTitle');
  const modalTag = document.getElementById('modalTag');
  const modalList = document.getElementById('modalList');
  const modalGoal = document.getElementById('modalGoal');
  const modalPlan = document.getElementById('modalPlan');

  function openModal(num, title, items, goal, plan) {
    modalTag.textContent = "Lekcja " + num;
    modalTitle.textContent = title;
    modalGoal.textContent = goal || '';
    modalPlan.textContent = plan || '';
    modalList.innerHTML = '';
    items.forEach((item, idx) => {
      const li = document.createElement('li');
      li.style.display = 'flex';
      li.style.alignItems = 'flex-start';
      li.style.gap = '12px';

      const badge = document.createElement('div');
      badge.textContent = idx + 1;
      badge.style.width = '24px';
      badge.style.height = '24px';
      badge.style.borderRadius = '50%';
      badge.style.background = 'var(--brand)';
      badge.style.color = 'var(--bg)';
      badge.style.display = 'flex';
      badge.style.alignItems = 'center';
      badge.style.justifyContent = 'center';
      badge.style.fontSize = '12px';
      badge.style.fontWeight = 'bold';

      const txt = document.createElement('span');
      txt.textContent = item;
      txt.style.color = 'var(--text-dim)';
      txt.style.lineHeight = '1.5';

      li.appendChild(badge);
      li.appendChild(txt);
      modalList.appendChild(li);
    });
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  modal.addEventListener('click', e => { if (e.target === modal) closeModal(); });

  // Attach click to cards – expects data-goal and data-plan attributes on the <a> element
  document.querySelectorAll('.out-card').forEach(card => {
    card.style.cursor = 'pointer';
    card.addEventListener('click', () => {
      const num = card.querySelector('.out-num')?.textContent.trim() || '';
      const title = card.querySelector('.out-title')?.textContent.trim() || '';
      const items = Array.from(card.querySelectorAll('ul li')).map(li => li.textContent.trim());
      const goal = card.dataset.goal || '';
      const plan = card.dataset.plan || '';
      openModal(num, title, items, goal, plan);
    });
  });
</script>
'''

for fname in files:
    path = os.path.join(base_dir, fname)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    # Insert modal before </body> if not present
    if 'id="trainingModal"' not in html:
        html = html.replace('</body>', modal_html_js + '\n</body>')
    # Add placeholder data attributes to each card anchor if missing
    import re
    def add_attrs(match):
        tag = match.group(0)
        if 'data-goal' in tag and 'data-plan' in tag:
            return tag
        # add generic placeholder text – you can edit later
        return tag.replace('>', ' data-goal="Tutaj cel edukacyjny" data-plan="Tutaj plan działania">')
    html = re.sub(r'<a\s+class="card[^>]*>', add_attrs, html)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print('Modal i atrybuty dodane/uzupełnione')
