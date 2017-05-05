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
      name: 'login',
      path: '/login',
      component: Vue.component('p-login'),
      beforeEnter: checkAuth
    },
    {
      name: 'home',
      path: '/home',
      component: Vue.component('p-home'),
      beforeEnter: checkAuth,
      children: [
        {
          name: 'code',
          path: '/code',
          component: Vue.component('p-code-form')
        },
        {
          name: 'file',
          path: '/file',
          component: Vue.component('p-file-form')
        },
        {
          name: 'grade',
          path: '/grade',
          component: Vue.component('p-grade'),
          props: true
        }
      ]
    },
  ]
});