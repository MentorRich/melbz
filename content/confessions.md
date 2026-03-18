---
cover_image: "/images/melbourne/confessions.jpg"
title: "MELBZ Confessions — Anonymous & Named"
date: 2026-03-17T08:30:00+10:00
author: ""
description: "Share your confession anonymously or with your name. Melbourne's juiciest secrets, told straight."
tags: ["confessions", "community", "anonymous"]
categories: ["Community"]
---

layout: "custom"

<div class="confessions-hero">
  <h1>Confessions</h1>
  <p class="confessions-subtitle">Melbourne's juiciest secrets, told straight. Anonymous or named — your call.</p>
</div>

<div class="confessions-container">
  <!-- Mode Toggle -->
  <div class="mode-toggle">
    <button id="mode-anonymous" class="mode-button active" onclick="setConfessionMode('anonymous')">
      <span class="mode-icon">🎭</span>
      <span class="mode-label">Anonymous</span>
    </button>
    <button id="mode-named" class="mode-button" onclick="setConfessionMode('named')">
      <span class="mode-icon">👤</span>
      <span class="mode-label">Named</span>
    </button>
  </div>
  
  <!-- Post Form -->
  <div class="confession-form-wrapper">
    <h3 id="form-title">Drop a confession</h3>
    <form id="confession-form">
      <textarea id="confession-text" placeholder="What's your confession? Spill the tea..." required rows="4"></textarea>
      
      <div id="named-fields" style="display: none;">
        <input type="text" id="confession-nickname" placeholder="Your nickname (appears with your post)">
      </div>
      
      <select id="confession-suburb">
        <option value="">From any suburb...</option>
        <optgroup label="Inner Melbourne">
          <option value="fitzroy">Fitzroy</option>
          <option value="carlton">Carlton</option>
          <option value="collingwood">Collingwood</option>
          <option value="brunswick">Brunswick</option>
          <option value="melbourne">Melbourne CBD</option>
        </optgroup>
      </select>
      
      <button type="submit" class="confession-submit">Confess</button>
    </form>
    <p class="form-note">✨ No tracking. No accounts. Just confessions.</p>
  </div>
  
  <!-- Recent Confessions -->
  <div class="recent-confessions">
    <h3>Recent Confessions</h3>
    
    <div class="confession-card">
      <div class="confession-header">
        <span class="confession-author">🎭 Anonymous</span>
        <span class="confession-meta">2 hours ago • Fitzroy</span>
      </div>
      <p class="confession-content">I judged that guy at the Fitzroy Wholefoods for buying $14 almond milk. Then I bought the same one. Who's the real villain here?</p>
      <div class="confession-actions">
        <button class="action-button" onclick="reactConfession(this, '🔥')">🔥 12</button>
        <button class="action-button" onclick="reactConfession(this, '💀')">💀 3</button>
        <button class="action-button" onclick="reactConfession(this, '😂')">😂 7</button>
      </div>
    </div>
    
    <div class="confession-card">
      <div class="confession-header">
        <span class="confession-author">👤 Marcus — <span class="reputation">🔥 47</span></span>
        <span class="confession-meta">4 hours ago • Carlton</span>
      </div>
      <p class="confession-content">I've been going to "that" cafe in Carlton for 6 months thinking it was indie. Found out last week it's a chain. Send thoughts and prayers.</p>
      <div class="confession-actions">
        <button class="action-button" onclick="reactConfession(this, '💀')">💀 15</button>
        <button class="action-button" onclick="reactConfession(this, '😂')">😂 22</button>
        <button class="action-button" onclick="reactConfession(this, '👏')">👏 8</button>
      </div>
    </div>
    
    <div class="confession-card">
      <div class="confession-header">
        <span class="confession-author">🎭 Anonymous</span>
        <span class="confession-meta">6 hours ago • St Kilda</span>
      </div>
      <p class="confession-content">Told my date I loved jazz. I don't. Three years later, we're married and I now own 47 jazz records I never listen to. Worth it.</p>
      <div class="confession-actions">
        <button class="action-button" onclick="reactConfession(this, '❤️')">❤️ 34</button>
        <button class="action-button" onclick="reactConfession(this, '😂')">😂 56</button>
        <button class="action-button" onclick="reactConfession(this, '🙏')">🙏 12</button>
      </div>
    </div>
    
    <div class="confession-card">
      <div class="confession-header">
        <span class="confession-author">👤 Lina — <span class="reputation">🔥 89</span></span>
        <span class="confession-meta">Yesterday • Collingwood</span>
      </div>
      <p class="confession-content">I work in Collingwood and I've seen the same homeless guy reading philosophy books for 2 years. We finally talked last week. His name's Derek. He knows more about Camus than I ever will.</p>
      <div class="confession-actions">
        <button class="action-button" onclick="reactConfession(this, '❤️')">❤️ 127</button>
        <button class="action-button" onclick="reactConfession(this, '😭')">😭 45</button>
        <button class="action-button" onclick="reactConfession(this, '📚')">📚 23</button>
      </div>
    </div>
  </div>
</div>

<style>
.confessions-hero {
  text-align: center;
  padding: 60px 20px 40px;
  background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%);
  color: #fff;
}

.confessions-hero h1 {
  font-size: 48px;
  font-weight: 700;
  margin-bottom: 12px;
}

.confessions-subtitle {
  font-size: 18px;
  color: rgba(255,255,255,0.7);
}

.confessions-container {
  max-width: 700px;
  margin: 0 auto;
  padding: 40px 20px 80px;
}

.mode-toggle {
  display: flex;
  gap: 12px;
  margin-bottom: 24px;
}

.mode-button {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 14px 20px;
  border: 2px solid #e5e7eb;
  background: #fff;
  border-radius: 10px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 600;
  transition: all 0.2s;
}

.mode-button.active {
  border-color: #e94560;
  background: rgba(233, 69, 96, 0.1);
  color: #e94560;
}

.mode-icon {
  font-size: 20px;
}

.confession-form-wrapper {
  background: #fff;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  margin-bottom: 32px;
}

#form-title {
  margin-bottom: 16px;
  font-size: 20px;
}

#confession-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

#confession-text, #confession-nickname, #confession-suburb {
  width: 100%;
  padding: 14px 16px;
  border: 2px solid #e5e7eb;
  border-radius: 10px;
  font-size: 16px;
  font-family: inherit;
}

#confession-text:focus, #confession-nickname:focus, #confession-suburb:focus {
  outline: none;
  border-color: #e94560;
}

.confession-submit {
  background: linear-gradient(135deg, #e94560 0%, #ff6b6b 100%);
  color: #fff;
  border: none;
  padding: 16px 32px;
  border-radius: 10px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s;
}

.confession-submit:hover {
  transform: translateY(-2px);
}

.form-note {
  text-align: center;
  margin-top: 12px;
  font-size: 13px;
  color: #6b7280;
}

.recent-confessions h3 {
  margin-bottom: 20px;
  font-size: 22px;
}

.confession-card {
  background: #fff;
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 16px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.confession-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
  font-size: 14px;
}

.confession-author {
  font-weight: 600;
}

.confession-meta {
  color: #6b7280;
}

.reputation {
  color: #e94560;
}

.confession-content {
  font-size: 16px;
  line-height: 1.6;
  margin-bottom: 16px;
}

.confession-actions {
  display: flex;
  gap: 8px;
}

.action-button {
  padding: 8px 14px;
  border: 1px solid #e5e7eb;
  background: #fff;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.action-button:hover {
  border-color: #e94560;
  background: rgba(233, 69, 96, 0.1);
}
</style>

<script>
let currentMode = 'anonymous';

function setConfessionMode(mode) {
  currentMode = mode;
  document.getElementById('mode-anonymous').classList.toggle('active', mode === 'anonymous');
  document.getElementById('mode-named').classList.toggle('active', mode === 'named');
  document.getElementById('form-title').textContent = mode === 'named' ? 'Post with your name' : 'Drop a confession';
  document.getElementById('named-fields').style.display = mode === 'named' ? 'block' : 'none';
}

document.getElementById('confession-form').addEventListener('submit', function(e) {
  e.preventDefault();
  const text = document.getElementById('confession-text').value.trim();
  const suburb = document.getElementById('confession-suburb').value;
  
  if (!text) return;
  
  // Get user from localStorage if in named mode
  const userStr = localStorage.getItem('melbz_user');
  let nickname = 'Anonymous';
  
  if (currentMode === 'named') {
    const customNickname = document.getElementById('confession-nickname').value.trim();
    if (userStr && !customNickname) {
      nickname = JSON.parse(userStr).nickname;
    } else if (customNickname) {
      nickname = customNickname;
    }
  }
  
  // In production, send to API
  console.log('New confession:', { text, suburb, mode: currentMode, author: nickname });
  
  // Reset form
  document.getElementById('confession-text').value = '';
  alert('Confession posted! (Demo mode - in production this goes live)');
});

function reactConfession(button, emoji) {
  const span = button.querySelector('span');
  const match = span.textContent.match(/(\d+)/);
  let count = match ? parseInt(match[1]) : 0;
  span.textContent = `${emoji} ${count + 1}`;
  button.style.borderColor = '#e94560';
  button.style.background = 'rgba(233, 69, 96, 0.1)';
}
</script>
## Related Articles

- [/st-kilda/](/st-kilda/)
- [/collingwood/](/collingwood/)
- [/fitzroy/](/fitzroy/)
- [/brunswick/](/brunswick/)
- [/melbourne-cbd/](/melbourne-cbd/)

*Find more Melbourne content at [melbz.com.au](/)*

### More to Explore

Melbourne has so much to offer. Consider adding these to your list:

- **[Venue Name]** — [What they do], [Address].
- **[Another Spot]** — [What they're known for], [Address].

The city rewards curiosity. The best experiences often come from wandering down unfamiliar streets and discovering venues that don't have the marketing budget of the big names.
