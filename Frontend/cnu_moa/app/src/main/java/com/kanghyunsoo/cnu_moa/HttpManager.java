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

public class HttpManager {
    static String result="";
    public void request(final Handler handler,final String _url, final int depart,final int board,final int year,final int month,final int day) {
        Thread t = new Thread() {
            public void run() {
                HttpURLConnection urlConn = null;
                String params = String.format("?depart=%d&board=%d&year=%d&month=%d&day=%d", depart, board, year, month, day);

                try {
                    URL url = new URL(_url + params);
                    urlConn = (HttpURLConnection) url.openConnection();

                    urlConn.setRequestMethod("GET");
                    urlConn.setDoInput(true);
                    urlConn.setDoOutput(true);
                    urlConn.setUseCaches(false);
                    urlConn.setDefaultUseCaches(false);
                    urlConn.connect();
                    urlConn.getOutputStream().close();

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
