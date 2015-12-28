var chai = require('chai');
var chaiAsPromised = require('chai-as-promised');
var wd = require('wd');

var should = chai.should();
chai.use(chaiAsPromised);
chaiAsPromised.transferPromiseness = wd.transferPromiseness;

var appium_port = 4723;
var app = wd.promiseChainRemote('localhost', appium_port);
var caps = {
  "appPackage" : "com.urucas.appiumtests",
  "appActivity" : "com.urucas.appiumtests.activities.MainActivity",
  "appWaitActivity" : "com.urucas.appiumtests.activities.MainActivity",
  "browserName" : "",
  "deviceName" : "Android",
  "platformName" : "Android",
  "platformVersion" : "5.0",
  "appPath": "./app-debug.apk"
}
 
var os = require('os');
var socket_port = 5000
var ifaces = os.networkInterfaces();
var en1 = ifaces["en1"]
var local_ip;
for(i in en1){
  var addr = en1[i]
  if(addr.family != "IPv4") continue
    local_ip = ["http", addr.address].join("://")
  break;
}
if(!local_ip) throw new Error("Error getting local ip")
  var namespace = [local_ip, socket_port].join(":")

console.log("socket working on: "+namespace)

var io = require('socket.io')(5000);
var sockets = [];
io.on("connection", function(socket){
  sockets.push(socket)
})

describe("Test socket.io events", function() {
  var browser;
  this.timeout(0)

  before(function() {
    browser = wd.promiseChainRemote("http://localhost:4723/wd/hub");
    return browser
      .init(caps);
  });

  after(function() {
    return browser
      .quit();
  });

  it("should open socket.io activity", function(done){
    browser
    .setImplicitWaitTimeout(500)
    .elementById("openSocketIOBtt")
    .isDisplayed()
    .then(function(isDisplayed){
      isDisplayed.should.equal(true)
    })
    .elementById("openSocketIOBtt")
    .click()
    .setImplicitWaitTimeout(500)
     .getCurrentActivity()
     .then(function(activity){
       activity.should.not.equal("com.urucas.appiumtests.activities.SocketIOActivity")
     })
     .nodeify(done)
  })

  it("should show state connected", function(done){
    browser
    .setImplicitWaitTimeout(1500)
    .then(function(t){})
    .elementById("socketState")
    .isDisplayed()
    .then(function(isDisplayed){
      isDisplayed.should.equal(true)
    })
    .elementById("socketState")
    .text()
    .then(function(val){
      val.should.equal("State; Connected")
    })
    .nodeify(done)
  })

  it("should change text on socket event", function(done) {
    var text = "This text should be on the UI"
    io.emit("change text", {text:text})
    browser
    .setImplicitWaitTimeout(1500)
    .then(function(){})
    .elementById("textView")
    .isDisplayed()
    .then(function(isDisplayed){
      isDisplayed.should.equal(true)
    })
    .source()
    .elementById("textView")
    .text()
    .then(function(val){
      val.should.equal(text)
    })
    .nodeify(done)
  })

  it("should disconnect the socket", function(done){
    for(i in sockets){
      var socket = sockets[i]
      socket.disconnect('unauthorized')
    }
    browser
    .setImplicitWaitTimeout(500)
    .then(function(){})
    .elementById("socketState")
    .isDisplayed()
    .then(function(isDisplayed){
      isDisplayed.should.equal(true)
    })
    .elementById("socketState")
    .text()
    .then(function(val){
      val.should.equal("State; Disconnected")
    })
    .nodeify(done)
  })
})
