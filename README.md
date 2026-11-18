# Yumm — Sistema Operativo Integral para Restaurantes

Plataforma SaaS moderna para la gestión inteligente de restaurantes: pedidos digitales con Menú QR, comandas en tiempo real con Cocina KDS, control de inventario con costeo automático, reservaciones web y analítica asistida por Inteligencia Artificial.

🚀 **Producción:** [https://yumm-app.vercel.app](https://yumm-app.vercel.app)

---

## 🍽️ Funcionalidades Principales

1. **Menú QR & Autopedidos:** Pedidos al instante desde el móvil del comensal sin descargar aplicaciones.
2. **División de Cuentas & Pagos:** Cierre rápido de mesa y división automatizada de cuentas.
3. **Cocina KDS Inteligente:** Organización de comandas por estaciones, control de tiempos de preparación y modo hora pico.
4. **Control de Inventario & Costos:** Descuento automático por receta, alertas de stock bajo y minimización de mermas.
5. **Inteligencia Artificial Gastronómica:** Predicción de demanda, platos más rentables y soporte automatizado 24/7.
6. **Reservaciones Web:** Gestión de turnos y anticipos para eliminar mesas vacías.
7. **Fidelización & Clientes VIP:** Programas de recompensas y cupones por niveles.
8. **Modo Offline & Multi-Sucursal:** Continuidad operativa total aún ante caídas del enlace de internet local.

---

## 📁 Arquitectura del Proyecto

```text
yumm-app/
├── index.html                  # Landing principal y Hero interactivo
├── ecosistema.html             # Módulos y suite de productos Yumm
├── cocina-kds.html             # Pantalla de cocina y gestión de comandas
├── ia.html                     # Módulo de Inteligencia Artificial predictiva
├── planes.html                 # Planes comerciales (Esencial, Pro, Enterprise)
├── contacto.html               # Solicitud de demo y formulario comercial
├── legal/
│   ├── privacy.html            # Política de Privacidad y Datos
│   ├── terms-of-booking.html   # Términos del Servicio y Contratación
│   ├── allergens.html          # Seguridad e Infraestructura
│   └── cookies.html            # Política de Cookies técnicas
├── 404.html                    # Página de error personalizada
├── sitemap.xml                 # Mapa del sitio estructurado para buscadores
├── robots.txt                  # Reglas de rastreo optimizadas
├── llms.txt                    # Documentación curada para agentes de IA (Lighthouse standard)
├── llms-full.txt               # Contenido extendido para modelos de lenguaje (GEO)
├── vercel.json                 # Configuración de cabeceras, rutas limpias y redirecciones
└── download_site.py            # Script automatizado de extracción y sanitización
```

---

## 🔍 SEO & Optimización para Motores de Inteligencia Artificial (GEO)

* **Marcado Estructurado Schema.org:**
  * `@type: Organization`: Identidad de marca, contacto y enlaces corporativos.
  * `@type: SoftwareApplication`: Metadatos de producto, categorías de negocio y tiers de precios (\$49, \$79, \$108 USD).
  * `@type: WebSite`: Enlaces canónicos y búsqueda del sitio.
* **GEO & Agentic Readiness:**
  * Archivos `llms.txt` y `llms-full.txt` accesibles para motores como Perplexity, Claude, ChatGPT y Gemini.
  * `robots.txt` configurado para dar acceso deliberado a agentes de IA.
  * Cumplimiento estricto de accesibilidad de contenido sin requerir ejecución de JavaScript en el rastreo inicial.

---

## 🛡️ Anti-Badge System

Implementación de triple capa para garantizar la eliminación completa del badge de marca de agua:
1. **Sanitización Build-time:** Eliminación de los nodos DOM `<div id="__framer-badge-container">`.
2. **Override CSS Global:** Bloqueo permanente de despliegue mediante reglas prioritarias `!important`.
3. **Runtime MutationObserver:** Monitoreo activo en el cliente para interceptar y remover cualquier inyección dinámica.

---

## ⚙️ Despliegue en Vercel

El proyecto está configurado para despliegue estático de alto rendimiento en el Edge de Vercel:

```bash
# Despliegue a producción
npx vercel deploy --prod
```
