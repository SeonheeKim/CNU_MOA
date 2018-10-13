package com.kanghyunsoo.cnu_moa;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.icu.util.Calendar;
import android.icu.util.GregorianCalendar;
import android.net.Uri;
import android.os.Handler;
import android.os.Message;
import android.support.v4.widget.SwipeRefreshLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.File;
import java.util.ArrayList;
import java.util.Locale;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemClickListener, SwipeRefreshLayout.OnRefreshListener {
    ListView lv;
    TextView tvTime;
    HttpManager hm;
    final String url="http://18.188.69.148:8000";
    ArrayAdapter<String> adapter;
    ArrayList<String> texts,links;
    SwipeRefreshLayout swipeRefreshLayout;
    DataManager dm=DataManager.getInstance();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        dm.fileData=new File(getFilesDir().toString(),"load");

        arrayInit();
        viewInit();
        loading();
        hm = new HttpManager();
        refresh();
    }
    void loading(){
        if(dm.load()){
            Toast.makeText(this,"불러오기 성공",Toast.LENGTH_SHORT).show();
        }else{
            Toast.makeText(this,"불러오기 실패",Toast.LENGTH_SHORT).show();
            dm.addLoadDepart(dm.departs.get(0));
            dm.addLoadDepart(dm.departs.get(1));
        }
    }
    void arrayInit(){
        texts=new ArrayList<>();
        links=new ArrayList<>();
    }
    private void viewInit(){
        swipeRefreshLayout=findViewById(R.id.main_swipe);
        swipeRefreshLayout.setOnRefreshListener(this);
        lv=findViewById(R.id.main_lv);
        adapter=new ArrayAdapter<String>(this,android.R.layout.simple_expandable_list_item_1,texts);
        lv.setAdapter(adapter);
        lv.setOnItemClickListener(this);
        tvTime=findViewById(R.id.main_tv_time);
        refreshTime();
    }

    public void onClick(View v){
        switch(v.getId()){
            case R.id.main_bt_setting:
                    Intent intent = new Intent(this,SettingActivity.class);
                    startActivity(intent);
                break;
        }
    }

    public void onRecieve(String result){
        Log.d("khs","onRecieve");
        Log.d("khs",result);
        try {
            JSONArray jarray = new JSONArray(result);
            for(int i=0;i<jarray.length();i++){
                JSONObject jObject=jarray.getJSONObject(i);
                Gll gll = new Gll();
                gll.title = jObject.getString("title");
                gll.writer = jObject.getString("writer");
                gll.depart = jObject.getInt("depart");
                gll.board = jObject.getInt("board");
                gll.year = jObject.getInt("year");
                gll.month=jObject.getInt("month");
                gll.day=jObject.getInt("day");
                gll.views=jObject.getInt("views");
                gll.link=jObject.getString("link");
                dm.glls.add(gll);
            }
            sortGll();
            adapter.notifyDataSetChanged();
        }catch(Exception e){
            e.printStackTrace();
        }finally{
            swipeRefreshLayout.setRefreshing(false);
        }
    }

    void sortGll(){
        dm.sortGlls();

        Log.d("khs","glls.size(): "+dm.glls.size());
        texts.clear();
        links.clear();
        for(Gll gll : dm.glls){
            String text=String.format(Locale.KOREA,"[%s][%s]%s |%s|%s|%d-%d-%d",dm.getDepartName(gll.depart),dm.getBoardName(gll.depart,gll.board),gll.title,gll.writer,gll.views,gll.year,gll.month,gll.day);
            texts.add(text);
            links.add(gll.link);
        }
    }

    void refresh(){
        Depart depart;
        for(int i=0;i<dm.loadDeparts.size();i++){
            depart=dm.loadDeparts.get(i);
            for(int j=0;j<depart.boards.size();j++){
                hm.request(handler,url,depart.id,depart.boards.get(j).id,dm.sYear,dm.sMonth,dm.sDay);
            }
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        refresh();
    }

    void refreshTime(){
        tvTime.setText(String.format(Locale.KOREA,"기준 날짜: %d년%d월%d일",dm.sYear,dm.sMonth,dm.sDay));
    }
    @Override
    public void onRefresh() {
        refresh();
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int pos, long id) {
        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse( links.get(pos)  ));
        startActivity(intent);
    }


    @SuppressLint("HandlerLeak")
    Handler handler = new Handler(){
        public void handleMessage(Message m){
            if(m.what==11){
                onRecieve(HttpManager.result);
                sendEmptyMessageDelayed(12,1000);
            }
            if(m.what==12){
                long tt=System.currentTimeMillis();
                Calendar cal = new GregorianCalendar();
                dm.sYear=cal.get(Calendar.YEAR);
                dm.sMonth=cal.get(Calendar.MONTH)+1;
                dm.sDay=cal.get(Calendar.DAY_OF_MONTH);
                refreshTime();
            }
        }
    };

    @Override
    public void onBackPressed(){
        if(dm.save()){
            Toast.makeText(this,"저장 완료",Toast.LENGTH_SHORT).show();
        }else{
            Toast.makeText(this,"저장 실패",Toast.LENGTH_SHORT).show();
        }
        finish();
    }

}
