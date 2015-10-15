package com.urucas.appiumtests.activities;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.urucas.appiumtests.R;

/**
 * Created by vruno on 10/14/15.
 */
public class OpenBrowserActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_open_browser);

        Button openBrowserBtt = (Button) findViewById(R.id.openBrowserBtt);
        openBrowserBtt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse("http://www.google.com")));
            }
        });
    }
}
