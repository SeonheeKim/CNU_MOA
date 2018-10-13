package com.kanghyunsoo.cnu_moa;

import android.os.Handler;

import org.json.JSONArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Locale;

public class HttpManager {
    static String result="";
    public void request(final Handler handler,final String _url, final int depart,final int board,final int year,final int month,final int day) {
        Thread t = new Thread() {
            public void run() {
                HttpURLConnection urlConn = null;
                String params = String.format(Locale.KOREA,"/%d/%d/%d/%d/%d?format=json", depart, board, year, month, day);

                try {
                    URL url = new URL(_url + params);
                    urlConn = (HttpURLConnection) url.openConnection();
                    urlConn.setRequestMethod("GET");
                    urlConn.setRequestProperty("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8");
                    urlConn.setRequestProperty("Accept-Encoding","gzip, deflate");
                    urlConn.setRequestProperty("Accept-Language","ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7");
                    urlConn.setRequestProperty("Cache-Control","max-age=0");
                    urlConn.setRequestProperty("Connection","keep-alive");
                    urlConn.setRequestProperty("Host","18.188.69.148:8000");
                    urlConn.setRequestProperty("Upgrade-Insecure-Requests","1");
                    urlConn.setRequestProperty("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36");

                    if (urlConn.getResponseCode() != HttpURLConnection.HTTP_OK)
                        return;

                    BufferedReader reader = new BufferedReader(new InputStreamReader(urlConn.getInputStream(), "UTF-8"));

                    String line;
                    String page = "";

                    while ((line = reader.readLine()) != null) {
                        page += line + "\n";
                    }
                    result = page;
                    handler.sendEmptyMessage(11);
                    return;
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                } finally {
                    if (urlConn != null)
                        urlConn.disconnect();
                }
                return;
            }
        };
        t.start();
    }
}
