package com.urucas.appiumtests.activities;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;

import com.urucas.appiumtests.R;

/**
 * Created by vrunoa on 3/6/16.
 */
public class FlagSecureActivity  extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_flagsecure);

        Button insecureBtt = (Button) findViewById(R.id.insecureBtt);
        insecureBtt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                insecure();
            }
        });

        Button secureBtt = (Button) findViewById(R.id.secureBtt);
        secureBtt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                secure();
            }
        });
    }

    private void secure() {
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE,
                WindowManager.LayoutParams.FLAG_SECURE);
    }

    private void insecure() {
        getWindow().clearFlags(WindowManager.LayoutParams.FLAG_SECURE);
    }
}
