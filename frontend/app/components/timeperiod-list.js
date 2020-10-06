import Component from '@glimmer/component';
import { action } from '@ember/object';

export default class TimeperiodListComponent extends Component {
  @action
  delete(timeperiod) {
    timeperiod.destroyRecord().then(function() {
    });
  }
}
