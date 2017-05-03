Vue.directive('highlight', {
  deep: true,
  
  bind: function (el, binding) {
    jQuery(el).find('code').each(function(i, $code) {
      $code.textContent = binding.value;
      hljs.highlightBlock($code);
    });
  },

  componentUpdated: function (el, binding) {
    jQuery(el).find('code').each(function(i, $code) {
      $code.textContent = binding.value;
      hljs.highlightBlock($code);
    });
  }
});