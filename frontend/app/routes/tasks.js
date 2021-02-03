import Route from '@ember/routing/route';
import AuthenticatedRouteMixin from 'ember-simple-auth/mixins/authenticated-route-mixin';
import { inject as service } from '@ember/service';

export default class TaskRoute extends Route.extend(AuthenticatedRouteMixin) {
  @service flashMessages;

  model() {
    return this.store.findAll('task');
  }
}
