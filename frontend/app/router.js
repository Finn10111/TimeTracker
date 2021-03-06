import EmberRouter from '@ember/routing/router';
import config from './config/environment';

export default class Router extends EmberRouter {
  location = config.locationType;
  rootURL = config.rootURL;
}

Router.map(function() {
  this.route('login');
  this.route('register');
  this.route('logout');
  this.route('profile');
  this.route('page-not-found', { path: '/*wildcard' });
  this.route('tasks');
});
