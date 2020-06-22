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
    this.stopAll();
    this.calculateToalSeconds();
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
    var self = this;
    self.activeTask = null;
    this.store.findAll('task')
      .then(function(tasks) {
        tasks.forEach(function(task)  {
          task.set('isRunning', false);
          task.save().then(function() {
            window.clearInterval(self.interval);
          });
        });
      task.set('isRunning', true);
      task.save().then(function() {
        self.activeTask = task;
        self.interval = setInterval(function() {
          task.incrementProperty('seconds');
          task.save().then(function() {
            self.calculateToalSeconds();
          });
        }, 1000);
      });
    });
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
  stopAll() {
    var self = this;
    this.store.findAll('task')
      .then(function(tasks) {
        tasks.forEach(function(task)  {
          task.set('isRunning', false);
          task.save().then(function() {
            window.clearInterval(self.interval);
          });
          self.activeTask = null;
        });
    });
  }

  @action
  calculateToalSeconds() {
    var self = this;
    this.totalSeconds = 0;
    this.store.findAll('task')
      .then(function(tasks) {
        tasks.forEach(function(task) {
          self.totalSeconds += task.seconds;
        })
    });
  }
}
