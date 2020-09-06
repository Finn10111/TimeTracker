import RESTSerializer from '@ember-data/serializer/rest';
import { assign } from '@ember/polyfills';


export default class ApplicationSerializer extends RESTSerializer {
  serializeIntoHash(hash, type, record, options) {
    // remove payloadkey / root record
    assign(hash, this.serialize(record, options));
  }

}
