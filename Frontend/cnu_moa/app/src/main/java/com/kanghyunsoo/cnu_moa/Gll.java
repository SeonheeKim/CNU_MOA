package com.kanghyunsoo.cnu_moa;

import java.io.Serializable;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Gll implements Serializable {
    static MessageDigest md5=null;
    String title;
    String writer;
    int depart;
    int board;
    int year;
    int month;
    int day;
    int views;
    String link;
    String hash;

    public int getDay(){
        return year*365+month*31+day;
    }
}
