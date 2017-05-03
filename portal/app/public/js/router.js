var checkAuth = function(to, from, next) {
  var isAuthenticated = AuthService.check();

  if (to.path === '/login') {
    redirect = isAuthenticated ? '/home' : undefined;
  } else {
    redirect = isAuthenticated ? undefined : '/login';
  }

  next(redirect);
};

router = new VueRouter({
  mode: 'history',
  
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/login',
      component: Vue.component('p-login'),
      beforeEnter: checkAuth
    },
    {
      path: '/home',
      component: Vue.component('p-home'),
      beforeEnter: checkAuth,
      children: [
        {
          path: '',
          component: Vue.component('p-code-form')
        },
        {
          path: '/grade',
          component: Vue.component('p-grade')
        }
      ]
    },
  ]
});