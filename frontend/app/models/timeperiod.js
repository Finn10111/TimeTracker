import Model, {attr, belongsTo} from '@ember-data/model';

export default class TimeperiodModel extends Model {
  @belongsTo('task') task;
  @attr('date', {defaultValue() { return new Date()}}) start;
  @attr('date') end;

  get miliSeconds() {
    let miliSeconds = 0;
    if (this.end) {
      miliSeconds = this.end - this.start;
    } else {
      miliSeconds = new Date() - this.start;
    }
    return miliSeconds;
  }

  get seconds() {
    return Math.round(this.miliSeconds / 1000);
  }
}
