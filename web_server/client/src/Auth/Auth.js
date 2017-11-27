class Auth {

  //Authenticate a user. Save a token string in localstorage.
  static authenticateUser(token, email) {
    localStorage.setItem('token', token);
    localStorage.setItem('email', email);
  }

  //Check if a user is authenticated.
  static isUserAuthenticated() {
    return localStorage.getItem('token') !== null
  }

  //De-authenticate a user
  static deauthenticate() {
    localStorage.removeItem('token');
    localStorage.removeItem('email');
  }

  //Get a token value
  static getToken() {
    return localStorage.getItem('token');
  }

  //Get email
  static getEmail() {
    return localStorage.getItem('email');
  }


}
export default Auth;
