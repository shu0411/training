import { createApp, ref } from 'vue'

const app = createApp({
  setup() {
    let intcount = ref(0).value;
    
    return {
      count: ref(0),
      countcolor: '<span style="color: RED">' + intcount + '</span>'
    }
  }
})

app.mount('#app')