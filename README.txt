REIN - ViPlex Compatible LED Build
==================================

TARGET
- ViPlex Express Web Page media
- 1152 x 2048 portrait solution
- Weather -> Air Quality -> Noise -> repeat
- Light professional theme
- No npm / React / external libraries required

WHY THIS BUILD IS DIFFERENT
- The entire UI, CSS and JavaScript are inside ONE index.html.
- No external CSS/JS/font/CDN dependencies.
- No React, Vue, Angular, Vite runtime or Webpack runtime.
- No Canvas, SVG, WebGL, CSS animations or transitions.
- No fetch(), async/await, promises, arrow functions, let/const, NodeList.forEach, padStart.
- Uses basic ES5-style JavaScript and XMLHttpRequest only for optional live data.
- If live data fails, fallback values remain visible; the page should not become blank.

TEST IN THIS ORDER
1. Extract this folder.
2. Double-click start_server.bat OR run: python server.py
3. Run ipconfig and note the PC IPv4 address, e.g. 192.168.1.20
4. From another device on the SAME LAN, open:
      http://192.168.1.20:8000
5. In ViPlex Express create a Web Page media item using that LAN URL.
6. Set the solution/page region to 1152 x 2048 and fill the entire screen.
7. Publish to the NovaStar player.

DO NOT USE IN VIPLEX
- http://localhost:8000
- http://0.0.0.0:8000

LIVE DATA
Current test setting inside index.html:
    var API_URL = 'data.json';

The page requests this every 5 seconds.

Best production setup:
- Let your REIN backend serve index.html.
- Expose latest LED data at /api/led-data.
- Change inside index.html:
    var API_URL = '/api/led-data';

This is same-origin and avoids CORS problems.

If you instead use an absolute URL such as:
    http://192.168.1.20:5000/api/led-data
then the backend must allow CORS from the webpage origin.

SLIDE TIMING
Inside index.html search for:
    var SLIDE_TIME = 12000;
12000 = 12 seconds.

DATA REFRESH
Inside index.html search for:
    var DATA_REFRESH_TIME = 5000;
5000 = 5 seconds.
