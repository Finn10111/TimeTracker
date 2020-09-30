'use strict';

module.exports = function(environment) {
  let ENV = {
    modulePrefix: 'timetracker',
    environment,
    rootURL: '/',
    locationType: 'auto',
    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. EMBER_NATIVE_DECORATOR_SUPPORT: true
      },
      EXTEND_PROTOTYPES: {
        // Prevent Ember Data from overriding Date.parse.
        Date: false
      }
    },

    APP: {
      // Here you can pass flags/options to your application instance
      // when it is created
    }
  };

  if (environment === 'development') {
    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;
  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.locationType = 'none';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';
    ENV.APP.autoboot = false;
  }

  if (environment === 'production') {
    // here you can enable a production-specific feature
  }

  ENV['ember-simple-auth'] = {
    authorizer: 'authorizer:token'
  };
  ENV['ember-simple-auth-token'] = {
    serverTokenEndpoint: '/api/auth/login',
    refreshAccessTokens: true,
    serverTokenRefreshEndpoint: '/api/auth/refresh',
    refreshLeeway: 300, // Refresh the token 5 minutes (300s) before it expires.
    headers: {'Content-Type': 'application/json'},
    tokenPropertyName: 'access_token',
    refreshTokenPropertyName: 'refresh_token',
    authorizationHeaderName: 'Authorization', // Header name added to each API request
    authorizationPrefix: 'Bearer ', // Prefix added to each API request
  };

  return ENV;
};
