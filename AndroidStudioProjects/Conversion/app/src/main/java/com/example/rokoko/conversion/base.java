package com.example.rokoko.conversion;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

/**
 * Created by RoKoKo on 23/02/2016.
 */


public class base extends SQLiteOpenHelper {//heredamos de la clase Openhelper para el funcionamiento de la base

    public base(Context context){
        super(context,"tasa3.db", null, 1);
    }//context,nombre del archivo de la base.db, null, version
    @Override
    public void onCreate(SQLiteDatabase db) {
        //Crear la base de datos
        //Crear la tabla Tasa
        db.execSQL(Tasa.CREATE_TABLE);
        //Insertar registros iniciales
        db.execSQL(Tasa.INSERT_SCRIPT);


    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        //Actualizar la base de datos
    }

}