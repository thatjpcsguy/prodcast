importScripts('/static/js/workbox-sw.prod.v1.0.1.js');

const workboxSW = new self.WorkboxSW();

workboxSW.router.registerRoute(
  '/',
  workboxSW.strategies.cacheFirst({
    cacheName: 'pages',
    cacheExpiration: {
      maxEntries: 100,
      maxAgeSeconds: 24 * 60 * 60,
    },
    cacheableResponse: {statuses: [200]},
  })
);

workboxSW.router.registerRoute(
  '/episodes',
  workboxSW.strategies.cacheFirst({
    cacheName: 'pages',
    cacheExpiration: {
      maxEntries: 100,
      maxAgeSeconds: 24 * 60 * 60,
    },
    cacheableResponse: {statuses: [200]},
  })
);

workboxSW.router.registerRoute(
  '/episodes/(.*)',
  workboxSW.strategies.cacheFirst({
    cacheName: 'pages',
    cacheExpiration: {
      maxEntries: 100,
      maxAgeSeconds: 24 * 60 * 60,
    },
    cacheableResponse: {statuses: [200]},
  })
);

workboxSW.router.registerRoute(
  '/static/(.*)',
  workboxSW.strategies.cacheFirst({
    cacheName: 'static',
    cacheExpiration: {
      maxEntries: 100,
      maxAgeSeconds: 7 * 24 * 60 * 60,
    },
    cacheableResponse: {statuses: [0, 200]},
  })
);





