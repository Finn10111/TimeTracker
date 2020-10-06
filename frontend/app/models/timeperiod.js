import Model, {attr, belongsTo} from '@ember-data/model';
import { tracked } from '@glimmer/tracking';

export default class TimeperiodModel extends Model {
  @belongsTo('task') task;
  @attr('date', {defaultValue() { return new Date()}}) start;
  @attr('date') end;

  @tracked miliSeconds;

  get seconds() {
    if (this.end) {
      this.miliSeconds = this.end - this.start;
    } else {
      this.miliSeconds = new Date() - this.start;
    }
    return Math.round(this.miliSeconds / 1000);
  }
}
