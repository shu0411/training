console.log(Vue.version)

const app = Vue.createApp({
  data: () => ({
    count: Vue.ref(0),
    ver: Vue.version,
    message: 'Hello Vue!',
    message2: 'Hello Vue!',
    toggle: false,
    user: {
      LastName: 'Bob',
      FirstName: 'Smith',
      Address: 'Tokyo',
      Age: 23,
    },
    colors: ['Red', 'Green', 'Blue','test'],
    nowTime: "-",
  }),
  methods: {
    onClick: function(){
      console.log("Button is Clicked")
      this.nowTime = new Date().toLocaleString()
    }
  }
})

app.component('hello-component', {
    template: '<p>Hello!</p>'
})

app.mount('#app')