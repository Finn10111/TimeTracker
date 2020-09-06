import RESTSerializer from '@ember-data/serializer/rest';
import { EmbeddedRecordsMixin } from '@ember-data/serializer/rest';

export default class ApplicationSerializer extends RESTSerializer.extend(EmbeddedRecordsMixin) {
  attrs = {
    timeperiods: {
      //deserialize: 'records'
      deserialize: 'records'
    }
  }
}
