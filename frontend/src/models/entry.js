// Model of Entry that match with the API's Model

class entry {
  constructor(
    id,
    value = 'Sample value',
    date = 'Sample date'
  ) {
    this.id = id
    this.value = value
    this.date = date
  }
}

export default entry
