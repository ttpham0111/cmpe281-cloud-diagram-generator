var AuthService = {
  user: null,

  login: function(username, password, success, error) {
    var self = this;
    return jQuery.ajax({
      type: 'POST',
      url: '/api/login',
      contentType: 'application/json; charset=utf-8',
      data: JSON.stringify({ username: username, password: password }),

      success: function(user) {
        self.user = user;
        self.user.authenticated = true;
        success();
      },

      error: function(data) {
        error(data);
      }
    });
  },

  logout: function() {
    var self = this;
    return jQuery.post('/api/logout', function() {
      self.user = null;
    });
  },

  check: function() {
    return this.user && this.user.authenticated;
  },

  getUser: function() {
    return this.user;
  }
};