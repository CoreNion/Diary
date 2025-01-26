self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open('diary-cache-v1').then(function(cache) {
      return cache.addAll([
        '/',
        '/static/css/base.css',
        '/static/css/home.css',
        '/static/css/create.css',
        '/static/manifest.json',
        '/static/js/editor.js',
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});
