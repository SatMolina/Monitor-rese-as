const CACHE_NAME = "molina-cache-v1";
const urlsToCache = [
  "/",
  "/static/styles.css",
  "/static/logo.png",
  "/static/icons/icon-192x192.png",
  "/static/icons/icon-512x512.png",
  "/manifest.json"
];

self.addEventListener("install", function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(urlsToCache);
    })
  );
});

self.addEventListener("fetch", function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});
