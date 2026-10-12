(()=>{const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const mb=$('.menu-btn'),menu=$('#menu');
if(mb){const set=o=>{menu.classList.toggle('open',o);mb.setAttribute('aria-expanded',o);mb.textContent=o?'Close':'Menu'};
 mb.addEventListener('click',()=>set(!menu.classList.contains('open')));
 addEventListener('keydown',e=>{if(e.key==='Escape'&&menu.classList.contains('open')){set(false);mb.focus()}});
 menu.addEventListener('click',e=>{if(e.target.closest('a'))set(false)})}
$$('form[data-demo]').forEach(f=>f.addEventListener('submit',e=>{e.preventDefault();const m=f.querySelector('.formmsg');m.textContent=f.checkValidity()?f.dataset.demo:'Please fill in the required fields.'}));
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const count=el=>{const end=parseFloat(el.dataset.count),dec=+(el.dataset.dec||0),t0=performance.now(),d=900,fmt=v=>dec?v.toFixed(dec):Math.round(v).toLocaleString('en-US');const f=t=>{const k=Math.min((t-t0)/d,1);el.textContent=fmt(end*(1-Math.pow(1-k,3)));if(k<1)requestAnimationFrame(f)};requestAnimationFrame(f)};
const els=$$('.rv');
if(!('IntersectionObserver' in window)||reduce){els.forEach(e=>e.classList.add('in'));return}
const io=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){const t=en.target,s=[...t.parentNode.children].filter(x=>x.classList.contains('rv'));t.style.transitionDelay=Math.min(Math.max(s.indexOf(t),0),5)*70+'ms';t.classList.add('in');t.querySelectorAll('[data-count]').forEach(count);io.unobserve(t)}}),{rootMargin:'0px 0px -80px 0px'});
els.forEach(e=>io.observe(e));
// safety: anything above the fold reveals immediately, and a scroll sweep catches fast scrolls the observer misses
let tk=0;const sweep=()=>{tk=0;els.forEach(e=>{if(!e.classList.contains('in')&&e.getBoundingClientRect().top<innerHeight)e.classList.add('in')})};addEventListener('scroll',()=>{if(!tk)tk=setTimeout(sweep,150)},{passive:true});
requestAnimationFrame(()=>els.forEach(e=>{if(e.getBoundingClientRect().top<innerHeight)e.classList.add('in')}));})();
