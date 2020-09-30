import { merge } from '@ember/polyfills';
import JWT from 'ember-simple-auth-token/authenticators/jwt';

export default JWT.extend({
  refreshAccessToken(token) {
    return new Promise((resolve, reject) => {
      const headers = merge(this.headers, {
        'Authorization': `Bearer ${token}`
      });
      this.makeRequest(this.serverTokenRefreshEndpoint, {}, headers).then(response => {
        try {
          const sessionData = this.handleAuthResponse(response.json);
          this.trigger('sessionDataUpdated', sessionData);
          return resolve(sessionData);
        } catch (error) {
          return reject(error);
        }
      }).catch(error => {
        this.handleTokenRefreshFail(error.status);
        return reject(error);
      });
    });
  }
});
