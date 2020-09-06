import Controller from '@ember/controller';
import { inject as service } from '@ember/service';

export default class LogoutController extends Controller {
  @service session;
}
