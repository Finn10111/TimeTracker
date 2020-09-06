import Controller from '@ember/controller';
import { action } from '@ember/object';

export default class RegisterController extends Controller {
  @action
  register(data) {
    console.log(data.identification);
    console.log(data.password);
    console.log(data.password_again);
    if (data.password == data.password_again) {
      fetch('/api/auth/register', {
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
        method: 'post',
        body: JSON.stringify({'identification': data.identification, 'password': data.password})
      }).then(function(response) {
        return response.json();
      }).then(function(data) {
      });
    }
  }
}
