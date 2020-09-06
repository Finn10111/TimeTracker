import Component from '@glimmer/component';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';
import { tracked } from '@glimmer/tracking';

export default class TaskListComponent extends Component {
  @service store;
  @tracked activeTask = null;
  @tracked interval = null;
  @tracked totalSeconds = 0;

  constructor(owner, args) {
    super(owner, args);
    this.calculateToalSeconds();
    var self = this;
    self.interval = setInterval(function() {
      self.calculateToalSeconds();
    }, 1000);
  }

  @action
  addTask(data) {
    if (!data.name) {
      return;
    }
    var self = this;
    this.store.createRecord('task', {
      name: data.name,
    }).save().then(function(task) {
      self.activate(task);
      // TODO: reset input
    });
  }

  @action
  activate(task) {
    this.stopAll();
    let timeperiod = this.store.createRecord('timeperiod');
    timeperiod.set('task', task);
    timeperiod.set('start', new Date());
    timeperiod.save()
      .then(function(response) {

    });
    this.activeTask = task;
  }

  @action
  delete(task) {
    var self = this;
    if (task.isRunning) {
      this.activeTask = null;
    }
    task.destroyRecord().then(function() {
      self.calculateToalSeconds();
    });
  }

  @action
  stop(task) {
    this.activeTask = null;
    task.get('timeperiods').forEach(function(timeperiod) {
      if (!timeperiod.end) {
        timeperiod.set('end', new Date());
        timeperiod.save();
      }
    });
  }

  @action
  stopAll() {
    var self = this;
    let tasks = this.store.peekAll('task');
    tasks.forEach(function(task)  {
      self.stop(task);
    });
  }

  @action
  calculateToalSeconds() {
    var self = this;
    this.totalSeconds = 0;

    // iterate over all tasks and update total seconds
    let tasks = this.store.peekAll('task')
    tasks.forEach(function(task) {
      self.totalSeconds += task.seconds;
    })

    // update active task?
  }
}
