function Queue(asStack) {
  Object.defineProperties(this, {
    add: {
      enumerable: true,
      writable: false,
      value: addToQueue
    },
    unshift: {
      enumerable: true,
      writable: false,
      value: unshiftToQueue
    },
    next: {
      enumerable: true,
      writable: false,
      value: run
    },
    clear: {
      enumerable: true,
      writable: false,
      value: clearQueue
    },
    contents: {
      enumerable: false,
      get: getQueue,
      set: setQueue
    },
    autoRun: {
      enumerable: true,
      writable: true,
      value: true
    },
    stop: {
      enumerable: true,
      writable: true,
      value: false
    }
  })

  var queue = []
  var running = false

  function clearQueue() {
    queue = []
    return queue
  }

  function getQueue() {
    return queue
  }

  function setQueue(val) {
    queue = val
    return queue
  }

  function addToQueue() {
    for (var i in arguments) {
      if (arguments.hasOwnProperty(i)) {
        queue.push(arguments[i])
      }
    }
    if (!running && !this.stop && this.autoRun) {
      this.next()
    }
  }

  function unshiftToQueue() {
    for (var i in arguments) {
      if (arguments.hasOwnProperty(i)) {
        queue.unshift(arguments[i])
      }
    }
    if (!running && !this.stop && this.autoRun) {
      this.next()
    }
  }

  function run() {
    running = true
    if (queue.length < 1 || this.stop) {
      running = false
      return
    }

    queue.shift().bind(this)()
  }
}

module.exports = Queue
