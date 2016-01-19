On this example we create a simple test for websockets using [socket.io](http://socket.io/) both in the server and client. This example is created in nodejs and mocha. Checkout the test dependencies over the [package.json](https://github.com/Urucas/AppiumTests/blob/master/socketio/package.json) and java for Android for the [cient app](https://github.com/Urucas/AppiumTests/tree/master/android-app/AppiumTests)

#Why?
Websockets are a useful techonology and to ensure their correct implementation we should create tests, in this case our web sockets events will change our UI, so we use [appium](appium.io) for functional testing. 

#How?
We create a websocket server before running any test, in this case we use nodejs and socket.io. Thanks to socket.io creating a websocket server it's just one line: 
```nodejs
var io = require('socket.io')(5000);
```

In our android app we have to create a connection to this server, for this we'll use socket.io java client adding the library to our .gradle file;

```gradle
dependencies {
    compile 'io.socket:socket.io-client:0.6.2'
}
```

Now, let's create a connection and the events we are going to use in our app;
```java
  String namespace = "http://10.0.0.47:5000";
  try {
    socket = IO.socket(namespace);
    socket.on(Socket.EVENT_CONNECT, new OnSocketConnected());
    socket.on(Socket.EVENT_DISCONNECT, new OnSocketDisconnected());
    socket.on(Socket.EVENT_ERROR, new OnSocketError());
    socket.on("change text", new OnChangeTextEvent());
    socket.connect();

  }catch(Exception e){
    e.printStackTrace();
  }
  
  private class OnSocketError implements Emitter.Listener{
        @Override
        public void call(Object... args) {
            Log.i("err", String.valueOf(args[0]));
        }
    }

    private class OnSocketConnected implements Emitter.Listener{
        private void update(){
            // do something
        }
        @Override
        public void call(Object... args) {
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    update();
                }
            });
        }
    }

    private class OnSocketDisconnected implements Emitter.Listener{
        private void update(){
            // do something
        }
        @Override
        public void call(Object... args) {
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    update();
                }
            });
        }
    }

    private class OnChangeTextEvent implements Emitter.Listener{
        private void update(JSONObject obj) {
            // do something in our UI
            try {
                String t = obj.getString("text");
                textView.setText(t);
            }catch(Exception e){}
        }
        @Override
        public void call(Object... args) {
            final JSONObject obj = (JSONObject) args[0];
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    update(obj);
                }
            });
        }
    }
```
... full code [here](https://github.com/Urucas/AppiumTests/blob/master/android-app/AppiumTests/app/src/main/java/com/urucas/appiumtests/activities/SocketIOActivity.java)

In this case, an event emitted by the websocket will change a TextView on the UI, so we should test that if the event is fired and catched on the client app the UI is changed;

```javascript
it("should change text on socket event", function(done) {
    var text = "This text should be on the UI"
    
    // emit the socket event 
    io.emit("change text", {text:text})
    
    browser
    .setImplicitWaitTimeout(1500)
    .then(function(){})
    .elementById("textView")
    .isDisplayed()
    .then(function(isDisplayed){
      isDisplayed.should.equal(true)
    })
    .elementById("textView")
    .text()
    .then(function(val){
      val.should.equal(text)
    })
    .nodeify(done)
  })
  ```
... complete test is [here](https://github.com/Urucas/AppiumTests/blob/master/socketio/tests/test.js)

Once we have wrapped everyting, we run our test ```npm test``` and wait for the results. 
