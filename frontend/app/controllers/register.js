import Controller from '@ember/controller';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';

export default class RegisterController extends Controller {
  @tracked errorMessage = '';

  @action
  register(data) {
    let self = this;
    if (data.password == data.password_again) {
      fetch('/api/auth/register', {
      headers: {
        'Content-Type': 'application/json'
      },
        method: 'post',
        body: JSON.stringify({
          'identification': data.identification, 
          'password': data.password
        })
      }).then(function(response) {
        return response.json();
      }).then(function(data) {
        if (data.success) {
          self.transitionToRoute('index');
        } else {
          self.errorMessage = data.message;
        }
      });
    } else {
      this.errorMessage = 'The passwords do not match :-(';
    }
  }
}
