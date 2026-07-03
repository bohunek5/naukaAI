import os

index_path = '/Users/karolbohdanowicz/my-ai-agents/naukaAI/index.html'

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up the first .cards / .card definitions
old_cards1 = """  .cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
  }"""
content = content.replace(old_cards1, "  /* cards layout handled below */")

old_card1 = """  .card {
    background-color: #0f1119;
    border: 1px solid #242838;
    border-radius: 20px;
    padding: 40px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
    color: white;
    transition: transform 0.2s, border-color 0.2s;
  }"""

new_card1 = """  .card {
    background-color: #0f1119;
    border: 1px solid #242838;
    border-radius: 20px;
    padding: 40px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
    color: white;
    transition: transform 0.2s, border-color 0.2s;
    width: 100%;
  }"""
content = content.replace(old_card1, new_card1)

# 2. Clean up the second .cards / .card definitions and media query
old_cards_responsive = """      /* Desktop: cards in a horizontal row */
  .cards {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    justify-content: center;
    gap: 30px;
    overflow-x: auto;
    padding-bottom: 20px;
  }
  .card {
    min-width: 280px;
    flex: 1;
    max-width: 320px;
  }

  /* Mobile: stack cards vertically, max 3 per screen */
  @media (max-width: 640px) {
    .cards {
      flex-direction: column !important;
      flex-wrap: wrap !important;
      overflow-x: visible;
      gap: 24px;
      align-items: center;
    }
    .card {
      max-width: 90%;
      min-width: auto;
    }
  }"""

new_cards_responsive = """      /* Desktop: 3 cards side by side */
  .cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    justify-content: center;
    width: 100%;
  }
  
  .card {
    max-width: 100%;
  }

  /* Tablet and Mobile: stack cards vertically */
  @media (max-width: 900px) {
    .cards {
      grid-template-columns: 1fr;
      gap: 24px;
      padding: 0 10px;
    }
    .card {
      max-width: 400px;
      margin: 0 auto; /* Center the cards */
    }
  }"""

content = content.replace(old_cards_responsive, new_cards_responsive)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html layout fixed.")
