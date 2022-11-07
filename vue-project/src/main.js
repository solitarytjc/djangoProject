import { createApp } from 'vue'
import './mock/'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from './assets/axiosInstance'
import './assets/main.css'



const app = createApp(App)
app.use(ElementPlus)
app.mount('#app')
app.config.globalProperties.$axios=axios;



