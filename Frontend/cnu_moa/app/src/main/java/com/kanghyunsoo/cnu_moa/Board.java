package com.kanghyunsoo.cnu_moa;

import android.widget.ArrayAdapter;

import java.io.Serializable;
import java.util.ArrayList;

public class Board implements Serializable {
    public int id;
    public String name;
    public Board(int id,String name){
        this.id=id;
        this.name=name;
    }
}
