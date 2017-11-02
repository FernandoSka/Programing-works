package com.example.rokoko.conversion;

import android.content.Intent;
import android.database.Cursor;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioGroup;
import android.widget.SimpleCursorAdapter;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    EditText txt1;
    Button btnc;
    TextView txtr;/*
    version sin sqlite3
    RadioGroup rg1,rg2;
    protected ArrayAdapter<CharSequence> adapter;
    protected ArrayAdapter<CharSequence> adapter2;
    */
    private Tasa  dataSource;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
//Obtener instancia del Spinner
        dataSource = new Tasa(this);//instanciamos la clase Tasa


        final Spinner spinner = (Spinner) findViewById(R.id.cur1);//creamos el spinner
        SimpleCursorAdapter Spinnerr = new SimpleCursorAdapter(this,//creamos el adaptador
                android.R.layout.simple_spinner_item,
                dataSource.getAll(),
                new String[]{Tasa.Columnas.pais},
                new int[]{android.R.id.text1},
                SimpleCursorAdapter.FLAG_REGISTER_CONTENT_OBSERVER);
        spinner.setAdapter(Spinnerr);//asignamos el adaptador  a spinner
        final Spinner spinner2 = (Spinner) findViewById(R.id.cur2);
        spinner2.setAdapter(Spinnerr);//asignamos el mismo a daptador a spinner2

//Asignas el origen de datos desde los recursos
/*

       version sin sqlite3, no tomar en cuenta
       adapter = ArrayAdapter.createFromResource(this, R.array.currency,
                android.R.layout.simple_spinner_item);
//Asignas el layout a inflar para cada elemento
//al momento de desplegar la lista


       adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

//Seteas el adaptador
        spinner.setAdapter(adapter);
//Obtener instancia del GameSpinner
        final Spinner spinner2 = (Spinner) findViewById(R.id.cur2);
//Asignas el origen de datos desde los recursos
        adapter2 = ArrayAdapter.createFromResource(this, R.array.currency,
                android.R.layout.simple_spinner_item);
//Asignas el layout a inflar para cada elemento
//al momento de desplegar la lista
        adapter2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

//Seteas el adaptador
        spinner2.setAdapter(adapter2);
*/



/*
        rg1 = (RadioGroup)findViewById(R.id.radg1);
        rg2 = (RadioGroup)findViewById(R.id.radg2);*/


        txt1 = (EditText)findViewById(R.id.conv);
        btnc = (Button)findViewById(R.id.btnconv);
        txtr = (TextView)findViewById(R.id.txtres);
        btnc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {



                Cursor c2 = (Cursor) spinner.getSelectedItem();//obtenemos el cursor de nuestro spinner
                String Text = c2.getString(
                        c2.getColumnIndex(Tasa.Columnas.pais));//convertimos nuestro cursor en string
                Cursor c1 = (Cursor) spinner2.getSelectedItem();
                String Text2 = c1.getString(
                        c1.getColumnIndex(Tasa.Columnas.pais));

                try {
                double num1 = Double.parseDouble(txt1.getText().toString());

                    Cursor multiplicador1c = dataSource.getmulti(Text);
                    multiplicador1c.moveToFirst();//movemos el cursor al primer valor, si no lo tomara como -1
                    String multiplicador1s =  multiplicador1c.getString(
                            multiplicador1c.getColumnIndex(Tasa.Columnas.multi));
                    int multiplicador1 = Integer.parseInt(multiplicador1s);



                    Cursor multiplicador2c = (Cursor)dataSource.getmulti(Text2);
                    multiplicador2c.moveToFirst();
                    String multiplicador2s = multiplicador2c.getString(
                            multiplicador2c.getColumnIndex(Tasa.Columnas.multi));
                    int multiplicador2 = Integer.parseInt(multiplicador2s);
                    num1 = ((num1*multiplicador1)/multiplicador2);




/*


version sin sqlite3, no tomar en cuenta

                if(Text.equals("Peso")){
                    if (Text2.equals("Peso")){
                        num1 = num1;
                    }
                    else if (Text2.equals("Dolar")){
                        num1 = num1*(0.05478);
                    }
                    else if (Text2.equals("Euro")) {
                        num1 = num1*(0.0493749268);
                    }
                }
                else if(Text.equals("Dolar")){
                    if (Text2.equals("Peso")){
                        num1 = num1*(18.2548375);
                    }
                    else if (Text2.equals("Dolar")){
                        num1 = num1;
                    }
                    else if (Text2.equals("Euros")) {
                        num1 = num1*(0.901331266);
                    }
                }
                else if(Text.equals("Euro")){
                    if (Text2.equals("Peso")){
                        num1 = num1*(20.2531946);
                    }
                    else if (Text2.equals("Dolar")){
                        num1 = num1*(1.10947);
                    }
                    else if (Text2.equals("Euro")) {
                        num1 = num1;
                    }
                }*/


                /*
                no tomar en cuenta!

                txtr.setText("Resultado: " + s);
                Toast.makeText(getApplicationContext(),"El total es: "+s,Toast.LENGTH_LONG).show();
*/
                    double s = num1;
                String arry[] = new String[1];//creamos un array para pasar los datos por un intent
                arry[0]=s+"";//convertimos s a string
                Intent intento = new  Intent(getApplicationContext(),layout2.class);//declaramos el intent para iniciar nuestra siguiente layout
                intento.putExtra("datos", arry);//seteamos los datos "extras" a pasar por medio del intent
                startActivity(intento);}
                catch (Exception e){
                   Toast.makeText(getApplicationContext(),"No deje espacios en blanco ",Toast.LENGTH_LONG).show();//en caso de haber espacios en blanco mostrara un toast con el texto
            }
            }
        });

            }
    }

