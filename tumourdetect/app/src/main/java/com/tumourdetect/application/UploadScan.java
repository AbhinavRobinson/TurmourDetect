package com.tumourdetect.application;

import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.tumourdetect.application.R;

public class UploadScan extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_upload_scan);

        Button uploadImage = (Button) findViewById(R.id.button);
        uploadImage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String web = "http://169.254.62.55:5000/index";
                Uri webaddress = Uri.parse(web);

                Intent gotoUploadImage = new Intent(Intent.ACTION_VIEW, webaddress);
                if(gotoUploadImage.resolveActivity(getPackageManager())!=null){
                    startActivity(gotoUploadImage);
                }
            }
        });
    }
}
