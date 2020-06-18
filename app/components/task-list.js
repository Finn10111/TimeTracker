import Component from '@glimmer/component';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';
import { tracked } from '@glimmer/tracking';

export default class TaskListComponent extends Component {
    @service store;
    @tracked activeTask = null;
    @tracked interval = null;
    @tracked totalMilliseconds = 0;

    constructor(owner, args) {
        super(owner, args);
        this.stopAll();
    }

    @action
    addTask(data) {
        var self = this;
        this.store.createRecord('task', {
            name: data.name,
        }).save().then(function(task) {
            self.activate(task);
            data = null;
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
                        self.calculateToalMilliseconds();
                    });
                }, 1000);
            });
        });

    }

    @action
    delete(task) {
        if (task.isRunning) {
            this.activeTask = null;
        }
        task.destroyRecord();
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
    calculateToalMilliseconds() {
        var self = this;
        this.totalMilliseconds = 0;
        this.store.findAll('task')
            .then(function(tasks) {
                tasks.forEach(function(task) {
                    self.totalMilliseconds += task.milliseconds;
                })
        });
    }
}
