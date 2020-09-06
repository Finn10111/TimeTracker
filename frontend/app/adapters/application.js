import RESTAdapter from '@ember-data/adapter/rest';
import { computed } from '@ember/object';
import { inject as service } from '@ember/service';
import CascadeDeleteMixin from 'ember-data-cascade-delete';
import TokenAdapterMixin from 'ember-simple-auth-token/mixins/token-adapter';

export default class ApplicationAdapter extends RESTAdapter.extend(TokenAdapterMixin, CascadeDeleteMixin) {
//export default class ApplicationAdapter extends RESTAdapter.extend(CascadeDeleteMixin) {
  @service session;

  namespace = '/api';

  @computed('session.data.authenticated.access_token')
  get headers() {
    let headers = {};
    if (this.session.isAuthenticated) {
      // OAuth 2
      headers['Authorization'] = `Bearer ${this.session.data.authenticated.access_token}`;
      headers['Content-Type'] = 'application/json';
      headers['Accept'] = 'application/json';
    }

    return headers;
  }
}
