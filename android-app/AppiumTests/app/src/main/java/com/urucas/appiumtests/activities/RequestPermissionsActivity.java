package com.urucas.appiumtests.activities;

import android.Manifest;
import android.content.pm.PackageManager;
import android.content.res.Resources;
import android.os.Bundle;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.ActionBarActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.urucas.appiumtests.R;

/**
 * Created by vruno on 12/9/15.
 */
public class RequestPermissionsActivity extends ActionBarActivity {

    private static final int REQ_CAMERA_PERMISSION = 1;
    private TextView stateTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_requestpermission);

        Button requestBtt = (Button) findViewById(R.id.requestBtt);
        requestBtt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                requestCameraPermission();
            }
        });

        stateTextView = (TextView) findViewById(R.id.stateTextView);
        stateTextView.setVisibility(View.INVISIBLE);
    }

    private void requestCameraPermission() {
        ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.CAMERA}, REQ_CAMERA_PERMISSION);
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        Resources r = getResources();
        stateTextView.setVisibility(View.VISIBLE);
        String state = r.getString(R.string.denied);
        if (PackageManager.PERMISSION_GRANTED == ContextCompat.checkSelfPermission(
                this, Manifest.permission.CAMERA)){
            state = r.getString(R.string.granted);
        }
        stateTextView.setText(String.format(
            r.getString(R.string.permission_state), state
        ));
    }
}
