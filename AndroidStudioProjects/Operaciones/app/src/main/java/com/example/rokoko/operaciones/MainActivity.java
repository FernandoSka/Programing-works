package com.example.rokoko.operaciones;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    EditText txt1,txt2;
    Button btns, btnr, btnm, btnd;
    TextView txtr;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
        txt1 = (EditText)findViewById(R.id.txt1);
        txt2 = (EditText)findViewById(R.id.txt2);
        btns = (Button)findViewById(R.id.btnsum);
        btnr = (Button)findViewById(R.id.btnres);
        btnm = (Button)findViewById(R.id.btnmul);
        btnd = (Button)findViewById(R.id.btndiv);
        txtr = (TextView)findViewById(R.id.txtr);
        btns.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int num1=Integer.parseInt(txt1.getText().toString());
                int num2=Integer.parseInt(txt2.getText().toString());
                int s = num1+num2;
                txtr.setText("Resultado: "+s);
            }
        });
        btnr.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int num1=Integer.parseInt(txt1.getText().toString());
                int num2=Integer.parseInt(txt2.getText().toString());
                int s = num1-num2;
                txtr.setText("Resultado: "+s);
            }
        });
        btnm.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int num1=Integer.parseInt(txt1.getText().toString());
                int num2=Integer.parseInt(txt2.getText().toString());
                int s = num1*num2;
                txtr.setText("Resultado: "+s);
            }
        });
        btnd.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int num1=Integer.parseInt(txt1.getText().toString());
                int num2=Integer.parseInt(txt2.getText().toString());
                float s = num1/num2;
                txtr.setText("Resultado: "+s);
            }
        });
    }
}
