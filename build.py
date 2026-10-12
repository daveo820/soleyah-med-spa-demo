# Static page builder for the Soleyah Med Spa & Wellness concept. Run: python3 build.py
from lib import CFG, img, page, bc, finish
BASE='https://soleyah-med-spa-demo.vercel.app/'
TEL,TEL_H='+15124705450','(512) 470&#8209;5450'
MAIL='Soleyah.medspa@gmail.com'
SUN='<svg class="sun" viewBox="0 0 40 22" aria-hidden="true"><path d="M2 21h36"/><path d="M8 21a12 12 0 0 1 24 0"/><path d="M20 3v3M8.5 7.5l2 2M31.5 7.5l-2 2"/></svg>'
ADDR='5601 Brodie Lane, Suite 670, Sunset Valley, TX 78745'
ORG={"@context":"https://schema.org","@type":"HealthAndBeautyBusiness","name":"Soleyah Med Spa & Wellness","url":BASE,"telephone":"+1-512-470-5450","email":MAIL,
 "founder":{"@type":"Person","name":"Laura Lara"},
 "address":{"@type":"PostalAddress","streetAddress":"5601 Brodie Lane, Suite 670","addressLocality":"Sunset Valley","addressRegion":"TX","postalCode":"78745","addressCountry":"US"},
 "description":"Med spa and wellness studio opening in Sunset Valley Village, Austin, targeted for November 2026.","image":BASE+"og.png"}
CFG.update(base=BASE,name='Soleyah Med Spa & Wellness',theme='#3e1f14',org=ORG,
 fonthead='<link rel="preload" as="font" type="font/woff2" href="fonts/cormorant-garamond-normal-500-latin.woff2" crossorigin><link rel="preload" as="font" type="font/woff2" href="fonts/jost-normal-400-latin.woff2" crossorigin>',
 icon="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='16' fill='%233e1f14'/%3E%3Cpath d='M7 22a9 9 0 0 1 18 0' stroke='%23efe4d4' stroke-width='2.4' fill='none'/%3E%3C/svg%3E",
 bar='Not the official Soleyah site. Facts come from soleyahmedspa.com, Sunset Valley Village and What Now Austin. Placeholders are labeled.',
 nav=[('treatments.html','Treatments'),('laura.html','Laura&rsquo;s story'),('visit.html','Visit')],
 mark='<a class="mark" href="index.html" aria-label="Soleyah home"><img src="img/soleyah-logo-640.png" alt="Soleyah" width="640" height="111" class="logo"><small class="logo-sub">Med Spa &amp; Wellness</small></a>',
 cta='<a class="btn" href="visit.html#list">Join the opening list</a>',
 foot=f'''<footer class="foot"><div class="wrap">
<div class="foot-sun" aria-hidden="true"></div>
<p class="foot-big">Opening in Sunset Valley,<br><em>November 2026.</em></p>
<div class="foot-grid"><address><b>Soleyah Med Spa &amp; Wellness</b><br>{ADDR}<br>Sunset Valley Village, next to Sephora and Nordstrom Rack</address>
<p><a href="tel:{TEL}">{TEL_H}</a><br><a href="mailto:{MAIL}">{MAIL}</a><br>Mon to Fri, 8am to 5pm (listed hours)</p>
<ul><li><a href="treatments.html">Treatments</a></li><li><a href="laura.html">Laura&rsquo;s story</a></li><li><a href="visit.html#list">Opening list</a></li></ul></div>
<div class="foot-row"><span>An Austin original. Sunset Valley, Texas.</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>''')

MENU=[('Injectables','Botox and Dysport, dermal fillers and Kybella.'),
 ('Laser','Laser hair removal, skin resurfacing, pigmentation and vascular treatments.'),
 ('Facials','Classic, hydration, anti aging and acne facials, plus HydraFacial, oxygen facials and dermaplaning.'),
 ('Microneedling','Microneedling with or without PRP, and RF microneedling.'),
 ('Chemical peels','Glycolic, TCA, VI Peel and Jessner&rsquo;s.'),
 ('Skin tightening','Ultherapy ultrasound and radiofrequency devices.'),
 ('Body contouring','CoolSculpting, EmSculpt and radiofrequency fat reduction.'),
 ('IV therapy','Vitamin drips and hydration therapy.'),
 ('Wellness','Bioidentical hormone replacement, weight loss injections and peptides.'),
 ('Day spa','Body scrubs, wraps and clay treatments, waxing and sugaring, and red light therapy.')]

page('index.html','Soleyah Med Spa and Wellness | Opening in Sunset Valley, TX',
 'Laura Lara is opening Soleyah, a med spa and wellness studio at Sunset Valley Village in Austin, targeted for November 2026. Join the opening list today.', f'''
<section class="hero"><div class="wrap hero-grid">
 <div class="hero-copy rv"><p class="kicker">{SUN} Sunset Valley Village &middot; Opening November 2026</p>
 <h1>Luxury that feels <em>welcoming,</em> not intimidating.</h1>
 <p class="lede">Soleyah is Laura Lara&rsquo;s new med spa and wellness studio on Brodie Lane: injectables, laser, facials, peptides, weight loss and red light therapy under one roof, with a skin analysis before any plan.</p>
 <div class="cta"><a class="btn" href="visit.html#list">Join the opening list</a><a class="btn btn--plain" href="treatments.html">See the menu</a></div></div>
 <div class="hero-sun rv" aria-hidden="true"><div class="arc a1"></div><div class="arc a2"></div><div class="arc a3"></div><div class="disc"></div>
  <p class="hero-stamp"><b>2,000</b><span>square feet on Brodie Lane</span></p></div>
</div></section>

<section class="arrival"><div class="wrap ar-grid">
 <div class="rv"><p class="kicker">{SUN} The arrival</p><h2>“I want people to walk in there and be like, wow, that was an experience.”</h2><p class="cite">Laura Lara, founder, to What Now Austin</p></div>
 <ol class="ritual">{''.join(f'<li class="rv"><span class="n">0{i+1}</span><b>{a}</b><span>{b}</span></li>' for i,(a,b) in enumerate([('A welcome drink','Something nutritious waiting when you arrive.'),('Warm lavender towels','Soft lighting, natural textures, neutral tones.'),('A skin analysis','Diagnostic technology first, so the plan fits your skin.'),('A plan, not a one time visit','Laura&rsquo;s words: long term relationships and customized plans.')]))}</ol>
</div></section>

<section class="menu-teaser"><div class="wrap">
 <div class="mt-head rv"><p class="kicker">{SUN} One roof</p><h2>Ten kinds of care, from Botox to a body wrap.</h2></div>
 <ul class="mt-list">{''.join(f'<li class="rv"><a href="treatments.html#{n.lower().replace(" ","-")}"><b>{n}</b><span>{d}</span></a></li>' for n,d in MENU[:6])}</ul>
 <a class="btn btn--plain" href="treatments.html">The full menu</a>
</div></section>

<section class="founder"><div class="wrap fd-grid">
 <div class="fd-card rv"><div class="ph-portrait" role="img" aria-label="Placeholder for a portrait of Laura Lara"><span>Portrait of Laura Lara<br>from Lala Blush</span></div></div>
 <div class="rv"><p class="kicker">{SUN} The founder</p><h2>From a $39,000 classroom to her fifth location.</h2>
 <p>Laura spent seven years teaching high school business. Her students kept asking why she taught them to build businesses but had never built one. During the pandemic she listened, found paramedical tattooing, and started Lala Blush.</p>
 <p>Soleyah is her biggest location yet, and it was designed from day one to grow into a brand people will call an Austin original.</p>
 <a class="btn btn--plain" href="laura.html">Read Laura&rsquo;s story</a></div>
</div></section>

<section class="where"><div class="wrap wh-grid rv">
 <div><p class="kicker" style="color:var(--sand)">{SUN} Where</p><h2>Sunset Valley Village, next to Sephora and Nordstrom Rack.</h2><p>{ADDR}. Construction is underway now.</p></div>
 <div class="wh-cta"><a class="btn light" href="visit.html#list">Get opening news</a><a class="btn btn--plain light" href="tel:{TEL}">Call {TEL_H}</a></div>
</div></section>''', extra_ld=[bc(('Home',''))])

page('treatments.html','Med Spa Treatments Coming to Sunset Valley | Soleyah Austin',
 'Injectables, laser, facials, microneedling, peels, skin tightening, body contouring, IV therapy and wellness at Soleyah. See the planned menu and join the list.', f'''
<section class="page-head"><div class="wrap"><p class="kicker rv">{SUN} The planned menu</p><h1 class="rv">Everything under one roof, starting with your skin.</h1>
<p class="lede rv">This is the treatment menu Soleyah publishes today. Final services, providers and pricing will be confirmed before opening.</p></div></section>
<section class="menu"><div class="wrap">{''.join(f'<article class="mi rv" id="{n.lower().replace(" ","-")}"><span class="mi-n">{i+1:02d}</span><h2>{n}</h2><p>{d}</p></article>' for i,(n,d) in enumerate(MENU))}
<div class="ph rv"><b>Placeholder</b>Pricing, the supervising medical director and provider credentials go here once Soleyah confirms them. Medical treatments require a consultation.</div></div></section>''',
 extra_ld=[bc(('Home',''),('Treatments','treatments.html'))])

page('laura.html','Meet Laura Lara, Founder of Soleyah Med Spa | Sunset Valley',
 'Former high school teacher, Lala Blush founder and now the woman behind Soleyah in Sunset Valley. Read how Laura Lara went from teaching to her fifth location.', f'''
<section class="page-head story"><div class="wrap st-grid"><div><p class="kicker rv">{SUN} Laura&rsquo;s story</p><h1 class="rv">“The world is yours.”</h1>
<p class="lede rv">Laura Lara grew up in El Paso, the daughter of immigrant parents from Mexico who sacrificed everything for their children&rsquo;s future.</p></div>
<div class="ph-portrait rv" role="img" aria-label="Placeholder for a portrait of Laura Lara"><span>Portrait of Laura<br>from Lala Blush</span></div></div></section>
<section class="timeline"><div class="wrap"><ol class="tl">
<li class="rv"><b>The classroom</b><p>Seven years teaching high school business, and on the path to principal. “Five years ago, I was a high school teacher making $39,000 a year.”</p></li>
<li class="rv"><b>The question</b><p>Her students kept asking: you make us do projects about building businesses, but you&rsquo;ve never built one. During the pandemic, she listened.</p></li>
<li class="rv"><b>Lala Blush</b><p>She discovered paramedical tattooing and built Lala Blush around paramedical tattooing, skin restoration and confidence driven aesthetics.</p></li>
<li class="rv"><b>Why it matters to her</b><p>“I firsthand saw how insecurities from acne scars, surgical scars, aging, and simply not feeling like yourself could affect the way people show up in the world.”</p></li>
<li class="rv"><b>Soleyah</b><p>Her fifth location and her biggest, in Sunset Valley, because she did not see a med spa there that offered everything or felt welcoming.</p></li></ol>
<blockquote class="pull rv"><p>“Anything you&rsquo;re envisioning in your head, envision it 10 times bigger, because it will happen.”</p><footer>Laura Lara, to What Now Austin, August 2026</footer></blockquote></div></section>''',
 extra_ld=[bc(('Home',''),('Laura','laura.html')),{"@context":"https://schema.org","@type":"Person","name":"Laura Lara","jobTitle":"Founder","worksFor":{"@type":"Organization","name":"Soleyah Med Spa & Wellness"}}])

page('visit.html','Visit Soleyah at Sunset Valley Village | Join the Opening List',
 'Soleyah opens at 5601 Brodie Lane, Suite 670 in Sunset Valley, targeted for November 2026. Join the opening list or call (512) 470 5450 with questions today.', f'''
<section class="page-head"><div class="wrap"><p class="kicker rv">{SUN} Visit</p><h1 class="rv">Be first through the door.</h1></div></section>
<section class="visit" id="list"><div class="wrap vi-grid">
<form class="rv" data-demo="Thank you. On the live site you would be on Soleyah&rsquo;s opening list. (Demo: nothing was sent.)" novalidate>
<div class="fld"><label for="nm">Name</label><input id="nm" name="nm" autocomplete="name" required></div>
<div class="fld"><label for="em">Email</label><input id="em" name="em" type="email" autocomplete="email" required></div>
<div class="fld"><label for="ph">Phone (optional)</label><input id="ph" name="ph" type="tel" autocomplete="tel"></div>
<div class="fld"><label for="int">Most interested in</label><select id="int" name="int">{''.join(f'<option>{n}</option>' for n,_ in MENU)}</select></div>
<button class="btn" type="submit">Join the opening list</button><p class="formmsg" role="status" aria-live="polite"></p></form>
<aside class="vi-side rv"><h2>Find us</h2><address>{ADDR}<br>Sunset Valley Village</address><p><a href="tel:{TEL}">{TEL_H}</a><br><a href="mailto:{MAIL}">{MAIL}</a></p>
<p class="note">Listed hours: Monday to Friday, 8am to 5pm. Opening hours will be confirmed.</p>
<div class="ph"><b>Placeholder</b>Map, parking notes and online booking go here at opening.</div></aside></div></section>''',
 extra_ld=[bc(('Home',''),('Visit','visit.html'))])

page('404.html','Page Not Found | Soleyah Med Spa and Wellness Concept, Austin',
 'That page is not part of the Soleyah concept. Head back home, see the planned treatment menu, or join the opening list for Sunset Valley Village in Austin.', f'''
<section class="page-head"><div class="wrap"><p class="kicker">{SUN} Not here</p><h1>This page has not opened yet.</h1><a class="btn" href="index.html">Back home</a></div></section>''')
finish(['index.html','treatments.html','laura.html','visit.html'])
print('built')
