(() => {
  "use strict";

  /* Settings live in site-config.js (Web3Forms key, Google tag ID, Cloudflare token). */
  const CFG = window.SITE_CONFIG || {};
  const FORM_ENDPOINT = "https://api.web3forms.com/submit";

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduceMQ = matchMedia("(prefers-reduced-motion: reduce)");
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const lerp = (a, b, t) => a + (b - a) * t;
  const smooth = (a, b, v) => { const t = clamp((v - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };
  const easeIO = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
  const hex = (h) => [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];
  const mix = (a, b, t) => `rgb(${Math.round(lerp(a[0], b[0], t))},${Math.round(lerp(a[1], b[1], t))},${Math.round(lerp(a[2], b[2], t))})`;

  /* ------------------------------------------------------------------
     City: a procedural city whose streets carry payments as light.
     Rendered with a small perspective camera on a 2D canvas.
  ------------------------------------------------------------------ */
  function City(canvas, opt = {}) {
    const ctx = canvas.getContext("2d", { alpha: false });
    let seed = opt.seed || 11;
    const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
    const COLS = opt.cols || 12, ROWS = opt.rows || 20;
    const B = 1, S = 0.42, P = B + S;
    const X0 = -(COLS * P) / 2, X1 = -X0, ZMAX = ROWS * P;
    const NEAR = 0.12;
    const xs = [], zs = [];
    for (let c = 0; c <= COLS; c++) xs.push(X0 + c * P);
    for (let r = 0; r <= ROWS; r++) zs.push(r * P);

    const blds = [];
    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        const bx = xs[c] + S / 2, bz = zs[r] + S / 2;
        const mx = bx + B / 2, mz = bz + B / 2;
        const dt = Math.exp(-((mx / 4.2) ** 2) - ((mz - 13) / 8) ** 2);
        const k = rnd();
        const lots = k < 0.3 ? [[0, 0, 1, 1]]
          : k < 0.5 ? [[0, 0, 0.5, 1], [0.5, 0, 1, 1]]
          : k < 0.7 ? [[0, 0, 1, 0.5], [0, 0.5, 1, 1]]
          : [[0, 0, 0.5, 0.5], [0.5, 0, 1, 0.5], [0, 0.5, 0.5, 1], [0.5, 0.5, 1, 1]];
        for (const [u1, v1, u2, v2] of lots) {
          if (rnd() < 0.05) continue;
          const g = 0.05;
          const b = { x1: bx + u1 * B + g, x2: bx + u2 * B - g, z1: bz + v1 * B + g, z2: bz + v2 * B - g };
          b.h = 0.2 + rnd() * 0.45 + Math.pow(rnd(), 2.3) * 4.8 * (0.16 + dt);
          b.cx = (b.x1 + b.x2) / 2; b.cz = (b.z1 + b.z2) / 2;
          b.win = [];
          const n = Math.min(18, Math.round(b.h * 4.5));
          for (let i = 0; i < n; i++) {
            if (rnd() < 0.45) continue;
            b.win.push({ side: rnd() < 0.5 ? 0 : 1, u: 0.15 + rnd() * 0.7, v: (0.08 + rnd() * 0.86) * b.h, warm: rnd() < 0.72 });
          }
          b.cs = new Float32Array(24);
          b.ss = new Float32Array(16);
          b.ok = false;
          blds.push(b);
        }
      }
    }

    /* Payments: light moving along street lanes */
    const COLS_WARM = [[255, 236, 206], [255, 178, 63], [255, 178, 63], [255, 214, 150]];
    const parts = [];
    const spawn = (p, fresh) => {
      const avenue = rnd() < 0.3;
      p.axis = avenue || rnd() < 0.55 ? "z" : "x";
      if (p.axis === "z") { p.line = avenue ? xs[COLS / 2] : xs[Math.floor(rnd() * xs.length)]; p.len = ZMAX; }
      else { p.line = zs[1 + Math.floor(rnd() * (zs.length - 2))]; p.len = X1 - X0; }
      p.dir = rnd() < 0.5 ? 1 : -1;
      p.speed = (avenue ? 1.6 : 0.8) + rnd() * 1.4;
      p.tl = 0.5 + rnd() * 1.4;
      p.pos = fresh ? rnd() * p.len : (p.dir > 0 ? -p.tl : p.len + p.tl);
      p.col = COLS_WARM[Math.floor(rnd() * COLS_WARM.length)];
      p.scr = null;
      return p;
    };
    const N = opt.particles || 150;
    for (let i = 0; i < N; i++) parts.push(spawn({}, true));
    const scripted = [];

    let W = 1, H = 1, F = 1, dpr = 1;
    const cam = { x: 0, y: 1, z: -2, cyw: 1, syw: 0, cp: 1, sp: 0, pitch: 0, yaw: 0 };
    const setCam = (px, py, pz, tx, ty, tz) => {
      cam.x = px; cam.y = py; cam.z = pz;
      const dx = tx - px, dy = ty - py, dz = tz - pz;
      cam.yaw = Math.atan2(dx, dz);
      cam.pitch = Math.atan2(dy, Math.hypot(dx, dz));
      cam.cyw = Math.cos(cam.yaw); cam.syw = Math.sin(cam.yaw);
      cam.cp = Math.cos(cam.pitch); cam.sp = Math.sin(cam.pitch);
    };
    const toCam = (x, y, z, o, i = 0) => {
      const dx = x - cam.x, dy = y - cam.y, dz = z - cam.z;
      const x1 = dx * cam.cyw - dz * cam.syw;
      const z1 = dx * cam.syw + dz * cam.cyw;
      o[i] = x1; o[i + 1] = dy * cam.cp - z1 * cam.sp; o[i + 2] = dy * cam.sp + z1 * cam.cp;
    };
    const A = new Float32Array(3), Bv = new Float32Array(3), T = new Float32Array(3);
    const clip = (a, b) => {
      if (a[2] < NEAR && b[2] < NEAR) return false;
      if (a[2] < NEAR) { const t = (NEAR - a[2]) / (b[2] - a[2]); a[0] += (b[0] - a[0]) * t; a[1] += (b[1] - a[1]) * t; a[2] = NEAR; }
      else if (b[2] < NEAR) { const t = (NEAR - b[2]) / (a[2] - b[2]); b[0] += (a[0] - b[0]) * t; b[1] += (a[1] - b[1]) * t; b[2] = NEAR; }
      return true;
    };
    const sx = (c) => W / 2 + (F * c[0]) / c[2];
    const sy = (c) => H / 2 - (F * c[1]) / c[2];

    const partPos = (p, along, o) => {
      const lane = p.dir > 0 ? 0.09 : -0.09;
      if (p.axis === "z") toCam(p.line + lane, 0.03, along, o);
      else toCam(X0 + along, 0.03, p.line - lane, o);
    };

    function resize() {
      const r = canvas.getBoundingClientRect();
      W = Math.max(1, r.width); H = Math.max(1, r.height);
      dpr = Math.min(window.devicePixelRatio || 1, opt.maxDpr || 1.6);
      canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      F = Math.min(H * 0.98, W * 1.5);
    }

    const DUSK = { top: hex("#121426"), mid: hex("#43314f"), low: hex("#b3664e"), hor: hex("#f4aa5f"), gnd: hex("#09080d") };
    const NIGHT = { top: hex("#05070b"), mid: hex("#06090e"), low: hex("#080b11"), hor: hex("#0a0d14"), gnd: hex("#06080c") };
    const FACE = [hex("#0e0c13"), hex("#15121b"), hex("#1d1823")];
    const FACE_N = [hex("#090c12"), hex("#0c1017"), hex("#10151d")];

    function update(dt) {
      for (const p of parts) {
        p.pos += p.dir * p.speed * dt;
        if (p.scr) {
          if ((p.dir > 0 && p.pos > p.scr.b) || (p.dir < 0 && p.pos < p.scr.a)) p.pos = p.dir > 0 ? p.scr.a : p.scr.b;
        } else if (p.pos < -p.tl - 0.2 || p.pos > p.len + p.tl + 0.2) spawn(p, false);
      }
    }

    function draw(s) {
      const n = s.night, wire = s.wire, flag = s.flag || 0;
      ctx.globalCompositeOperation = "source-over";
      ctx.globalAlpha = 1;
      const hy = H / 2 + F * Math.tan(cam.pitch);

      // Ground
      ctx.fillStyle = mix(DUSK.gnd, NIGHT.gnd, n);
      ctx.fillRect(0, 0, W, H);

      // Sky
      if (hy > 0) {
        const g = ctx.createLinearGradient(0, 0, 0, hy);
        g.addColorStop(0, mix(DUSK.top, NIGHT.top, n));
        g.addColorStop(0.5, mix(DUSK.mid, NIGHT.mid, n));
        g.addColorStop(0.84, mix(DUSK.low, NIGHT.low, n));
        g.addColorStop(0.96, mix(DUSK.hor, NIGHT.hor, n));
        g.addColorStop(1, mix(DUSK.hor, NIGHT.hor, n));
        ctx.fillStyle = g;
        ctx.fillRect(0, 0, W, Math.min(H, hy + 1));
        const horC = DUSK.hor.map((v, k) => Math.round(lerp(v, NIGHT.hor[k], n)));
        const bh = H * 0.16;
        const band = ctx.createLinearGradient(0, hy, 0, hy + bh);
        band.addColorStop(0, `rgba(${horC[0]},${horC[1]},${horC[2]},1)`);
        band.addColorStop(0.35, `rgba(${horC[0]},${horC[1]},${horC[2]},0.45)`);
        band.addColorStop(1, `rgba(${horC[0]},${horC[1]},${horC[2]},0)`);
        ctx.fillStyle = band;
        ctx.fillRect(0, hy, W, bh);
        const day = 1 - n;
        if (day > 0.01) {
          const sunX = W / 2 - F * Math.tan(cam.yaw);
          const rg = ctx.createRadialGradient(sunX, hy, 0, sunX, hy, Math.max(W, H) * 0.55);
          rg.addColorStop(0, `rgba(255,196,120,${0.55 * day})`);
          rg.addColorStop(0.35, `rgba(240,140,90,${0.18 * day})`);
          rg.addColorStop(1, "rgba(240,140,90,0)");
          ctx.fillStyle = rg;
          ctx.fillRect(0, 0, W, H);
          const hz = ctx.createLinearGradient(0, hy, 0, hy + H * 0.14);
          hz.addColorStop(0, `rgba(244,170,95,${0.28 * day})`);
          hz.addColorStop(1, "rgba(244,170,95,0)");
          ctx.fillStyle = hz;
          ctx.fillRect(0, hy, W, H * 0.14);
        }
      }

      // Street network (visible once scanned)
      if (wire > 0.01) {
        ctx.beginPath();
        for (const x of xs) {
          toCam(x, 0, 0, A); toCam(x, 0, ZMAX, Bv);
          if (clip(A, Bv)) { ctx.moveTo(sx(A), sy(A)); ctx.lineTo(sx(Bv), sy(Bv)); }
        }
        for (const z of zs) {
          toCam(X0, 0, z, A); toCam(X1, 0, z, Bv);
          if (clip(A, Bv)) { ctx.moveTo(sx(A), sy(A)); ctx.lineTo(sx(Bv), sy(Bv)); }
        }
        ctx.strokeStyle = `rgba(255,178,63,${0.16 * wire})`;
        ctx.lineWidth = 0.8;
        ctx.stroke();
      }

      // Buildings: depth sort, project corners
      for (const b of blds) { toCam(b.cx, b.h / 2, b.cz, T); b.d = T[2]; }
      blds.sort((a, b) => b.d - a.d);
      const fillA = 1 - wire;
      const winA = (1 - n) * (1 - wire);
      const fc = FACE.map((c, i) => mix(c, FACE_N[i], n));
      const wireLines = new Path2D(), ringLines = new Path2D();
      const dots = [];
      for (const b of blds) {
        b.ok = false;
        if (b.d < NEAR) continue;
        const cs = b.cs, ss = b.ss;
        const X = [b.x1, b.x2, b.x2, b.x1], Z = [b.z1, b.z1, b.z2, b.z2];
        let bad = false;
        for (let i = 0; i < 8; i++) {
          toCam(X[i % 4], i < 4 ? 0 : b.h, Z[i % 4], cs, i * 3);
          if (cs[i * 3 + 2] < NEAR) { bad = true; break; }
          ss[i * 2] = W / 2 + (F * cs[i * 3]) / cs[i * 3 + 2];
          ss[i * 2 + 1] = H / 2 - (F * cs[i * 3 + 1]) / cs[i * 3 + 2];
        }
        if (bad) continue;
        b.ok = true;

        if (fillA > 0.01) {
          ctx.globalAlpha = fillA;
          const quad = (a, c, d, e, col) => {
            ctx.fillStyle = col;
            ctx.beginPath();
            ctx.moveTo(ss[a * 2], ss[a * 2 + 1]); ctx.lineTo(ss[c * 2], ss[c * 2 + 1]);
            ctx.lineTo(ss[d * 2], ss[d * 2 + 1]); ctx.lineTo(ss[e * 2], ss[e * 2 + 1]);
            ctx.closePath(); ctx.fill();
          };
          if (cam.z < b.z1) quad(0, 1, 5, 4, fc[0]);
          if (cam.z > b.z2) quad(2, 3, 7, 6, fc[0]);
          if (cam.x < b.x1) quad(3, 0, 4, 7, fc[1]);
          if (cam.x > b.x2) quad(1, 2, 6, 5, fc[1]);
          if (cam.y > b.h) quad(4, 5, 6, 7, fc[2]);
          if (winA > 0.02 && b.win.length) {
            ctx.globalAlpha = winA;
            for (const w of b.win) {
              let wx, wz;
              if (w.side === 0) { if (cam.z >= b.z1) continue; wx = lerp(b.x1, b.x2, w.u); wz = b.z1 - 0.002; }
              else if (cam.x < b.x1) { wx = b.x1 - 0.002; wz = lerp(b.z1, b.z2, w.u); }
              else if (cam.x > b.x2) { wx = b.x2 + 0.002; wz = lerp(b.z1, b.z2, w.u); }
              else continue;
              toCam(wx, w.v, wz, T);
              if (T[2] < NEAR) continue;
              const sz = clamp((F * 0.024) / T[2], 0.7, 3);
              ctx.fillStyle = w.warm ? "#ffc779" : "#ffe7c2";
              ctx.fillRect(sx(T) - sz / 2, sy(T) - sz / 2, sz, sz * 1.3);
            }
          }
          ctx.globalAlpha = 1;
        }

        if (wire > 0.01) {
          const E = [0, 1, 1, 2, 2, 3, 3, 0, 4, 5, 5, 6, 6, 7, 7, 4, 0, 4, 1, 5, 2, 6, 3, 7];
          for (let i = 0; i < E.length; i += 2) {
            wireLines.moveTo(ss[E[i] * 2], ss[E[i] * 2 + 1]);
            wireLines.lineTo(ss[E[i + 1] * 2], ss[E[i + 1] * 2 + 1]);
          }
          if (b.h > 0.7) {
            for (let y = 0.32; y < b.h - 0.12; y += 0.32) {
              const t = y / b.h;
              for (let i = 0; i < 4; i++) {
                const j = (i + 1) % 4;
                for (const [k, o] of [[i, A], [j, Bv]]) {
                  o[0] = lerp(cs[k * 3], cs[(k + 4) * 3], t);
                  o[1] = lerp(cs[k * 3 + 1], cs[(k + 4) * 3 + 1], t);
                  o[2] = lerp(cs[k * 3 + 2], cs[(k + 4) * 3 + 2], t);
                }
                ringLines.moveTo(sx(A), sy(A)); ringLines.lineTo(sx(Bv), sy(Bv));
              }
            }
          }
          for (let i = 4; i < 8; i++) dots.push(ss[i * 2], ss[i * 2 + 1]);
        }
      }

      if (wire > 0.01) {
        ctx.lineWidth = 0.7;
        ctx.strokeStyle = `rgba(150,170,205,${0.14 * wire})`;
        ctx.stroke(ringLines);
        ctx.strokeStyle = `rgba(214,226,250,${0.42 * wire})`;
        ctx.stroke(wireLines);
        ctx.fillStyle = `rgba(236,242,255,${0.8 * wire})`;
        for (let i = 0; i < dots.length; i += 2) ctx.fillRect(dots[i] - 0.8, dots[i + 1] - 0.8, 1.6, 1.6);
      }

      // Payments, batched by colour and width (no per-particle gradients)
      ctx.globalCompositeOperation = "lighter";
      ctx.lineCap = "round";
      const amber = [255, 178, 63], red = [255, 91, 58];
      const buckets = new Map();
      for (const p of parts) {
        partPos(p, p.pos, A);
        partPos(p, p.pos - p.dir * p.tl, Bv);
        p.vis = false;
        if (!clip(A, Bv)) continue;
        const hx = sx(A), hyy = sy(A), tx = sx(Bv), ty = sy(Bv);
        if ((hx < -50 && tx < -50) || (hx > W + 50 && tx > W + 50) || (hyy < -50 && ty < -50) || (hyy > H + 50 && ty > H + 50)) continue;
        p.vis = true; p.sx = hx; p.sy = hyy; p.sz = A[2]; p.tx = tx; p.ty = ty;
        const flagged = p.scr && p.scr.flag && flag > 0;
        const w = Math.round(clamp((F * 0.03) / A[2], 0.6, 3.6) * 2) / 2;
        const key = (flagged ? "f" : COLS_WARM.indexOf(p.col)) + "|" + w;
        let bk = buckets.get(key);
        if (!bk) { bk = { col: p.col, flagged, w, tail: new Path2D(), mid: new Path2D(), head: new Path2D() }; buckets.set(key, bk); }
        const mx = lerp(tx, hx, 0.45), my = lerp(ty, hyy, 0.45);
        bk.tail.moveTo(tx, ty); bk.tail.lineTo(mx, my);
        bk.mid.moveTo(mx, my); bk.mid.lineTo(hx, hyy);
        bk.head.moveTo(hx + w * 0.85, hyy); bk.head.arc(hx, hyy, w * 0.85, 0, Math.PI * 2);
      }
      for (const bk of buckets.values()) {
        let col = bk.col;
        if (wire > 0) col = col.map((v, i) => lerp(v, amber[i], wire * 0.75));
        if (bk.flagged) col = col.map((v, i) => lerp(v, red[i], flag));
        const c = `${col[0] | 0},${col[1] | 0},${col[2] | 0}`;
        ctx.lineWidth = bk.w;
        ctx.strokeStyle = `rgba(${c},0.22)`; ctx.stroke(bk.tail);
        ctx.strokeStyle = `rgba(${c},0.85)`; ctx.stroke(bk.mid);
        ctx.fillStyle = `rgba(${c},0.95)`; ctx.fill(bk.head);
      }
      ctx.globalCompositeOperation = "source-over";
    }

    /* Targets for the detection boxes, chosen so they land in open screen space */
    const nearestBuilding = (fx, fy, minH, used) => {
      let best = null, bd = Infinity;
      for (const b of blds) {
        if (b.h < minH || used.includes(b)) continue;
        toCam(b.cx, b.h, b.cz, T);
        if (T[2] < 1) continue;
        const d = Math.hypot(sx(T) - fx * W, sy(T) - fy * H);
        if (d < bd) { bd = d; best = b; }
      }
      return best;
    };
    const addScripted = (fx, fy, flagB) => {
      let best = null, bd = Infinity;
      for (const [axis, lines] of [["z", xs], ["x", zs.slice(1, -1)]]) {
        for (const line of lines) {
          const len = axis === "z" ? ZMAX : X1 - X0;
          for (let s = 1; s < len - 1; s += 0.35) {
            if (axis === "z") toCam(line, 0, s, T); else toCam(X0 + s, 0, line, T);
            if (T[2] < 1.5) continue;
            const d = Math.hypot(sx(T) - fx * W, sy(T) - fy * H);
            if (d < bd) { bd = d; best = { axis, line, s, len }; }
          }
        }
      }
      if (!best) return null;
      const p = { axis: best.axis, line: best.line, len: best.len, dir: 1, speed: 0.32, tl: 1.4, col: COLS_WARM[0] };
      p.scr = { a: best.s - 0.9, b: best.s + 0.9, flag: !!flagB };
      p.pos = best.s;
      parts.push(p); scripted.push(p);
      return p;
    };
    const flagStreams = (b) => {
      const out = [];
      const ix = xs.reduce((m, x) => (Math.abs(x - b.x1) < Math.abs(m - b.x1) ? x : m), xs[0]);
      const iz = zs.reduce((m, z) => (Math.abs(z - b.z1) < Math.abs(m - b.z1) ? z : m), zs[0]);
      const mk = (axis, line, end, dir, off) => {
        const len = axis === "z" ? ZMAX : X1 - X0;
        const p = { axis, line, len, dir, speed: 0.42, tl: 0.7, col: COLS_WARM[3] };
        p.scr = dir > 0 ? { a: end - 1.6, b: end, flag: true } : { a: end, b: end + 1.6, flag: true };
        p.pos = lerp(p.scr.a, p.scr.b, off);
        parts.push(p); scripted.push(p); out.push(p);
      };
      mk("z", ix, b.cz, 1, 0.1);
      mk("z", ix, b.cz, -1, 0.55);
      mk("x", iz, b.cx - X0, 1, 0.35);
      mk("x", iz, b.cx - X0, -1, 0.8);
      return out;
    };

    let targets = [];
    function pickTargets(camAt) {
      for (const p of scripted) parts.splice(parts.indexOf(p), 1);
      scripted.length = 0;
      camAt();
      const used = [];
      const narrow = W < 700;
      const b1 = nearestBuilding(narrow ? 0.7 : 0.66, narrow ? 0.26 : 0.27, 2, used); used.push(b1);
      const b2 = nearestBuilding(narrow ? 0.38 : 0.47, narrow ? 0.42 : 0.47, 2.6, used); used.push(b2);
      const p1 = narrow ? null : addScripted(0.8, 0.58);
      const p2 = narrow ? null : addScripted(0.3, 0.22);
      flagStreams(b2);
      targets = [
        { kind: "b", ref: b1, label: "Client · ID verified", icon: "check" },
        { kind: "b", ref: b2, label: "4 cash deposits · 24h · $9,600 avg", flag: true, icon: "gap" },
        { kind: "p", ref: p1, label: "Intl EFT · $14,500 · Reportable", icon: "gap" },
        { kind: "p", ref: p2, label: "Name screen · Clear", icon: "check" },
      ].filter((t) => t.ref);
      return targets;
    }
    function boxes() {
      return targets.map((t) => {
        if (t.kind === "b") {
          const b = t.ref;
          if (!b.ok) return null;
          let x1 = Infinity, y1 = Infinity, x2 = -Infinity, y2 = -Infinity;
          for (let i = 0; i < 8; i++) { const x = b.ss[i * 2], y = b.ss[i * 2 + 1]; x1 = Math.min(x1, x); x2 = Math.max(x2, x); y1 = Math.min(y1, y); y2 = Math.max(y2, y); }
          const pad = t.flag ? 16 : 10;
          return { x: x1 - pad, y: y1 - pad, w: x2 - x1 + pad * 2, h: y2 - y1 + pad * 2 };
        }
        const p = t.ref;
        if (!p.vis) return null;
        const pad = clamp((F * 0.06) / p.sz, 12, 26);
        const x1 = Math.min(p.sx, p.tx) - pad, x2 = Math.max(p.sx, p.tx) + pad;
        const y1 = Math.min(p.sy, p.ty) - pad, y2 = Math.max(p.sy, p.ty) + pad;
        return { x: x1, y: y1, w: Math.max(44, x2 - x1), h: Math.max(44, y2 - y1) };
      });
    }

    function pickOne(camAt, fx, fy, label, flag) {
      camAt();
      const b = nearestBuilding(fx, fy, 1.4, []);
      targets = b ? [{ kind: "b", ref: b, label, flag, icon: flag ? "gap" : "check" }] : [];
      return targets;
    }

    return { resize, update, draw, setCam, pickTargets, pickOne, boxes, get size() { return [W, H]; } };
  }

  /* ------------------------------------------------------------------
     Hero: scroll drives the camera from street level at dusk to a
     scanned overhead view, then detection, then the tile grid.
  ------------------------------------------------------------------ */
  const KEYS = [
    [0.0, 0, 0.5, -1.9, 0, 0.95, 20],
    [0.12, 0, 0.58, -1.3, 0, 0.9, 20],
    [0.46, -6.5, 6.2, -2.4, 0.2, 0, 9],
    [0.78, -7.8, 11.2, 3.2, 0.4, 0, 11.5],
    [1.0, -6.2, 9.2, 6.0, 0.4, 0, 12.5],
  ];
  const camAtP = (city, p) => {
    let i = 0;
    while (i < KEYS.length - 2 && p > KEYS[i + 1][0]) i++;
    const a = KEYS[i], b = KEYS[i + 1];
    const t = easeIO(clamp((p - a[0]) / (b[0] - a[0]), 0, 1));
    city.setCam(lerp(a[1], b[1], t), lerp(a[2], b[2], t), lerp(a[3], b[3], t), lerp(a[4], b[4], t), lerp(a[5], b[5], t), lerp(a[6], b[6], t));
  };

  const hero = $("[data-hero]");
  const heroCanvas = $("[data-hero-canvas]");
  if (hero && heroCanvas && heroCanvas.getContext) {
    const city = City(heroCanvas, { seed: 23, particles: innerWidth < 700 ? 100 : 150, maxDpr: 1.25 });
    const boxLayer = $("[data-hero-boxes]");
    const beats = { a: $('[data-beat="a"]'), b: $('[data-beat="b"]'), c: $('[data-beat="c"]') };
    const note = $("[data-hero-note]"), cue = $("[data-hero-cue]");
    const tiles = $("[data-tiles]");
    let p = 0, visible = true, dirty = true, last = performance.now(), boxEls = [], tgts = [], boxesShown = true;

    const icon = (id) => `<svg aria-hidden="true"><use href="#i-${id}"/></svg>`;
    const buildBoxes = () => {
      boxLayer.innerHTML = "";
      boxEls = tgts.map((t) => {
        const el = document.createElement("div");
        el.className = "dbox" + (t.flag ? " is-flag" : "");
        el.innerHTML = `<div class="dbox-tag">${icon(t.icon)}<span>${t.label}</span></div>`;
        boxLayer.appendChild(el);
        return el;
      });
    };
    const buildTiles = () => {
      const [w, h] = city.size;
      const size = w > 700 ? 78 : 56;
      const cols = Math.ceil(w / size), rows = Math.ceil(h / size);
      tiles.style.gridTemplateColumns = `repeat(${cols}, 1fr)`;
      tiles.style.gridTemplateRows = `repeat(${rows}, 1fr)`;
      const frag = document.createDocumentFragment();
      const maxD = Math.hypot(cols / 2, rows / 2);
      let s = 7;
      const r = () => (s = (s * 16807) % 2147483647) / 2147483647;
      for (let y = 0; y < rows; y++) for (let x = 0; x < cols; x++) {
        const d = clamp(Math.hypot(x + 0.5 - cols / 2, y + 0.5 - rows / 2) / maxD * 0.82 + r() * 0.18, 0, 1);
        const el = document.createElement("i");
        el.className = "tile" + (r() < 0.06 ? " is-lit" : "");
        el.style.setProperty("--d", d.toFixed(3));
        frag.appendChild(el);
      }
      tiles.replaceChildren(frag);
    };
    const resize = () => {
      city.resize();
      tgts = city.pickTargets(() => camAtP(city, 0.7));
      buildBoxes();
      buildTiles();
      dirty = true;
    };
    let heroTop = 0, heroTotal = 1, tagW = [];
    const measure = () => {
      heroTop = hero.getBoundingClientRect().top + scrollY;
      heroTotal = Math.max(1, hero.offsetHeight - innerHeight);
      tagW = boxEls.map((el) => el.firstElementChild.offsetWidth);
    };
    const readScroll = () => {
      const np = clamp((scrollY - heroTop) / heroTotal, 0, 1);
      if (np !== p) { p = np; dirty = true; }
    };
    const setBeat = (el, on) => el && el.classList.toggle("is-on", on);
    let lastT = "";

    const frame = (now) => {
      const dt = Math.min(0.05, (now - last) / 1000);
      last = now;
      if (visible) {
        const still = reduceMQ.matches;
        if (!still || dirty) {
          if (!still) city.update(dt);
          camAtP(city, p);
          const covered = p > 0.985;
          const detect = smooth(0.52, 0.6, p) * (1 - smooth(0.82, 0.88, p));
          if (!covered) city.draw({ night: smooth(0.06, 0.36, p), wire: smooth(0.14, 0.42, p), flag: detect });
          if (detect > 0.01 || boxesShown) {
            const bx = city.boxes();
            boxesShown = detect > 0.01;
            boxEls.forEach((el, i) => {
              const b = bx[i];
              el.classList.toggle("is-on", !!b && detect > 0.5);
              if (b && boxesShown) {
                el.style.transform = `translate3d(${b.x.toFixed(1)}px, ${b.y.toFixed(1)}px, 0)`;
                el.style.width = `${b.w.toFixed(1)}px`;
                el.style.height = `${b.h.toFixed(1)}px`;
                el.classList.toggle("tag-left", b.x + (tagW[i] || 0) > city.size[0] - 24);
              }
            });
          }
          setBeat(beats.a, p < 0.14);
          setBeat(beats.b, p >= 0.22 && p < 0.47);
          setBeat(beats.c, p >= 0.54 && p < 0.8);
          note.classList.toggle("is-on", p > 0.5 && p < 0.84);
          cue.classList.toggle("is-off", p > 0.02);
          const tv = smooth(0.8, 0.975, p).toFixed(3);
          if (tv !== lastT) { tiles.style.setProperty("--t", tv); lastT = tv; }
          dirty = false;
        }
      }
      requestAnimationFrame(frame);
    };

    new IntersectionObserver(([e]) => { visible = e.isIntersecting; dirty = true; }).observe(hero);
    addEventListener("scroll", readScroll, { passive: true });
    let rt;
    addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(() => { resize(); measure(); readScroll(); }, 120); });
    reduceMQ.addEventListener?.("change", () => { dirty = true; });
    resize();
    measure();
    readScroll();
    document.fonts?.ready.then(() => { measure(); readScroll(); });
    addEventListener("load", () => { measure(); readScroll(); });
    requestAnimationFrame(frame);
  }

  /* Inner page hero: the scanned city, one box on the subject */
  const pageCanvas = $("[data-page-canvas]");
  if (pageCanvas && pageCanvas.getContext) {
    const city = City(pageCanvas, { seed: 17 + pageCanvas.dataset.label.length, particles: innerWidth < 700 ? 80 : 130, maxDpr: 1.5 });
    const layer = $("[data-page-boxes]");
    const label = pageCanvas.dataset.label, flag = pageCanvas.hasAttribute("data-flag");
    let on = true, a = 0.55, last = performance.now(), el = null;
    const camAt = (ang) => () => { const cz = 12, r = 12.5; city.setCam(Math.sin(ang) * r, 8.2, cz - Math.cos(ang) * r, 0.5, 0, cz + 1); };
    const render = (dt) => {
      a += dt * 0.012;
      camAt(a)();
      city.update(dt);
      city.draw({ night: 1, wire: 1, flag: flag ? 1 : 0 });
      const b = city.boxes()[0];
      if (el) {
        el.classList.toggle("is-on", !!b);
        if (b) {
          el.style.transform = `translate3d(${b.x.toFixed(1)}px, ${b.y.toFixed(1)}px, 0)`;
          el.style.width = `${b.w.toFixed(1)}px`;
          el.style.height = `${b.h.toFixed(1)}px`;
        }
      }
    };
    const size = () => {
      city.resize();
      const narrow = city.size[0] < 700;
      const t = city.pickOne(camAt(a), narrow ? 0.62 : 0.7, narrow ? 0.3 : 0.38, label, flag);
      layer.innerHTML = "";
      el = null;
      if (t.length) {
        el = document.createElement("div");
        el.className = "dbox" + (flag ? " is-flag" : "");
        el.innerHTML = `<div class="dbox-tag"><svg aria-hidden="true"><use href="#i-${flag ? "gap" : "check"}"/></svg><span>${label}</span></div>`;
        layer.appendChild(el);
      }
      render(0);
    };
    const loop = (now) => {
      const dt = Math.min(0.05, (now - last) / 1000);
      last = now;
      if (on && !reduceMQ.matches) render(dt);
      requestAnimationFrame(loop);
    };
    new IntersectionObserver(([e]) => { on = e.isIntersecting; }).observe(pageCanvas);
    let rt;
    addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(size, 120); });
    size();
    requestAnimationFrame(loop);
  }

  /* Closing scene: the scanned city, turning slowly */
  const closeCanvas = $("[data-close-canvas]");
  if (closeCanvas && closeCanvas.getContext) {
    const city = City(closeCanvas, { seed: 41, particles: innerWidth < 700 ? 70 : 110, maxDpr: 1.4 });
    let on = false, a = 0.4, last = performance.now();
    const render = (dt) => {
      a += dt * 0.025;
      const cx = 0, cz = 14, r = 13;
      city.setCam(cx + Math.sin(a) * r, 7.4, cz - Math.cos(a) * r, 0, 0.5, cz);
      city.update(dt);
      city.draw({ night: 1, wire: 1, flag: 0 });
    };
    const loop = (now) => {
      const dt = Math.min(0.05, (now - last) / 1000);
      last = now;
      if (on && !reduceMQ.matches) render(dt);
      requestAnimationFrame(loop);
    };
    const size = () => { city.resize(); render(0); };
    new IntersectionObserver(([e]) => { on = e.isIntersecting; }).observe(closeCanvas);
    addEventListener("resize", size);
    size();
    requestAnimationFrame(loop);
  }

  /* ------------------------------------------------------------------
     Linework art for cards and service modules
  ------------------------------------------------------------------ */
  const pt = (x, y) => `${+x.toFixed(1)} ${+y.toFixed(1)}`;
  const isoBox = (cx, cy, a, b, h, floors = 0) => {
    const top = `M${pt(cx, cy - h - b)}L${pt(cx + a, cy - h)}L${pt(cx, cy - h + b)}L${pt(cx - a, cy - h)}Z`;
    const vis = `${top}M${pt(cx - a, cy - h)}V${cy}L${pt(cx, cy + b)}L${pt(cx + a, cy)}V${cy - h}M${pt(cx, cy - h + b)}V${cy + b}`;
    const hid = `M${pt(cx - a, cy)}L${pt(cx, cy - b)}L${pt(cx + a, cy)}M${pt(cx, cy - b)}V${cy - h - b}`;
    let fl = "";
    for (let i = 1; i <= floors; i++) { const k = (h * i) / (floors + 1); fl += `M${pt(cx - a, cy - k)}L${pt(cx, cy + b - k)}L${pt(cx + a, cy - k)}`; }
    const face = `M${pt(cx - a, cy - h)}L${pt(cx, cy - h + b)}L${pt(cx + a, cy - h)}V${cy}L${pt(cx, cy + b)}L${pt(cx - a, cy)}Z`;
    return `<path class="art-face" d="${face}"/><path class="art-dim" d="${hid}"/><path class="art-line" d="${vis}${fl}"/>`;
  };
  const grid = () => {
    let d = "";
    for (let c = -220; c <= 220; c += 44) d += `M${pt(-20, c - 11.3)}L${pt(340, c + 192.8)}`;
    for (let c = -20; c <= 420; c += 44) d += `M${pt(-20, c + 11.3)}L${pt(340, c - 192.8)}`;
    return `<path d="${d}" fill="none" stroke="rgba(226,232,242,0.06)" stroke-width="1" vector-effect="non-scaling-stroke"/>`;
  };
  const bracket = (x1, y1, x2, y2, l = 12) =>
    `<path class="art-amber" d="M${x1} ${y1 + l}V${y1}H${x1 + l}M${x2 - l} ${y1}H${x2}V${y1 + l}M${x2} ${y2 - l}V${y2}H${x2 - l}M${x1 + l} ${y2}H${x1}V${y2 - l}"/>`;
  const trail = (d, delay = 0) => `<path class="art-line" d="${d}" style="stroke:rgba(255,178,63,.22)"/><path class="art-trail" d="${d}" pathLength="286" style="animation-delay:${delay}s"/>`;
  let gid = 0;
  const scan = (x, y, w) => {
    const id = `scan-grad-${++gid}`;
    return `<defs><linearGradient id="${id}" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#ffb23f" stop-opacity=".5"/><stop offset="1" stop-color="#ffb23f" stop-opacity="0"/></linearGradient></defs>
      <g class="art-scanbar"><rect x="${x}" y="${y - 26}" width="${w}" height="26" fill="url(#${id})"/><rect x="${x}" y="${y}" width="${w}" height="1.5" fill="#ffb23f"/></g>`;
  };
  const ART = {
    one: () => grid() + trail(`M${pt(-10, 196)}L${pt(114, 125)}`) + isoBox(160, 124, 46, 26, 62, 2) + bracket(98, 22, 222, 162) + `<circle class="art-dot" cx="114" cy="125" r="3"/>`,
    many: () => grid() + trail("M90 137L170 109L250 145", 0) + trail("M250 145L90 137", 1.4) + isoBox(90, 120, 30, 17, 44, 1) + isoBox(170, 92, 30, 17, 70, 2) + isoBox(250, 128, 30, 17, 36) + `<circle class="art-dot" cx="90" cy="137" r="3"/><circle class="art-dot" cx="170" cy="109" r="3"/><circle class="art-dot" cx="250" cy="145" r="3"/>`,
    scan: () => grid() + isoBox(160, 132, 50, 28, 80, 3) + `<g style="clip-path:inset(0)">${scan(104, 32, 112)}</g>` + bracket(96, 18, 224, 170),
    address: () => grid() + `<path class="art-amber" d="M96 118L140 143L96 168L52 143Z" stroke-dasharray="4 4"/><path class="art-amber" d="M96 143V96"/><circle cx="96" cy="90" r="6" class="art-amber"/><circle class="art-dot" cx="96" cy="143" r="3"/>` + isoBox(206, 118, 38, 22, 58, 2),
    register: () => grid() + isoBox(160, 124, 40, 23, 58, 2) + bracket(106, 28, 214, 158) + `<rect x="196" y="16" width="24" height="18" rx="3" fill="#ffb23f"/><path d="m202 25 4 4 8-8" fill="none" stroke="#1d1304" stroke-width="1.8"/>`,
    programme: () => {
      let s = grid();
      const ys = [150, 126, 102, 78, 54];
      s += `<path class="art-dim" d="M90 ${ys[0]}V${ys[4]}M230 ${ys[0]}V${ys[4]}M160 ${ys[0] + 36}V${ys[4] + 36}"/>`;
      ys.forEach((y, i) => {
        const last = i === ys.length - 1;
        s += `<path class="${last ? "art-amber" : "art-line"}" d="M160 ${y - 36}L230 ${y}L160 ${y + 36}L90 ${y}Z" style="${last ? "" : "fill:rgba(255,255,255,.025)"}"/>`;
      });
      return s;
    },
    review: () => grid() + isoBox(160, 134, 52, 30, 76, 3) + `<g>${scan(102, 36, 116)}</g>` + bracket(94, 20, 226, 172),
    training: () => grid() + trail(`M${pt(40, 168)}L${pt(290, 26)}`) + [[78, 146], [130, 116], [182, 87], [234, 57]].map(([x, y], i) => isoBox(x, y, 18, 10, 26 + (i % 2) * 8)).join(""),
  };
  $$("[data-art]").forEach((el) => {
    const make = ART[el.dataset.art];
    if (make) el.insertAdjacentHTML("afterbegin", `<svg viewBox="0 0 320 180" preserveAspectRatio="xMidYMid slice" aria-hidden="true">${make()}</svg>`);
  });

  /* ------------------------------------------------------------------
     Odometers
  ------------------------------------------------------------------ */
  const makeOdo = (el, value) => {
    el.textContent = "";
    const sr = document.createElement("span");
    sr.className = "sr";
    sr.textContent = value;
    const vis = document.createElement("span");
    vis.className = "odo";
    vis.setAttribute("aria-hidden", "true");
    const cols = [];
    [...value].forEach((ch) => {
      if (/\d/.test(ch)) {
        const col = document.createElement("span");
        col.className = "odo-col";
        const strip = document.createElement("span");
        for (let k = 0; k < 20; k++) { const d = document.createElement("span"); d.dataset.d = k % 10; strip.appendChild(d); }
        col.appendChild(strip);
        vis.appendChild(col);
        cols.push({ strip, d: +ch });
      } else {
        const s = document.createElement("span");
        s.className = "odo-ch";
        s.dataset.d = ch;
        vis.appendChild(s);
      }
    });
    el.replaceWith(vis);
    vis.before(sr);
    return { roll: () => cols.forEach((c, i) => { c.strip.style.transitionDelay = `${i * 90}ms`; c.strip.style.transform = `translateY(-${10 + c.d}em)`; }) };
  };
  const odos = new Map();
  $$("[data-odo]").forEach((el) => {
    const row = el.closest("[data-reveal]");
    odos.set(row, makeOdo(el, el.dataset.odo));
  });

  /* Reveal */
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      e.target.classList.add("is-in");
      const o = odos.get(e.target);
      if (o) setTimeout(o.roll, 150);
      io.unobserve(e.target);
    });
  }, { threshold: 0.25 });
  $$("[data-reveal]").forEach((el) => io.observe(el));

  /* ------------------------------------------------------------------
     Sector ticker: duplicate the row for a seamless loop
  ------------------------------------------------------------------ */
  const tick = $(".ticker-row");
  if (tick) $$("li", tick).forEach((li) => { const c = li.cloneNode(true); c.setAttribute("aria-hidden", "true"); tick.appendChild(c); });

  /* ------------------------------------------------------------------
     Navigation theme and menu
  ------------------------------------------------------------------ */
  const nav = $("[data-nav]");
  const themed = $$("[data-theme]");
  let bands = [];
  const measureBands = () => {
    bands = themed.map((el) => { const r = el.getBoundingClientRect(); return [r.top + scrollY, r.bottom + scrollY, el.dataset.theme]; });
  };
  let navTick = false;
  const navTheme = () => {
    navTick = false;
    const y = scrollY + 44;
    const s = bands.find((b) => b[0] <= y && b[1] > y);
    nav.classList.toggle("is-light", !!s && s[2] === "light");
  };
  addEventListener("scroll", () => { if (!navTick) { navTick = true; requestAnimationFrame(navTheme); } }, { passive: true });
  const remeasure = () => { measureBands(); navTheme(); };
  addEventListener("resize", remeasure);
  addEventListener("load", remeasure);
  document.fonts?.ready.then(remeasure);
  if ("ResizeObserver" in window) new ResizeObserver(remeasure).observe(document.body);
  remeasure();

  /* Mega menu: panels open on click or hover; the preview follows the pointed item */
  const megaItems = $$(".mega-item");
  const closeMega = (except) => {
    megaItems.forEach((it) => {
      if (it === except) return;
      const t = $("[data-mega-trigger]", it), pnl = $("[data-mega-panel]", it);
      t.setAttribute("aria-expanded", "false");
      pnl.hidden = true;
    });
    if (!except) nav.classList.remove("is-open");
  };
  const openMega = (it) => {
    const t = $("[data-mega-trigger]", it), pnl = $("[data-mega-panel]", it);
    if (t.getAttribute("aria-expanded") === "true") return;
    closeMega(it);
    t.setAttribute("aria-expanded", "true");
    pnl.hidden = false;
    pnl.classList.remove("is-entering"); void pnl.offsetWidth; pnl.classList.add("is-entering");
    nav.classList.add("is-open");
  };
  const hoverable = matchMedia("(hover: hover)");
  megaItems.forEach((it) => {
    const t = $("[data-mega-trigger]", it), pnl = $("[data-mega-panel]", it);
    const links = $$(".mega-link", pnl);
    const title = $("[data-mega-title]", pnl), desc = $("[data-mega-desc]", pnl), more = $("[data-mega-more]", pnl);
    const preview = (a) => {
      links.forEach((l) => l.classList.toggle("is-active", l === a));
      title.textContent = a.dataset.title;
      desc.textContent = a.dataset.desc;
      more.href = a.getAttribute("href");
    };
    if (links[0]) preview(links[0]);
    links.forEach((a) => {
      a.addEventListener("mouseenter", () => preview(a));
      a.addEventListener("focus", () => preview(a));
      if (location.pathname.endsWith("/" + a.getAttribute("href"))) a.setAttribute("aria-current", "page");
    });
    t.addEventListener("click", () => (t.getAttribute("aria-expanded") === "true" ? closeMega() : openMega(it)));
    t.addEventListener("keydown", (e) => {
      if (e.key === "ArrowDown") { e.preventDefault(); openMega(it); links[0]?.focus(); }
    });
    pnl.addEventListener("keydown", (e) => {
      const i = links.indexOf(document.activeElement);
      if (e.key === "ArrowDown" && i > -1) { e.preventDefault(); links[(i + 1) % links.length].focus(); }
      if (e.key === "ArrowUp" && i > -1) { e.preventDefault(); links[(i - 1 + links.length) % links.length].focus(); }
    });
    let leave;
    it.addEventListener("mouseenter", () => { if (hoverable.matches) { clearTimeout(leave); openMega(it); } });
    it.addEventListener("mouseleave", () => { if (hoverable.matches) leave = setTimeout(() => closeMega(), 220); });
    it.addEventListener("focusout", (e) => { if (!it.contains(e.relatedTarget)) closeMega(); });
  });
  addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    const open = megaItems.find((it) => $("[data-mega-trigger]", it).getAttribute("aria-expanded") === "true");
    if (open) { closeMega(); $("[data-mega-trigger]", open).focus(); }
  });
  document.addEventListener("click", (e) => { if (!e.target.closest(".mega-item")) closeMega(); });

  const menu = $("[data-menu]");
  const opener = $("[data-menu-open]");
  const closeMenu = (restore = true) => {
    menu.hidden = true;
    menu.classList.remove("is-open");
    opener.setAttribute("aria-expanded", "false");
    document.documentElement.style.overflow = "";
    if (restore) opener.focus();
  };
  opener.addEventListener("click", () => {
    menu.hidden = false;
    menu.classList.add("is-open");
    opener.setAttribute("aria-expanded", "true");
    document.documentElement.style.overflow = "hidden";
    $(".menu-links a", menu).focus();
  });
  $("[data-menu-close]").addEventListener("click", () => closeMenu());
  $$("[data-menu-link]").forEach((a) => a.addEventListener("click", () => closeMenu(false)));
  menu.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeMenu();
    if (e.key !== "Tab") return;
    const f = $$("a, button", menu);
    if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f.at(-1).focus(); }
    else if (!e.shiftKey && document.activeElement === f.at(-1)) { e.preventDefault(); f[0].focus(); }
  });

  /* ------------------------------------------------------------------
     Tabs (shared)
  ------------------------------------------------------------------ */
  const tablist = (list, onSelect) => {
    const tabs = $$('[role="tab"]', list);
    const select = (tab, focus, silent) => {
      tabs.forEach((t) => {
        const on = t === tab;
        const was = t.getAttribute("aria-selected") === "true";
        t.setAttribute("aria-selected", String(on));
        t.tabIndex = on ? 0 : -1;
        const panel = $("#" + t.getAttribute("aria-controls"));
        panel.hidden = !on;
        if (on && !was) { panel.classList.remove("is-entering"); void panel.offsetWidth; panel.classList.add("is-entering"); }
      });
      if (focus) tab.focus();
      if (!silent && onSelect) onSelect(tabs.indexOf(tab));
    };
    tabs.forEach((t, i) => {
      t.addEventListener("click", () => select(t));
      t.addEventListener("keydown", (e) => {
        const k = e.key;
        let j = null;
        if (k === "ArrowRight" || k === "ArrowDown") j = (i + 1) % tabs.length;
        if (k === "ArrowLeft" || k === "ArrowUp") j = (i - 1 + tabs.length) % tabs.length;
        if (k === "Home") j = 0;
        if (k === "End") j = tabs.length - 1;
        if (j !== null) { e.preventDefault(); select(tabs[j], true); }
      });
    });
    // Panels ship visible so the answers are readable without JS; hide the unselected ones here
    const cur = tabs.find((t) => t.getAttribute("aria-selected") === "true") || tabs[0];
    tabs.forEach((t) => { $("#" + t.getAttribute("aria-controls")).hidden = t !== cur; });
    return { select: (i, silent) => select(tabs[i], false, silent), tabs };
  };

  const faqTabs = $("[data-faq-tabs]");
  if (faqTabs) tablist(faqTabs);

  /* ------------------------------------------------------------------
     Gates: a payment travels through four checkpoints
  ------------------------------------------------------------------ */
  const gates = $("[data-gates]");
  const corridor = $("[data-corridor]");
  if (gates && corridor) {
    const GX = [150, 450, 750, 1050];
    const NAMES = $$('[data-gate-tabs] [role="tab"]').map((t) => t.textContent.trim());
    const Q = GX.map((x) => (x - 20) / 1160);
    let floor = "";
    for (let x = 20; x <= 1180; x += 40) floor += `M${x} 204L${x + 22} 178`;
    let g = "";
    GX.forEach((x, i) => {
      g += `<g class="cor-g" data-g="${i}">
        <path class="cor-gate-back" d="M${x - 24} 178V38H${x + 68}V178"/>
        <path class="cor-gate" d="M${x - 46} 204V64H${x + 46}V204M${x - 46} 64L${x - 24} 38M${x + 46} 64L${x + 68} 38M${x + 46} 204L${x + 68} 178"/>
        <rect class="cor-scan" x="${x - 45}" y="64" width="90" height="12" style="--scan-h:128px"/>
        <text class="cor-label" x="${x - 46}" y="232">0${i + 1} ${NAMES[i]}</text>
      </g>`;
    });
    corridor.innerHTML = `<svg viewBox="0 0 1200 240" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
      <defs><linearGradient id="pulse-tail" x1="0" x2="1"><stop offset="0" stop-color="#ffb23f" stop-opacity="0"/><stop offset="1" stop-color="#ffb23f" stop-opacity=".9"/></linearGradient></defs>
      <path class="cor-floor" d="M20 178H1200M20 204H1180${floor}"/>
      <path class="cor-rail" d="M20 191H1180"/>
      <line class="cor-done" x1="20" y1="191" x2="20" y2="191" data-done/>
      ${g}
      <g data-pulse transform="translate(20 191)"><rect x="-120" y="-1.5" width="120" height="3" fill="url(#pulse-tail)"/><circle class="cor-halo" r="14"/><circle class="cor-pulse" r="5"/></g>
    </svg>`;
    const done = $("[data-done]", corridor), pulse = $("[data-pulse]", corridor);
    const gEls = $$(".cor-g", corridor);
    const pinned = matchMedia("(min-width: 821px)");
    let active = -1, shownX = 20, tween = 0;

    const svgEl = $("svg", corridor);
    const place = (x) => {
      shownX = x;
      // Narrow screens see a 520-unit window that follows the pulse
      const vx = pinned.matches ? 0 : clamp(x - 300, 0, 680);
      svgEl.setAttribute("viewBox", pinned.matches ? "0 0 1200 240" : `${vx.toFixed(1)} 0 520 240`);
      done.setAttribute("x2", x.toFixed(1));
      pulse.setAttribute("transform", `translate(${x.toFixed(1)} 191)`);
      gEls.forEach((el, i) => el.classList.toggle("is-on", x >= GX[i] - 2));
    };
    const tabs = tablist($("[data-gate-tabs]"), (i) => {
      if (pinned.matches) {
        const r = gates.getBoundingClientRect();
        const total = gates.offsetHeight - innerHeight;
        const top = scrollY + r.top + (Q[i] + 0.03) * total;
        scrollTo({ top, behavior: reduceMQ.matches ? "auto" : "smooth" });
      } else {
        goTo(GX[i] + 40, i);
      }
    });
    const hit = (i) => {
      const el = gEls[i];
      if (!el) return;
      el.classList.remove("is-hit"); void el.getBoundingClientRect(); el.classList.add("is-hit");
    };
    const setActive = (i) => {
      if (i === active) return;
      if (i > active) hit(i);
      active = i;
      tabs.select(i, true);
    };
    const goTo = (x, i) => {
      cancelAnimationFrame(tween);
      const from = shownX, t0 = performance.now(), dur = reduceMQ.matches ? 1 : 900;
      const step = (now) => {
        const t = clamp((now - t0) / dur, 0, 1);
        place(lerp(from, x, easeIO(t)));
        if (t < 1) tween = requestAnimationFrame(step); else hit(i);
      };
      tween = requestAnimationFrame(step);
      active = i;
    };
    let gTop = 0, gTotal = 1;
    const gMeasure = () => { gTop = gates.getBoundingClientRect().top + scrollY; gTotal = Math.max(1, gates.offsetHeight - innerHeight); };
    addEventListener("resize", () => { gMeasure(); onScroll(); });
    addEventListener("load", () => { gMeasure(); onScroll(); });
    document.fonts?.ready.then(() => { gMeasure(); onScroll(); });
    gMeasure();
    const onScroll = () => {
      if (!pinned.matches) return;
      const q = clamp((scrollY - gTop) / gTotal, 0, 1);
      place(20 + q * 1160);
      let i = 0;
      Q.forEach((v, k) => { if (q >= v - 0.02) i = k; });
      setActive(i);
    };
    addEventListener("scroll", onScroll, { passive: true });
    pinned.addEventListener?.("change", () => { if (!pinned.matches) place(GX[Math.max(0, active)] + 40); onScroll(); });
    if (pinned.matches) onScroll(); else place(GX[0] + 40);
  }

  /* ------------------------------------------------------------------
     Gap checker
  ------------------------------------------------------------------ */
  const checker = $("[data-checker]");
  const gapList = $("[data-gaps]");
  const scoreEl = $("[data-score]");
  let gapState = null;
  if (checker && gapList && scoreEl) {
    const ITEMS = [
      { id: "reg", text: "FINTRAC registration", fix: "MSB registration" },
      { id: "address", text: "A Canadian business address", fix: "Canadian address" },
      { id: "officer", text: "A named compliance officer", fix: "Compliance programs" },
      { id: "policies", text: "Written policies and procedures", fix: "Compliance programs" },
      { id: "risk", text: "A documented risk assessment", fix: "Compliance programs" },
      { id: "training", text: "An ongoing training program", fix: "Training" },
      { id: "review", text: "An effectiveness review in the last two years", fix: "Effectiveness reviews" },
    ];
    const lis = {};
    ITEMS.forEach((it) => {
      const li = document.createElement("li");
      li.innerHTML = `<svg aria-hidden="true"><use href="#i-gap"/></svg><span></span><span class="fix"></span>`;
      gapList.appendChild(li);
      lis[it.id] = li;
    });

    // live score odometer: two columns, hidden leading zero
    scoreEl.textContent = "";
    const scols = [0, 1].map(() => {
      const col = document.createElement("span");
      col.className = "odo-col";
      const strip = document.createElement("span");
      for (let k = 0; k < 10; k++) { const d = document.createElement("span"); d.dataset.d = k; strip.appendChild(d); }
      col.appendChild(strip);
      scoreEl.appendChild(col);
      return { col, strip };
    });
    const setScore = (n) => {
      const tens = Math.floor(n / 10), ones = n % 10;
      scols[0].col.style.display = tens ? "" : "none";
      scols[0].strip.style.transform = `translateY(-${tens}em)`;
      scols[1].strip.style.transform = `translateY(-${ones}em)`;
    };
    const ofEl = $("[data-score-of]"), srEl = $("[data-score-sr]");
    const addrField = $("[data-address-field]");

    const run = () => {
      const fd = new FormData(checker);
      const base = fd.get("base"), reg = fd.get("reg"), addr = fd.get("address");
      const els = fd.getAll("el");
      addrField.hidden = base !== "out";
      const state = {
        reg: reg === "yes",
        address: base === "out" ? addr === "yes" : null,
        officer: els.includes("officer"), policies: els.includes("policies"), risk: els.includes("risk"),
        training: els.includes("training"), review: els.includes("review"),
      };
      let have = 0, total = 0;
      const gaps = [];
      ITEMS.forEach((it) => {
        const li = lis[it.id];
        const v = state[it.id];
        li.hidden = v === null;
        if (v === null) return;
        total++;
        if (v) have++; else gaps.push(it);
        const text = it.id === "reg" && reg === "progress" ? "FINTRAC registration, in progress" : it.text;
        li.className = v ? "is-done" : "is-gap";
        li.firstElementChild.firstElementChild.setAttribute("href", v ? "#i-check" : "#i-gap");
        li.children[1].textContent = text;
        li.children[2].textContent = v ? "In place" : it.fix;
      });
      setScore(have);
      ofEl.textContent = `of ${total}`;
      srEl.textContent = `${have} of ${total} in place.`;
      gapState = { activity: fd.get("activity"), base, reg, gaps, have, total };
    };
    checker.addEventListener("change", run);
    run();
  }

  /* ------------------------------------------------------------------
     Consultation form: picks, carry-over, submit
  ------------------------------------------------------------------ */
  const form = $("[data-consult]");
  const setNeed = (v) => { const r = form && $(`input[name="need"][value="${v}"]`, form); if (r) r.checked = true; };
  $$("[data-pick]").forEach((a) => a.addEventListener("click", () => setNeed(a.dataset.pick)));
  const needParam = new URLSearchParams(location.search).get("need");
  if (needParam) setNeed(needParam);

  const carry = $("[data-carry]");
  if (carry && form) carry.addEventListener("click", (e) => {
    if (!gapState) return;
    e.preventDefault();
    const g = gapState;
    const ids = g.gaps.map((x) => x.id);
    const need = ids.includes("reg") ? "register"
      : ids.includes("address") ? "address"
      : ids.some((x) => ["officer", "policies", "risk"].includes(x)) ? "programme"
      : ids.includes("review") ? "review"
      : ids.includes("training") ? "training" : "unsure";
    setNeed(need);
    const notes = $("[data-notes]");
    const lines = [
      `From the gap check: ${g.activity}, based ${g.base === "out" ? "outside" : "in"} Canada. ${g.have} of ${g.total} in place.`,
      g.gaps.length ? `Gaps: ${g.gaps.map((x) => (/^[A-Z]{2}/.test(x.text) ? x.text : x.text.charAt(0).toLowerCase() + x.text.slice(1))).join("; ")}.` : "No gaps flagged. We'd like a second opinion.",
    ];
    notes.value = lines.join("\n");
    $("#consult").scrollIntoView({ behavior: reduceMQ.matches ? "auto" : "smooth", block: "start" });
    setTimeout(() => $("#f-name").focus({ preventScroll: true }), reduceMQ.matches ? 0 : 700);
  });

  if (form) {
    const msg = $("[data-msg]", form);
    const btn = $('button[type="submit"]', form);
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      msg.className = "form-msg";
      msg.textContent = "";
      const req = $$("[required]", form);
      req.forEach((f) => f.setAttribute("aria-invalid", String(!f.checkValidity())));
      const bad = req.filter((f) => !f.checkValidity());
      if (bad.length) {
        const names = bad.map((f) => $(`label[for="${f.id}"]`, form).textContent.trim().toLowerCase());
        const list = names.length > 1 ? `${names.slice(0, -1).join(", ")} and ${names.at(-1)}` : names[0];
        const emailBad = bad.some((f) => f.type === "email" && f.value);
        msg.textContent = emailBad && bad.length === 1 ? "That email address doesn't look complete. Please check it." : `Please add your ${list}.`;
        msg.classList.add("err");
        bad[0].focus();
        return;
      }
      const label = btn.innerHTML;
      btn.disabled = true;
      btn.textContent = "Sending…";
      try {
        if (!CFG.web3formsKey) throw new Error("no-endpoint");
        const data = Object.fromEntries(new FormData(form));
        if (data.botcheck) throw new Error("http");
        const needLabel = $(`input[name="need"]:checked + span`, form)?.textContent || "";
        const payload = { ...data, access_key: CFG.web3formsKey, need: needLabel, subject: `${data.subject}: ${needLabel}`, replyto: data.email };
        const res = await fetch(FORM_ENDPOINT, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(payload) });
        const out = await res.json().catch(() => ({}));
        if (!res.ok || out.success === false) throw new Error("http");
        window.gtag?.("event", "generate_lead", { form: "consultation", need: data.need });
        msg.textContent = "Thank you. We'll be in touch to find a time.";
        msg.classList.add("ok");
        form.reset();
      } catch (err) {
        msg.textContent = err.message === "no-endpoint"
          ? "Online requests aren't switched on yet. Please email info@amlcanada.ca and we'll find a time."
          : "That didn't go through. Please check your connection and try again.";
        msg.classList.add("err");
      } finally {
        btn.disabled = false;
        btn.innerHTML = label;
      }
    });
    $$("input, textarea", form).forEach((f) => f.addEventListener("input", () => f.removeAttribute("aria-invalid")));
  }

  /* Analytics: Cloudflare Web Analytics is cookieless and loads directly.
     The Google tag loads only after the visitor accepts the cookie banner. */
  const addScript = (src, attrs = {}) => {
    const sc = document.createElement("script");
    sc.src = src; sc.async = true;
    Object.entries(attrs).forEach(([k, v]) => sc.setAttribute(k, v));
    document.head.appendChild(sc);
  };
  if (CFG.cfBeacon) addScript("https://static.cloudflareinsights.com/beacon.min.js", { defer: "", "data-cf-beacon": JSON.stringify({ token: CFG.cfBeacon }) });

  const CONSENT_KEY = "amlc-consent";
  const store = { get: () => { try { return localStorage.getItem(CONSENT_KEY); } catch { return null; } },
                  set: (v) => { try { localStorage.setItem(CONSENT_KEY, v); } catch { /* storage blocked */ } } };
  let gtagLoaded = false;
  const loadGoogle = () => {
    if (gtagLoaded || !CFG.gaId) return;
    gtagLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("consent", "default", { analytics_storage: "granted", ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied" });
    window.gtag("js", new Date());
    window.gtag("config", CFG.gaId, { anonymize_ip: true });
    addScript(`https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(CFG.gaId)}`);
  };
  const banner = $("[data-consent]");
  const reopen = $("[data-consent-open]");
  if (CFG.gaId && banner) {
    reopen && (reopen.hidden = false);
    const choice = store.get();
    if (choice === "yes") loadGoogle();
    else if (choice !== "no") banner.hidden = false;
    $("[data-consent-yes]", banner).addEventListener("click", () => { store.set("yes"); banner.hidden = true; loadGoogle(); });
    $("[data-consent-no]", banner).addEventListener("click", () => {
      store.set("no"); banner.hidden = true;
      if (gtagLoaded) { window.gtag("consent", "update", { analytics_storage: "denied" }); }
    });
    reopen?.addEventListener("click", () => { banner.hidden = false; $("[data-consent-yes]", banner).focus(); });
  }

  const yr = $("[data-year]");
  if (yr) yr.textContent = new Date().getFullYear();
})();
