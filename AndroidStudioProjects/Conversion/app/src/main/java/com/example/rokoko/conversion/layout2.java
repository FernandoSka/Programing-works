package com.example.rokoko.conversion;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

/**
 * Created by RoKoKo on 22/02/2016.
 */
public class layout2 extends AppCompatActivity {
    TextView res;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.layout2);

        res = (TextView)findViewById(R.id.txtot);
        String arry2[] = new String[1];//creamos un array en donde se almacenaran los datos de nuestro array anterior
        Bundle recupera= getIntent().getExtras();//recuperamos los "extras" de nuestro intent
        if (recupera != null){
            arry2= recupera.getStringArray("datos");//almacenamos los datos del array anterior en nuestro nuevo array
        }
        res.setText(arry2[0]);//seteamos nuestro primer valor del array en el texto
}
    }