package com.example.rokoko.conversion;

import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.provider.BaseColumns;

/**
 * Created by RoKoKo on 23/02/2016.
 */
public class Tasa {
    public static final String TABLE_NAME = "tasa";
    public static final String STRING_TYPE = "text";//revisar documentacion de sqlite3 para los tipos de objetos
    public static final String INT_TYPE = "integer";
    public static class Columnas{
        public static final String ID = BaseColumns._ID;
        public static final String pais = "pais";
        public static final String multi= "multiplicador";
    }
    public static final String CREATE_TABLE =
            "create table "+TABLE_NAME+"(" +
                    Columnas.ID+" "+INT_TYPE+" primary key autoincrement," +
                    Columnas.pais+" "+STRING_TYPE+" not null," +
                    Columnas.multi+" "+INT_TYPE+" not null)";
    public static final String INSERT_SCRIPT =
            "insert into "+TABLE_NAME+" values(" +
                    "null," +
                    "\"Peso\"," +
                    "100)," +
                    "(null," +
                    "\"Dolar\"," +
                    "1821)," +
                    "(null," +
                    "\"Euro\"," +
                    "2007)";//nota el slash invertido + comillas es fundamental para cualquier elemento de tipo string

    private base openHelper;
    private SQLiteDatabase database;


    public Tasa(Context context) {
        //Creando una instancia hacia la base de datos
        openHelper = new base(context);
        database = openHelper.getWritableDatabase();
    }

    public Cursor getAll(){
        //Seleccionamos todas las filas de la tabla Quotes
        return database.rawQuery(
                "select * from " + TABLE_NAME, null);
    }
    public Cursor getmulti(String paisa) {

        //Argumentos del WHERE
        String selectionArgs[] = new String[]{paisa};


        String query =
                "select "+Tasa.Columnas.multi+
                        " from "+Tasa.TABLE_NAME +
                        " where "+Tasa.Columnas.pais+
                        "= ?";
        return database.rawQuery(query,selectionArgs);
    }

}

