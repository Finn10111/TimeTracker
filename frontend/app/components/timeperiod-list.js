import Component from '@glimmer/component';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';

export default class TimeperiodListComponent extends Component {
  @service flashMessages;

  @action
  delete(timeperiod) {
    var self = this;
    timeperiod.destroyRecord().then(function() {
    })
    .catch(function(){
      self.flashMessages.danger('Something went wrong!');
    });
  }
}
