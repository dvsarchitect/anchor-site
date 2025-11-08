// Copied from website-mockup/script.js - minor adjustments for Hugo
document.addEventListener('DOMContentLoaded',function(){
	const toggle=document.querySelector('.mobile-menu-toggle'), nav=document.querySelector('.nav-links');
	if(toggle){ toggle.addEventListener('click',function(){ nav.classList.toggle('mobile-active'); this.classList.toggle('active'); }); }

	// Smooth scroll for in-page anchors only (avoid intercepting absolute hashes like /#about on other pages)
	document.querySelectorAll('a[href^="#"]').forEach(a=>{
		a.addEventListener('click',function(ev){
			const href=this.getAttribute('href');
			if(href && href.startsWith('#') && href.length>1){
				const target=document.querySelector(href);
				if(target){
					ev.preventDefault();
					const navH=(document.querySelector('.navbar')?.offsetHeight)||0;
					const y=target.getBoundingClientRect().top + window.scrollY - navH - 20;
					window.scrollTo({top:y, behavior:'smooth'});
					// Close mobile menu after navigation
					nav?.classList.remove('mobile-active'); toggle?.classList.remove('active');
				}
			}
		});
	});

	// Share buttons
	const shareBtns=document.querySelectorAll('.share-btn');
	shareBtns.forEach(btn=>{
		btn.addEventListener('click',function(){
			const platform=this.dataset.platform, url=window.location.href,
						title=(document.querySelector('.article-title')?.textContent)||'The Anchor';
			let share='';
			switch(platform){
				case 'twitter': share=`https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(title)}`; break;
				case 'facebook': share=`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`; break;
				case 'email': share=`mailto:?subject=${encodeURIComponent(title)}&body=${encodeURIComponent('Check out this devotional: '+url)}`; break;
			}
			if(share){ platform==='email' ? (window.location.href=share) : window.open(share,'_blank','width=600,height=400'); }
		});
	});

	// Reading progress on devotional pages
	const enableProgress=()=>{
		const bar=document.createElement('div');
		bar.className='reading-progress';
		bar.style.cssText='position:fixed;top:0;left:0;width:0%;height:3px;background:var(--color-accent);z-index:9999;transition:width .2s ease;';
		document.body.appendChild(bar);
		window.addEventListener('scroll',()=>{
			const view=window.innerHeight, doc=document.documentElement.scrollHeight - view, y=window.scrollY;
			const pct = doc>0 ? (y/doc*100) : 0; bar.style.width=pct+'%';
		});
	};
	document.querySelector('.devotional-article') && enableProgress();

	// Hide-on-scroll navbar behavior
	let last=0; const navbar=document.querySelector('.navbar');
	window.addEventListener('scroll',()=>{
		const y=window.scrollY;
		if(y<=0){ navbar?.classList.remove('scroll-up'); }
		else if(y>last && !navbar?.classList.contains('scroll-down')){ navbar?.classList.remove('scroll-up'); navbar?.classList.add('scroll-down'); }
		else if(y<last && navbar?.classList.contains('scroll-down')){ navbar?.classList.remove('scroll-down'); navbar?.classList.add('scroll-up'); }
		last=y;
	});

		// Theme toggle logic
		const root = document.documentElement;
		const btn = document.getElementById('theme-toggle');
		const getPref = () => localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
		const apply = (mode) => { root.setAttribute('data-theme', mode); if(btn){ btn.querySelector('.theme-icon').textContent = mode==='dark' ? '☀️' : '🌙'; btn.setAttribute('aria-pressed', mode==='dark' ? 'true':'false'); } };
		apply(getPref());
		btn && btn.addEventListener('click', () => {
			const next = (root.getAttribute('data-theme') === 'dark') ? 'light' : 'dark';
			localStorage.setItem('theme', next);
			apply(next);
		});
});