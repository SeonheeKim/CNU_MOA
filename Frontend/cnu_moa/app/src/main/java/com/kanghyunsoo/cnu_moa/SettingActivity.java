package com.kanghyunsoo.cnu_moa;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

public class SettingActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener {
    Spinner spinner;
    TextView tv;
    ArrayAdapter<String> adapter;
    int selectedDepartId=0;
    DataManager dm=DataManager.getInstance();
    public void onCreate(Bundle b){
        super.onCreate(b);
        setContentView(R.layout.activity_setting);
        spinner=findViewById(R.id.setting_spinner);
        tv=findViewById(R.id.setting_tv);
        String names[]=new String[dm.departs.size()];
        int i=0;
        for(Depart d : dm.departs){
            names[i++]=d.name;
        }
        adapter=new ArrayAdapter<String>(this,R.layout.support_simple_spinner_dropdown_item,names);
        spinner.setAdapter(adapter);
        spinner.setOnItemSelectedListener(this);
        refresh();
    }

    void refresh(){
        String asdf="";
        for(Depart d : dm.loadDeparts){
            asdf+=d.name;
            asdf+="\n";
        }
        tv.setText(asdf);
    }
    public void onClick(View v){
        switch(v.getId()){
            case R.id.setting_bt_add:
                dm.addLoadDepart(dm.departs.get(selectedDepartId));
                refresh();

                break;
            case R.id.setting_bt_reload:
                dm.sYear=1999;dm.sMonth=1;dm.sDay=1;
                onBackPressed();
                break;
            case R.id.setting_bt_reset:
                dm.sYear=1999;dm.sMonth=1;dm.sDay=1;
                dm.loadDeparts.clear();
                dm.loadDeparts.add(dm.departs.get(0));
                dm.glls.clear();
                dm.save();
                refresh();
                break;
        }
    }
    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int pos, long id) {
        selectedDepartId=pos;
    }

    @Override
    public void onNothingSelected(AdapterView<?> adapterView) {
    }


    @Override
    public void onBackPressed(){
        if(dm.save()){
            Toast.makeText(this,"설정 저장 완료",Toast.LENGTH_SHORT).show();
        }else{
            Toast.makeText(this,"설정 저장 실패",Toast.LENGTH_SHORT).show();
        }
        finish();
    }
}
