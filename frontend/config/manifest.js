'use strict';

module.exports = function(/* environment, appConfig */) {
  // See https://zonkyio.github.io/ember-web-app for a list of
  // supported properties

  return {
    name: "TimeTracker",
    short_name: "TimeTracker",
    description: "app for tracking times",
    start_url: "/",
    display: "standalone",
    background_color: "#fff",
    theme_color: "#fff",
    icons: [
      {
        src: "/timetracker.png",
        sizes: "192x192",
        type: "image/png"
      }
    ],
    ms: {
      tileColor: '#fff'
    }
  };
}
