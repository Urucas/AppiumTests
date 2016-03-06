package com.urucas.appiumtests.activities;


import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.urucas.appiumtests.R;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button openBrowserBtt = (Button) findViewById(R.id.openBrowserBtt);
        openBrowserBtt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, OpenBrowserActivity.class);
                startActivity(intent);
            }
        });

        Button openWebviewBtt = (Button) findViewById(R.id.openWebviewBtt);
        openWebviewBtt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, WebViewActivity.class);
                startActivity(intent);
            }
        });

        Button requestPermBtt = (Button) findViewById(R.id.openRequestBtt);
        requestPermBtt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, RequestPermissionsActivity.class);
                startActivity(intent);
            }
        });

        Button socketIOBtt = (Button) findViewById(R.id.openSocketIOBtt);
        socketIOBtt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, SocketIOActivity.class);
                startActivity(intent);
            }
        });

        Button flagBtt = (Button) findViewById(R.id.openFlagBtt);
        flagBtt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, FlagSecureActivity.class);
                startActivity(intent);
            }
        });
    }

}
