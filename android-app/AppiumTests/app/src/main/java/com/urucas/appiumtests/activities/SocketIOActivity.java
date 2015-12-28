package com.urucas.appiumtests.activities;

import android.content.res.Resources;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.TextView;

import com.urucas.appiumtests.R;

import org.json.JSONObject;

import java.net.InetAddress;
import java.net.NetworkInterface;
import java.util.Collections;
import java.util.List;

import io.socket.client.IO;
import io.socket.client.Socket;
import io.socket.emitter.Emitter;

/**
 * Created by vruno on 12/28/15.
 */
public class SocketIOActivity extends AppCompatActivity {

    private Socket socket;
    private TextView socketState;
    private TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_socketio);

        String namespace = "http://10.0.0.47:5000";

        socketState = (TextView) findViewById(R.id.socketState);
        textView = (TextView) findViewById(R.id.textView);

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
    }

    private class OnSocketError implements Emitter.Listener{

        @Override
        public void call(Object... args) {
            Log.i("err", String.valueOf(args[0]));
        }
    }

    private class OnSocketConnected implements Emitter.Listener{

        private void update(){
            Resources r = getResources();
            String c = r.getString(R.string.connected);
            socketState.setText(String.format(
                    r.getString(R.string.socket_status),
                    c
            ));
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
            Resources r = getResources();
            String c = r.getString(R.string.disconnected);
            socketState.setText(String.format(
                    r.getString(R.string.socket_status),
                    c
            ));
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

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if(socket != null){
            socket.disconnect();
        }
    }
}
