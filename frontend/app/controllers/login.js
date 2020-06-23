import Controller from '@ember/controller';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';

export default class LoginController extends Controller {
  @service session;

  @action
  async authenticate() {
    console.log('auth');
    let { identification, password } = this;
    try {
      await this.session.authenticate('authenticator:token', identification, password);
    } catch(error) {
      this.errorMessage = error.error || error;
    }

    if (this.session.isAuthenticated) {
      // What to do with all this success?
    }
  }
}
