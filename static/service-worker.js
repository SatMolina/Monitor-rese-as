// service-worker.js
const CACHE_NAME = 'my-cache-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/styles.css',
  '/app.js', // Si tienes un archivo JS, agrégalo aquí
  '/static/logo.png', // Otros archivos estáticos, como imágenes, puedes añadirlos aquí
];

// Durante la instalación, caché todos los archivos necesarios
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('Archivos en caché durante la instalación');
      return cache.addAll(urlsToCache);
    })
  );
});

// Durante la activación, borra versiones anteriores de la caché
self.addEventListener('activate', (event) => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (!cacheWhitelist.includes(cacheName)) {
            console.log(`Borrando caché antiguo: ${cacheName}`);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Durante la navegación, trata de servir desde la caché, si no está, haz una solicitud a la red
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return cachedResponse || fetch(event.request);
    })
  );
});
