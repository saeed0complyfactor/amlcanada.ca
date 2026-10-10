(() => {
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  // Settings come from build.py (WEB3FORMS_KEY, GA4_ID) via window.AMLC.
  const CONFIG = window.AMLC || {};

  /* Menu */
  const menu = $("#menu");
  const openBtn = $(".utility-btn");
  const closeBtn = $(".menu-close");
  const setMenu = (open) => {
    menu.hidden = !open;
    openBtn.setAttribute("aria-expanded", String(open));
    document.body.style.overflow = open ? "hidden" : "";
    (open ? closeBtn : openBtn).focus();
  };
  openBtn.addEventListener("click", () => setMenu(true));
  closeBtn.addEventListener("click", () => setMenu(false));
  addEventListener("keydown", (e) => { if (e.key === "Escape" && !menu.hidden) setMenu(false); });
  $$("a", menu).forEach((a) => a.addEventListener("click", () => { menu.hidden = true; openBtn.setAttribute("aria-expanded", "false"); document.body.style.overflow = ""; }));

  /* Hero carousel (homepage only) */
  const slides = $$(".slide");
  if (slides.length) {
  const copies = $$(".panel-copy");
  const thumbs = $$(".thumb");
  const toggle = $(".thumb-toggle");
  const DURATION = 7000;
  let current = 0;
  let timer = null;
  let playing = !reduce;

  const runBar = (i) => {
    thumbs.forEach((t) => {
      const bar = $("i", t);
      bar.getAnimations().forEach((a) => a.cancel());
    });
    if (!playing) return;
    $("i", thumbs[i]).animate([{ width: "0%" }, { width: "100%" }], { duration: DURATION, easing: "linear", fill: "forwards" });
  };

  const go = (i, user = false) => {
    if (i === current && !user) return;
    slides[current].classList.remove("is-on");
    slides[current].setAttribute("aria-hidden", "true");
    copies[current].hidden = true;
    copies[current].classList.remove("is-on");
    thumbs[current].classList.remove("is-on");
    thumbs[current].removeAttribute("aria-current");
    current = i;
    slides[i].classList.add("is-on");
    slides[i].removeAttribute("aria-hidden");
    const img = $("img", slides[i]);
    img.loading = "eager";
    copies[i].hidden = false;
    copies[i].classList.add("is-on");
    thumbs[i].classList.add("is-on");
    thumbs[i].setAttribute("aria-current", "true");
    if (!reduce) {
      copies[i].animate([{ opacity: 0, transform: "translateY(14px)" }, { opacity: 1, transform: "none" }], {
        duration: 900, delay: 250, easing: "cubic-bezier(0.16, 1, 0.3, 1)", fill: "backwards",
      });
    }
    schedule();
  };

  const schedule = () => {
    clearTimeout(timer);
    runBar(current);
    if (playing) timer = setTimeout(() => go((current + 1) % slides.length), DURATION);
  };

  const setPlaying = (p) => {
    playing = p;
    toggle.setAttribute("aria-label", p ? "Pause slideshow" : "Play slideshow");
    $("use", toggle).setAttribute("href", p ? "#pause" : "#play");
    schedule();
  };

  thumbs.forEach((t) => t.addEventListener("click", () => go(+t.dataset.go, true)));
  toggle.addEventListener("click", () => setPlaying(!playing));
  if (reduce) setPlaying(false);

  // Pause while the visitor is reading the panel or the tab is hidden.
  const hero = $(".hero");
  let hoverPaused = false;
  hero.addEventListener("pointerenter", () => { if (playing) { hoverPaused = true; clearTimeout(timer); $("i", thumbs[current]).getAnimations().forEach((a) => a.pause()); } });
  hero.addEventListener("pointerleave", () => { if (hoverPaused) { hoverPaused = false; schedule(); } });
  document.addEventListener("visibilitychange", () => { if (!document.hidden && playing) schedule(); else clearTimeout(timer); });
  schedule();
  }

  /* Expertise tabs (homepage only) */
  const tabs = $$('.exp-tabs [role="tab"]');
  const selectTab = (name, focus = false) => {
    tabs.forEach((t) => {
      const on = t.dataset.tab === name;
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
      if (on && focus) t.focus();
    });
    $$("[data-panel]").forEach((p) => (p.hidden = p.dataset.panel !== name));
    $$("[data-blurb]").forEach((p) => (p.hidden = p.dataset.blurb !== name));
    $$("[data-img]").forEach((p) => (p.hidden = p.dataset.img !== name));
    const panel = $(`[data-panel="${name}"]`);
    if (!reduce) {
      $$("li", panel).forEach((li, k) =>
        li.animate([{ opacity: 0, transform: "translateX(-10px)" }, { opacity: 1, transform: "none" }], {
          duration: 600, delay: k * 50, easing: "cubic-bezier(0.16, 1, 0.3, 1)", fill: "backwards",
        })
      );
      const img = $(`[data-img="${name}"]`);
      img.animate([{ opacity: 0, transform: "scale(1.04)" }, { opacity: 1, transform: "none" }], { duration: 900, easing: "cubic-bezier(0.16, 1, 0.3, 1)" });
    }
  };
  tabs.forEach((t, i) => {
    t.addEventListener("click", () => selectTab(t.dataset.tab));
    t.addEventListener("keydown", (e) => {
      const keys = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 };
      if (e.key in keys) {
        e.preventDefault();
        selectTab(tabs[(i + keys[e.key] + tabs.length) % tabs.length].dataset.tab, true);
      }
    });
  });

  /* Expertise items open in place */
  const openItem = (li, open) => {
    const btn = $(":scope > button", li);
    const detail = $(".exp-detail", li);
    btn.setAttribute("aria-expanded", String(open));
    detail.hidden = !open;
    if (open && !reduce) detail.animate([{ opacity: 0, transform: "translateY(-6px)" }, { opacity: 1, transform: "none" }], { duration: 450, easing: "cubic-bezier(0.16, 1, 0.3, 1)" });
  };
  $$(".exp-list li").forEach((li) => {
    $(":scope > button", li).addEventListener("click", (e) => {
      const open = e.currentTarget.getAttribute("aria-expanded") !== "true";
      $$("li", li.parentElement).forEach((x) => x !== li && openItem(x, false));
      openItem(li, open);
    });
  });

  // Links anywhere on the page can point at a tab and an item.
  $$("a[data-tab]").forEach((a) =>
    a.addEventListener("click", () => {
      selectTab(a.dataset.tab);
      if (a.dataset.item) {
        const li = $(`[data-panel="${a.dataset.tab}"] li[data-item="${a.dataset.item}"]`);
        if (li) {
          $$("li", li.parentElement).forEach((x) => openItem(x, x === li));
        }
      }
    })
  );

  // "Ask about…" links preselect the form.
  const needSelect = $('select[name="need"]');
  if (needSelect) {
    $$("a[data-need]").forEach((a) => a.addEventListener("click", () => { needSelect.value = a.dataset.need; }));
    const asked = new URLSearchParams(location.search).get("need");
    const match = asked && [...needSelect.options].find((o) => o.text.toLowerCase().startsWith(asked.toLowerCase().replace(/s$/, "")));
    if (match) needSelect.value = match.value || match.text;
  }

  /* Scroll reveal: content is visible without JS */
  if (!reduce && "IntersectionObserver" in window) {
    document.documentElement.classList.add("js");
    const targets = [".eyeline", ".tile", ".exp-body", ".explain-copy", ".explain-photo", ".consult-grid > *", ".foot-grid", ".lead-grid > *", ".rule-grid > *", ".steps-list li", ".link-card", ".svc-row", ".group", ".hw-list > li", ".cta-grid > *"];
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    targets.forEach((sel) => $$(sel).forEach((el, k) => {
      el.classList.add("reveal");
      el.style.transitionDelay = `${Math.min(k, 3) * 80}ms`;
      io.observe(el);
    }));
  }

  /* Consultation form */
  const form = $("#consult-form");
  if (form) {
  const msg = $(".form-msg", form);
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    msg.className = "form-msg";
    let bad = null;
    $$("input, select", form).forEach((f) => {
      const invalid = !f.checkValidity();
      f.setAttribute("aria-invalid", String(invalid));
      if (invalid && !bad) bad = f;
    });
    if (bad) {
      const label = bad.closest("label").firstElementChild.textContent;
      msg.textContent = bad.type === "email" && bad.value ? "Enter an email address like name@company.ca." : `Please add your ${label.toLowerCase()}.`;
      msg.classList.add("err");
      bad.focus();
      return;
    }
    const btn = $("button", form);
    const label = btn.innerHTML;
    btn.disabled = true;
    btn.textContent = "Sending…";
    try {
      if (!CONFIG.web3formsKey) throw new Error("no-endpoint");
      const data = new FormData(form);
      if (data.get("botcheck")) throw new Error("bot");
      data.delete("botcheck");
      data.append("access_key", CONFIG.web3formsKey);
      data.append("subject", `Consultation request: ${data.get("need") || "AML Canada"}`);
      data.append("from_name", "AML Canada website");
      data.append("page", location.pathname);
      const res = await fetch("https://api.web3forms.com/submit", { method: "POST", headers: { Accept: "application/json" }, body: data });
      const json = await res.json().catch(() => ({}));
      if (!res.ok || !json.success) throw new Error("http");
      if (window.gtag) window.gtag("event", "generate_lead", { service: data.get("need") });
      msg.textContent = "Thank you. We’ll be in touch to find a time.";
      msg.classList.add("ok");
      form.reset();
    } catch (err) {
      msg.textContent = err.message === "no-endpoint"
        ? "Consultation requests aren’t connected on this preview yet. Nothing was sent."
        : "That didn’t go through. Please check your connection and try again.";
      msg.classList.add("err");
    } finally {
      btn.disabled = false;
      btn.innerHTML = label;
    }
  });
  $$("input, select", form).forEach((f) => f.addEventListener("input", () => f.removeAttribute("aria-invalid")));
  }

  /* Google Analytics, only after consent */
  if (CONFIG.ga4) {
    const KEY = "amlc-consent";
    let choice = null;
    try { choice = localStorage.getItem(KEY); } catch {}
    const loadGa = () => {
      if (window.gtag) return;
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { window.dataLayer.push(arguments); };
      window.gtag("js", new Date());
      window.gtag("config", CONFIG.ga4, { anonymize_ip: true });
      const s = document.createElement("script");
      s.async = true;
      s.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(CONFIG.ga4)}`;
      document.head.appendChild(s);
    };
    const banner = document.createElement("div");
    banner.className = "consent";
    banner.setAttribute("role", "dialog");
    banner.setAttribute("aria-label", "Cookie choice");
    banner.innerHTML = '<p>We use Google Analytics cookies to understand how this site is used, only if you agree. <a href="privacy.html#cookies">Privacy policy</a></p><div class="consent-actions"><button type="button" data-c="reject">Reject</button><button type="button" data-c="accept" class="btn">Accept</button></div>';
    const decide = (c) => {
      try { localStorage.setItem(KEY, c); } catch {}
      banner.remove();
      if (c === "accept") loadGa();
      else if (window.gtag) location.reload(); // stop a session that was already measuring
    };
    banner.addEventListener("click", (e) => { const c = e.target.closest("[data-c]"); if (c) decide(c.dataset.c); });
    const show = () => { if (!banner.isConnected) document.body.appendChild(banner); };
    if (choice === "accept") loadGa();
    else if (choice !== "reject") show();
    $$(".cookie-settings").forEach((b) => { b.hidden = false; b.addEventListener("click", show); });
  }
})();
