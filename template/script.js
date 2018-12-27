var vm = new Vue({
  el: '#app',
  data () {
    return {
      info: {
        'data': {
          'hum': 0,
          'temp': 0
        }
      }
    }
  },
  created () {
    let that = this
    setInterval(function () {
      axios
      .get('http://192.168.0.100:9000/instance.json')
      .then(response => (that.info = response))
    }, 10000)
  }
})