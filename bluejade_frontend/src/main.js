import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui';
import "element-ui/lib/theme-chalk/index.css"

var axios = require('axios')
axios.defaults.baseUrl = 'http://localhost:8888/api'

Vue.prototype.$axios = axios
Vue.config.productionTip = false

Vue.use(ElementUI);

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
