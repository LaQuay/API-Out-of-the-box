import ApiServiceBase from './apiServiceBase.js'
import Config from '../config.js'

class EntryAPI extends ApiServiceBase {
  constructor() {
    super()
    this.baseUrl = Config.services.api_out_of_the_box.url
  }

  getAllEntries(priority, callback) {
    this.getFromUrl(
      this.baseUrl + `/entries/`,
      responseJson => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      priority
    )
  }

  getEntry(id, priority, callback, errorCallback) {
    this.getFromUrl(
      this.baseUrl + `/entries/${id}`,
      responseJson => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      errorJson => {
        const error = errorJson
        if (error) {
          console.log(error)
          errorCallback(error)
        }
      },
      priority
    )
  }

  addEntry(entry, priority, callback, errorCallback) {
    this.postToUrl(
      this.baseUrl + `/entries/`,
      entry,
      responseJson => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      errorJson => {
        const error = errorJson
        if (error) {
          console.log(error)
          errorCallback(error)
        }
      },
      priority
    )
  }

  updateEntry(entry, priority, callback, errorCallback) {
    this.putToUrl(
      this.baseUrl + `/entries/${entry.id}`,
      entry,
      responseJson => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      errorJson => {
        const error = errorJson
        if (error) {
          console.log(error)
          errorCallback(error)
        }
      },
      priority
    )
  }

  deleteEntry(entry, priority, callback, errorCallback) {
    this.deleteToUrl(
      this.baseUrl + `/entries/${entry}`,
      responseJson => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      errorJson => {
        const error = errorJson
        if (error) {
          console.log(error)
          errorCallback(error)
        }
      },
      priority
    )
  }
}

export default new EntryAPI()
