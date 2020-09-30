import RESTAdapter from '@ember-data/adapter/rest';
import { computed } from '@ember/object';
import { inject as service } from '@ember/service';
import CascadeDeleteMixin from 'ember-data-cascade-delete';
import TokenAdapterMixin from 'ember-simple-auth-token/mixins/token-adapter';

export default class ApplicationAdapter extends RESTAdapter.extend(TokenAdapterMixin, CascadeDeleteMixin) {
//export default s ApplicationAdapter extends RESTAdapter.extend(CascadeDeleteMixin) {
  namespace = '/api';
}
