//import { createApp, ref } from 'vue'

console.log(Vue.version)

const app = Vue.createApp({
  data: () => ({
    count: Vue.ref(0),
    ver: Vue.version,
    countcolor: '<span style="color: RED">0</span>',
    message: 'Hello Vue!',
    user: {
      lastName: 'Bob',
      firstName: 'Smith',
      address: 'Tokyo',
    },
    colors: ['Red', 'Green', 'Blue']
  }),
//  data: function(){
//    let intCount = Vue.ref(0).value;
//    return{
//      count: Vue.ref(0),
//      ver: Vue.version,
//      countcolor: '<span style="color: RED">'+ intCount +'</span>'
//    }
//  },
})

app.mount('#app')