importScripts('/static/js/workbox-sw.prod.v1.0.1.js');

/**
 * DO NOT EDIT THE FILE MANIFEST ENTRY
 *
 * The method precache() does the following:
 * 1. Cache URLs in the manifest to a local cache.
 * 2. When a network request is made for any of these URLs the response
 *    will ALWAYS comes from the cache, NEVER the network.
 * 3. When the service worker changes ONLY assets with a revision change are
 *    updated, old cache entries are left as is.
 *
 * By changing the file manifest manually, your users may end up not receiving
 * new versions of files because the revision hasn't changed.
 *
 * Please use workbox-build or some other tool / approach to generate the file
 * manifest which accounts for changes to local files and update the revision
 * accordingly.
 */
const fileManifest = [
  {
    "url": "/static/img/icon.png",
    "revision": "ea9ebde06add5414e75ebe00bc86c3fd"
  },
  {
    "url": "/static/img/og.png",
    "revision": "e41941a8176a210eae8fedcb728a4a54"
  },
  {
    "url": "/static/js/ga.js",
    "revision": "3fe57bda29ce82a4ba3f1f67c70383ec"
  },
  {
    "url": "/static/js/wavesurfer.min.js",
    "revision": "31f8e171313706667b3ef1b869012b51"
  },
  {
    "url": "/static/js/webfont.js",
    "revision": "7c96a5f11d9741541d5e3c42ff6380d7"
  },
  {
    "url": "/static/manifest.json",
    "revision": "05fa8390daacb9fcab1a17bd66976ab5"
  }
];

const workboxSW = new self.WorkboxSW();
workboxSW.precache(fileManifest);


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
  'https://api.soundcloud.com/tracks/(.*)',
  workboxSW.strategies.cacheFirst({
    cacheName: 'tracks',
    cacheExpiration: {
      maxEntries: 100,
      maxAgeSeconds: 7 * 24 * 60 * 60,
    },
    cacheableResponse: {statuses: [0, 200]},
  })
);




