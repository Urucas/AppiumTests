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
    }

}
