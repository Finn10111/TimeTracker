import Model, {attr, hasMany} from '@ember-data/model';

export default class TaskModel extends Model {
  @attr('string') name;
  @hasMany('timeperiod', { cascadeDelete: true }) timeperiods;

  get isRunning() {
    let running = false;
    this.timeperiods.forEach(function(timeperiod) {
      if (!timeperiod.end) {
        running = true;
      }
    });
    return running;
  }

  get seconds() {
    let seconds = 0;
    this.timeperiods.forEach(function(timeperiod) {
      seconds += timeperiod.get('seconds');
    });
    return seconds;
    
  }
}
