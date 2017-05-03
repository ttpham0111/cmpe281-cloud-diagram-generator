var AuthService = {
  user: {
    authenticated: false,
    id: ''
  },

  login: function(userId, password, success, error) {
    var user = this.user;

    return jQuery.ajax({
      type: 'POST',
      url: '/api/login',
      contentType: 'application/json; charset=utf-8',
      data: JSON.stringify({ user_id: userId, password: password }),

      success: function() {
        user.authenticated = true;
        user.id = userId;

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
      self.user = {
        authenticated: false
      };
    });
  },

  check: function() {
    return this.user.authenticated;
  },

  getUserId: function() {
    return this.user.id;
  }
};