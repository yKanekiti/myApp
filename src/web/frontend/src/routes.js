import Vue from 'vue';
import Router from 'vue-router';
import Home from './components/pages/Home.vue';
import Sub from './components/pages/Sub.vue';

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/sub',
            name: 'sub',
            component: Sub
        }
    ]
})
