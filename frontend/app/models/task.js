import Model, {attr} from '@ember-data/model';

export default class TaskModel extends Model {
  @attr('string') name;
  @attr('number', {defaultValue: 0}) seconds;
  @attr('boolean', {defaultValue: false}) isRunning;

  get milliseconds() {
    return this.seconds * 1000;
  }
}
