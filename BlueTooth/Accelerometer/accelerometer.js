/* define Parameters **************************************************************/
const DEVICE_NAME_PREFIX = 'BBC micro:bit'
const     ACCELEROMETERSERVICE_SERVICE_UUID = 'e95d0753-251d-470a-a062-fa1922dfa9a8'
const ACCELEROMETERDATA_CHARACTERISTIC_UUID = 'e95dca4b-251d-470a-a062-fa1922dfa9a8'
// Messages
const MSG_CONNECTED = 'Connected'
const MSG_CONNECT_ERROR = 'Failed to Conect'
const MSG_DISCONNECTED = 'Disconnected'
/*********************************************************************************/
// for connection process
const SERVICE_UUID = ACCELEROMETERSERVICE_SERVICE_UUID
const CHARACTERISTIC_UUID = ACCELEROMETERDATA_CHARACTERISTIC_UUID
// connected device value
var connectDevice

// disconnect process
function disconnect () {
  if (!connectDevice || !connectDevice.gatt.connected) return
  connectDevice.gatt.disconnect()
  alert(MSG_DISCONNECTED)
  postDisconnect()
}

function postDisconnect () {
  document.js.x.value = ''
  document.js.y.value = ''
  document.js.z.value = ''
}

// connect process
function connect () {
  navigator.bluetooth.requestDevice({
    filters: [{
      namePrefix: DEVICE_NAME_PREFIX
    }],
    optionalServices: [SERVICE_UUID]
  })
    .then(device => {
      connectDevice = device
      console.log('device', device)
      return device.gatt.connect()
    })
    .then(server => {
      console.log('server', server)
      server.getPrimaryService(SERVICE_UUID)
        .then(service => {
          // start service is here
          startService(service, CHARACTERISTIC_UUID) // start service
        })
    })
    .catch(error => {
      console.log(error)
      alert(MSG_CONNECT_ERROR)
    })
}

// start service event
function startService (service, charUUID) {
  service.getCharacteristic(charUUID)
    .then(characteristic => {
      characteristic.startNotifications()
        .then(char => {
          alert(MSG_CONNECTED)
          characteristic.addEventListener('characteristicvaluechanged',
            // event is here
            onAccelerometerValueChanged)
          console.log('Accelerometer:', char)
        })
    })
    .catch(error => {
      console.log(error)
      alert(MSG_CONNECT_ERROR)
    })
}

// event handler
function onAccelerometerValueChanged (event) {
  var AcceleratorX = event.target.value.getUint16(0) / 1000.0
  console.log('x:' + AcceleratorX)
  document.js.x.value = AcceleratorX
  var AcceleratorY = event.target.value.getUint16(2) / 1000.0
  console.log('y:' + AcceleratorY)
  document.js.y.value = AcceleratorY
  var AcceleratorZ = event.target.value.getUint16(4) / 1000.0
  console.log('z:' + AcceleratorZ)
  document.js.z.value = AcceleratorZ
}
