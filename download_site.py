import urllib.request
import urllib.error
import re
import os

BASE_URL = "https://jazzed-times-273705.framer.app"
DEST_DIR = "/Users/bryan/Documents/ChatGPT/github/yumm-app"

ROUTES = [
    ("/", "index.html", None),
    ("/ecosistema", "ecosistema.html", "ecosistema/index.html"),
    ("/cocina-kds", "cocina-kds.html", "cocina-kds/index.html"),
    ("/ia", "ia.html", "ia/index.html"),
    ("/planes", "planes.html", "planes/index.html"),
    ("/contacto", "contacto.html", "contacto/index.html"),
    ("/legal/privacy", "legal/privacy.html", "legal/privacy/index.html"),
    ("/legal/terms-of-booking", "legal/terms-of-booking.html", "legal/terms-of-booking/index.html"),
    ("/legal/allergens", "legal/allergens.html", "legal/allergens/index.html"),
    ("/legal/cookies", "legal/cookies.html", "legal/cookies/index.html"),
    ("/404", "404.html", None),
]

ANTI_BADGE_HEAD = """
<!-- Yumm Engine / Anti-Badge & Brand Overrides -->
<style id="yumm-anti-framer-badge">
#__framer-badge-container,
.__framer-badge,
[data-framer-name="Badge"],
a[title*="Framer"],
a[href*="framer.com"] {
  display: none !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  width: 0 !important;
  height: 0 !important;
  position: absolute !important;
  top: -9999px !important;
  z-index: -100 !important;
}
</style>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://yumm-app.vercel.app/#organization",
      "name": "Yumm",
      "url": "https://yumm-app.vercel.app",
      "logo": "https://framerusercontent.com/images/1alrpgPyhYM4P7bY6IrePHRGvY.jpg",
      "description": "Sistema operativo integral para restaurantes: pedidos QR, comandas KDS, inventario inteligente y analítica con Inteligencia Artificial.",
      "contactPoint": {
        "@type": "ContactPoint",
        "contactType": "customer support",
        "url": "https://yumm-app.vercel.app/contacto",
        "availableLanguage": ["Spanish"]
      }
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://yumm-app.vercel.app/#software",
      "name": "Yumm Restaurantes",
      "applicationCategory": "BusinessApplication",
      "operatingSystem": "Web, Cloud, iOS, Android, POS",
      "offers": [
        {
          "@type": "Offer",
          "name": "Plan Esencial",
          "price": "49",
          "priceCurrency": "USD",
          "description": "Menú QR, pedidos digitales, cocina KDS básica"
        },
        {
          "@type": "Offer",
          "name": "Plan Pro",
          "price": "79",
          "priceCurrency": "USD",
          "description": "Cocina KDS avanzada, inventario con costeo automático y reservas web"
        },
        {
          "@type": "Offer",
          "name": "Plan Enterprise",
          "price": "108",
          "priceCurrency": "USD",
          "description": "IA predictiva, multi-sucursal, modo offline y soporte 24/7"
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://yumm-app.vercel.app/#website",
      "url": "https://yumm-app.vercel.app",
      "name": "Yumm - Software Integral para Restaurantes",
      "publisher": { "@id": "https://yumm-app.vercel.app/#organization" }
    }
  ]
}
</script>
"""

ANTI_BADGE_BODY = """
<script id="yumm-badge-remover">
(function() {
  function obliterateBadge() {
    var b = document.getElementById('__framer-badge-container');
    if (b) b.remove();
    var badges = document.querySelectorAll('.__framer-badge, [data-framer-name="Badge"], a[href*="framer.com"]');
    for (var i = 0; i < badges.length; i++) {
      badges[i].remove();
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', obliterateBadge);
  } else {
    obliterateBadge();
  }
  var observer = new MutationObserver(obliterateBadge);
  observer.observe(document.documentElement, { childList: true, subtree: true });
})();
</script>
"""

def sanitize_html(html: str) -> str:
    # 1. Strip framer badge container
    html = re.sub(r'<div id="__framer-badge-container".*?</div>', '', html, flags=re.DOTALL)
    
    # 2. Strip any standalone framer badge anchors
    html = re.sub(r'<a[^>]*class="[^"]*__framer-badge[^"]*"[^>]*>.*?</a>', '', html, flags=re.DOTALL)
    
    # 3. Replace generator meta tag
    html = re.sub(r'<meta name="generator" content="Framer[^"]*">', '<meta name="generator" content="Yumm SaaS Engine">', html)
    
    # 4. Canonical / Host replacement
    html = html.replace('https://jazzed-times-273705.framer.app', 'https://yumm-app.vercel.app')
    
    # 5. Inject CSS & Schema into <head>
    if '</head>' in html:
        html = html.replace('</head>', f'{ANTI_BADGE_HEAD}\n</head>', 1)
    
    # 6. Inject Remover script into </body>
    if '</body>' in html:
        html = html.replace('</body>', f'{ANTI_BADGE_BODY}\n</body>', 1)
        
    return html

def fetch_and_save():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    
    print("Beginning site download & optimization...")
    results = []
    
    for route, file1, file2 in ROUTES:
        url = f"{BASE_URL}{route}" if route != "/" else f"{BASE_URL}/"
        print(f"Fetching {url}...")
        
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                content = response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            content = e.read().decode('utf-8')
            
        initial_len = len(content)
        sanitized = sanitize_html(content)
        final_len = len(sanitized)
        
        # Save file1
        p1 = os.path.join(DEST_DIR, file1)
        os.makedirs(os.path.dirname(p1), exist_ok=True)
        with open(p1, 'w', encoding='utf-8') as f:
            f.write(sanitized)
            
        # Save file2 if exists
        if file2:
            p2 = os.path.join(DEST_DIR, file2)
            os.makedirs(os.path.dirname(p2), exist_ok=True)
            with open(p2, 'w', encoding='utf-8') as f:
                f.write(sanitized)
                
        results.append((route, file1, initial_len, final_len))
        print(f"✓ Saved {file1} (raw: {initial_len} bytes -> sanitized: {final_len} bytes)")
        
    print("\nDownload complete! Summary:")
    for r, f, init_l, fin_l in results:
        print(f" - {r:22} -> {f:25} ({fin_l} bytes)")

if __name__ == "__main__":
    fetch_and_save()
