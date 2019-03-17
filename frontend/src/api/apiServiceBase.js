import axios from 'axios'

import Queue from '../toolbox/queue.js'

class ApiServiceBase {
  constructor() {
    this.queue = new Queue()
  }

  __catchErrorMessage(error) {
    if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      console.log(error.response.status)
      let responseMessage = JSON.parse(error.response.request.response)
      console.log(responseMessage.error.code + ' - ' + responseMessage.error.message)
      return {
        message: {
          message: responseMessage.error.message,
          code: responseMessage.error.code
        },
        status: error.response.status
      }
    } else if (error.request) {
      // The request was made but no response was received
      // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
      // http.ClientRequest in node.js
      console.log(error.request)
    } else {
      // Something happened in setting up the request that triggered an Error
      console.log('Error', error.message)
    }
  }

  getFromUrl(url, callback, errorCallback, priority) {
    console.log(url + ' - GET')
    this.queue[priority ? 'unshift' : 'add'](() => {
      const self = this
      axios
        .get(url)
        .then(response => {
          console.log(url + ' - Response - ' + response.status)
          self.queue.next()
          return {
            message: response.data.data,
            status: response.status
          }
        })
        .then(callback)
        .catch(error => {
          self.queue.next()

          return this.__catchErrorMessage(error)
        })
        .then(errorCallback)
    })
  }

  postToUrl(url, body, callback, errorCallback, priority) {
    console.log(url + ' - POST')
    console.log(body)
    this.queue[priority ? 'unshift' : 'add'](() => {
      const self = this
      axios
        .post(url, body)
        .then(response => {
          console.log(url + ' - Response - ' + response.status)
          self.queue.next()
          return {
            message: response.data.data,
            status: response.status
          }
        })
        .then(callback)
        .catch(error => {
          self.queue.next()

          return this.__catchErrorMessage(error)
        })
        .then(errorCallback)
    })
  }

  putToUrl(url, body, callback, errorCallback, priority) {
    console.log(url + ' - PUT')
    console.log(body)
    this.queue[priority ? 'unshift' : 'add'](() => {
      const self = this
      axios
        .put(url, body)
        .then(response => {
          console.log(url + ' - Response - ' + response.status)
          self.queue.next()
          return {
            message: response.data.data,
            status: response.status
          }
        })
        .then(callback)
        .catch(error => {
          self.queue.next()

          return this.__catchErrorMessage(error)
        })
        .then(errorCallback)
    })
  }

  deleteToUrl(url, callback, errorCallback, priority) {
    console.log(url + ' - DELETE')
    this.queue[priority ? 'unshift' : 'add'](() => {
      const self = this
      axios
        .delete(url)
        .then(response => {
          console.log(url + ' - Response - ' + response.status)
          self.queue.next()
          return {
            message: response.data.data,
            status: response.status
          }
        })
        .then(callback)
        .catch(error => {
          self.queue.next()

          return this.__catchErrorMessage(error)
        })
        .then(errorCallback)
    })
  }
}

export default ApiServiceBase
