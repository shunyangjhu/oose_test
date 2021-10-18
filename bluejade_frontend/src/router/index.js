import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import CommodityListPage from "../components/commodity/CommodityListPage";

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'Default',
            redirect: '/home',
            component: Home
        },
        {
            path: '/home',
            name: 'Home',
            redirect: '/commodity_list',
            component: Home,
            children: [
                {
                    path: '/commodity_list',
                    name: CommodityListPage,
                    component: () => import('../components/commodity/CommodityListPage')
                }
            ]
        },
        {
            path: '/login',
            name: 'Login',
            component: () => import('../components/login/Login')
        },
        {
            path: '/register',
            name: 'Register',
            component: () => import('../components/login/Register')
        },

    ]
})
