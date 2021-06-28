import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

/* bootstrap globl styles */
import "bootstrap/dist/css/bootstrap.min.css";
import 'bootstrap';

/* base theme */
import './theme/themes.scss';
import './theme/core.css';


createApp(App).use(router).mount('#app')
