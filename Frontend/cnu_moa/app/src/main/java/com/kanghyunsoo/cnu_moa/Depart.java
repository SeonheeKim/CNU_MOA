package com.kanghyunsoo.cnu_moa;

import java.io.Serializable;
import java.util.ArrayList;

public class Depart implements Serializable {
    public int id;
    public String name;
    public ArrayList<Board> boards;

    public Depart(int id,String name){
        this.id=id;
        this.name=name;
        boards= new ArrayList<>();
    }

    public Depart add(int id,String name){
        boards.add(new Board(id,name));
        return this;
    }
}
