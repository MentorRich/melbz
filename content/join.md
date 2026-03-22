---
cover_image: "/images/shared/city-architecture.jpg"
title: "Join MELBZ — Your Suburb, Your Voice"
date: 2026-03-17T08:30:00+10:00
author: "Marcus Cole"
description: "Join MELBZ and become part of your suburb's community. Share confessions, debate flat white prices, and discover what's happening near you."
tags: ["community", "join", "signup"]
categories: ["Community"]
---

layout: "custom"

<div class="join-hero">
  <h1>Welcome to the neighbourhood</h1>
  <p class="join-subtitle">Join 2,847 MELBZ members discovering their suburbs together</p>
</div>

<div class="join-container">
  <div class="join-form-wrapper">
    <form id="join-form" class="join-form">
      <div class="form-group">
        <label for="nickname">What should we call you?</label>
        <input type="text" id="nickname" name="nickname" placeholder="Your nickname" required minlength="2" maxlength="20">
        <span class="hint">This is how you'll appear when you post</span>
      </div>
      
      <div class="form-group">
        <label for="suburb">What's your suburb?</label>
        <select id="suburb" name="suburb" required>
          <option value="">Select your suburb...</option>
          <optgroup label="Inner Melbourne">
            <option value="fitzroy">Fitzroy</option>
            <option value="carlton">Carlton</option>
            <option value="collingwood">Collingwood</option>
            <option value="brunswick">Brunswick</option>
            <option value="north-melbourne">North Melbourne</option>
            <option value="richmond">Richmond</option>
            <option value="south-yarra">South Yarra</option>
            <option value="prahran">Prahran</option>
            <option value="st-kilda">St Kilda</option>
            <option value="southbank">Southbank</option>
            <option value="melbourne">Melbourne CBD</option>
          </optgroup>
          <optgroup label="Inner North">
            <option value="fitzroy-north">Fitzroy North</option>
            <option value="brunswick-east">Brunswick East</option>
            <option value="thornbury">Thornbury</option>
            <option value="northcote">Northcote</option>
            <option value="coburg">Coburg</option>
            <option value="cremorne">Cremorne</option>
            <option value="preston">Preston</option>
          </optgroup>
          <optgroup label="Inner West">
            <option value="footscray">Footscray</option>
            <option value="seddon">Seddon</option>
            <option value="kensington">Kensington</option>
            <option value="west-melbourne">West Melbourne</option>
          </optgroup>
          <optgroup label="Inner East">
            <option value="hawthorn">Hawthorn</option>
            <option value="kew">Kew</option>
            <option value="camberwell">Camberwell</option>
            <option value="balaclava">Balaclava</option>
            <option value="elsternwick">Elsternwick</option>
          </optgroup>
          <optgroup label="Bayside">
            <option value="brighton">Brighton</option>
            <option value="hampton">Hampton</option>
            <option value="sandringham">Sandringham</option>
            <option value="port-melbourne">Port Melbourne</option>
            <option value="albert-park">Albert Park</option>
          </optgroup>
        </select>
      </div>
      
      <div class="form-group">
        <label for="email">Your email (for magic links)</label>
        <input type="email" id="email" name="email" placeholder="hq@melbz.com.au" required>
        <span class="hint">We'll send you a magic link to sign in — no passwords yet</span>
      </div>
      
      <div class="form-group checkbox-group">
        <label class="checkbox-label">
          <input type="checkbox" id="newsletter" name="newsletter" checked>
          <span>Send me weekly suburb updates &amp; under the radars</span>
        </label>
      </div>
      
      <button type="submit" class="join-button">Join MELBZ</button>
    </form>
    
    <div id="join-success" class="join-success" style="display: none;">
      <div class="success-icon">🎉</div>
      <h2>You're in!</h2>
      <p id="welcome-message"></p>
      <a href="/" class="continue-button">See what's happening in your suburb →</a>
    </div>
  </div>
  
  <div class="join-benefits">
    <h3>What you get as a member:</h3>
    <ul>
      <li><span class="benefit-icon">⚡</span> <strong>Real-time updates</strong> — See what's happening in your suburb right now</li>
      <li><span class="benefit-icon">💬</span> <strong>Post confessions</strong> — Anonymous or named, your choice</li>
      <li><span class="benefit-icon">🗳</span> <strong>Vote on debates</strong> — Flat white prices, best pasta, etc.</li>
      <li><span class="benefit-icon">🎯</span> <strong>Personalised picks</strong> — Articles matched to your suburb</li>
      <li><span class="benefit-icon">👋</span> <strong>Join the Lounge</strong> — Connect with neighbours</li>
    </ul>
  </div>
</div>

<style>
.join-hero {
  text-align: center;
  padding: 60px 20px 40px;
  background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 100%);
  color: #fff;
}

.join-hero h1 {
  font-size: 42px;
  font-weight: 700;
  margin-bottom: 12px;
  letter-spacing: -1px;
}

.join-subtitle {
  font-size: 18px;
  color: rgba(255,255,255,0.7);
}

.join-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px 20px 80px;
}

@media (max-width: 768px) {
  .join-container {
    grid-template-columns: 1fr;
  }
}

.join-form-wrapper {
  background: #fff;
  border-radius: 16px;
  padding: 32px;
  box-shadow: 0 4px 30px rgba(0,0,0,0.1);
}

.join-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-weight: 600;
  color: #1a1a2e;
  font-size: 14px;
}

.form-group input[type="text"],
.form-group input[type="email"],
.form-group select {
  padding: 14px 16px;
  border: 2px solid #e5e7eb;
  border-radius: 10px;
  font-size: 16px;
  transition: border-color 0.2s;
}

.form-group input:focus,
.form-group select:focus {
  outline: none;
  border-color: #e94560;
}

.hint {
  font-size: 12px;
  color: #6b7280;
}

.checkbox-group {
  flex-direction: row;
  align-items: center;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  font-weight: 400;
}

.checkbox-label input {
  width: 18px;
  height: 18px;
  accent-color: #e94560;
}

.join-button {
  background: linear-gradient(135deg, #e94560 0%, #ff6b6b 100%);
  color: #fff;
  border: none;
  padding: 16px 32px;
  border-radius: 10px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
}

.join-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 20px rgba(233, 69, 96, 0.4);
}

.join-success {
  text-align: center;
  padding: 40px 20px;
}

.success-icon {
  font-size: 64px;
  margin-bottom: 16px;
}

.join-success h2 {
  font-size: 32px;
  margin-bottom: 12px;
  color: #1a1a2e;
}

#welcome-message {
  font-size: 16px;
  color: #6b7280;
  margin-bottom: 24px;
}

.continue-button {
  display: inline-block;
  background: #1a1a2e;
  color: #fff;
  padding: 14px 28px;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 600;
  transition: background 0.2s;
}

.continue-button:hover {
  background: #e94560;
}

.join-benefits {
  color: #1a1a2e;
  padding: 20px 0;
}

.join-benefits h3 {
  font-size: 24px;
  margin-bottom: 24px;
}

.join-benefits ul {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.join-benefits li {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  font-size: 16px;
  line-height: 1.4;
}

.benefit-icon {
  font-size: 24px;
  flex-shrink: 0;
}
</style>

<script>
(function() {
  const form = document.getElementById('join-form');
  const success = document.getElementById('join-success');
  const welcomeMsg = document.getElementById('welcome-message');
  
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const nickname = document.getElementById('nickname').value.trim();
    const suburb = document.getElementById('suburb').value;
    const email = document.getElementById('email').value;
    const newsletter = document.getElementById('newsletter').checked;
    
    // Store user preferences in localStorage
    localStorage.setItem('melbz_user', JSON.stringify({
      nickname: nickname,
      suburb: suburb,
      email: email,
      newsletter: newsletter,
      joinedAt: new Date().toISOString()
    }));
    
    // Update personalisation
    localStorage.setItem('melbz_nickname', nickname);
    localStorage.setItem('melbz_suburb', suburb);
    
    // Hide form, show success
    form.style.display = 'none';
    success.style.display = 'block';
    welcomeMsg.textContent = `Hey ${nickname} — here's what's happening in ${suburb.replace(/-/g, ' ')} this week.`;
    
    // In production, send to API
    console.log('New member:', { nickname, suburb, email, newsletter });
  });
})();
</script>
## Related Articles

- [Northcote](/northcote/)
- [South Yarra](/south-yarra/)
- [Prahran](/prahran/)
- [Southbank](/southbank/)
- [Richmond](/richmond/)


