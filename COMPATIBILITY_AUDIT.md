# ViPlex Web Page Compatibility Audit

This build follows a conservative compatibility profile because NovaStar documents Web Page media and URL requirements, but does not publish a detailed browser-engine/API compatibility table.

Legend:
- YES = safe/required for this build
- CONDITIONAL = browser/player/firmware/network dependent
- NO = not available inside a browser webpage
- AVOID = deliberately not used in this build

1. HTML — YES. Used.
2. CSS — YES for basic styling. Used conservatively.
3. JavaScript — CONDITIONAL at engine level; basic ES5 only is used.
4. Images — YES in NovaStar media generally; this build does not require images.
5. CSS Animations — CONDITIONAL; AVOID in this build.
6. CSS Transitions — CONDITIONAL; AVOID in this build.
7. DOM Manipulation — CONDITIONAL but fundamental to dynamic browser pages; basic getElementById/text updates only.
8. JavaScript Timers — CONDITIONAL; setInterval/setTimeout used because they are basic legacy browser APIs.
9. Canvas — CONDITIONAL; AVOID.
10. SVG — CONDITIONAL; AVOID.
11. HTML5 — CONDITIONAL by feature; basic HTML only.
12. React/Vue/Angular — CONDITIONAL production output only; AVOID.
13. Vite/Webpack apps — CONDITIONAL after production build; AVOID runtime/tooling.
14. Local LAN webpage — YES when player can route to the host LAN URL.
15. Remote HTTP webpage — CONDITIONAL on network reachability.
16. HTTPS webpage — CONDITIONAL on TLS/certificate/browser support.
17. REST API / Fetch / XHR — CONDITIONAL. This build uses XMLHttpRequest, not fetch.
18. WebSocket — CONDITIONAL; AVOID.
19. External CDN libraries — CONDITIONAL on Internet/TLS; AVOID.
20. External fonts — CONDITIONAL; AVOID. Uses Arial/Helvetica system fallbacks.
21. Node.js runtime inside webpage — NO.
22. Python runtime inside webpage — NO.
23. npm packages running directly on player — NO.
24. Server-side JavaScript inside webpage — NO.
25. Server-side React inside webpage — NO.
26. Browser extensions — NO/should not be relied on.
27. Direct laptop filesystem access — NO/should not be relied on.
28. Laptop localhost from player — NO. localhost points to the player itself.
29. APIs bound only to laptop localhost — NO from player. Bind API/server to LAN interface and use PC LAN IP.
30. Heavy JavaScript — AVOID.
31. Complex animations — AVOID.
32. Heavy WebGL/3D — AVOID.
33. Large images/videos — AVOID/optimize.
34. Very modern browser APIs — AVOID unless verified on the exact player/firmware.

## Existing project audit

The original uploaded LED project used several higher-risk features for an unknown embedded browser, including CSS Grid, CSS custom properties, SVG, transitions/transforms, `fetch`/modern JavaScript patterns, and multiple external project files. Those features are valid in modern Chrome but are not explicitly guaranteed by NovaStar's ViPlex documentation.

The later `REIN_NovaStar_Safe` build removed most modern features and used XMLHttpRequest, but it still depended on separate CSS/JS resources. Because the user's one-file simple HTML is known to render successfully, this new build collapses the entire presentation into one `index.html`, leaving only `data.json` as an optional live-data source. Even if that request fails, fallback data stays visible.
