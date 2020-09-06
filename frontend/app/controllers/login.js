import Controller from '@ember/controller';
import { action } from '@ember/object';
import { inject as service } from '@ember/service';
import { tracked } from "@glimmer/tracking";

export default class LoginController extends Controller {
  @tracked errorMessage;
  @service session;

  @action
  async authenticate() {
    let { identification, password } = this;
    try {
      await this.session.authenticate('authenticator:token', {identification, password});
    } catch(error) {
      this.errorMessage = error.error || error;
    }

    if (this.session.isAuthenticated) {
      // What to do with all this success?
    }
  }
}
