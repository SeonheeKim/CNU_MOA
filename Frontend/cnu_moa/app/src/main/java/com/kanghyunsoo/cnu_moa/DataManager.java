package com.kanghyunsoo.cnu_moa;

import android.util.Log;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

public class DataManager {
    private static final DataManager ins=new DataManager();
    public static DataManager getInstance(){
        return ins;
    }
    File fileData;
    ArrayList<Depart> departs;
    ArrayList<Depart> loadDeparts;
    ArrayList<Gll> glls;
    int sYear=1999,sMonth=1,sDay=1;

    public DataManager(){

        glls=new ArrayList<>();
        departs=new ArrayList<>();
        loadDeparts=new ArrayList<>();
        departs.add(new Depart(1,"컴퓨터공학과")
                .add(1,"학사공지")
                .add(2,"일반공지")
                .add(3,"사업단소식")
                .add(4,"취업정보"));
        departs.add(new Depart(2,"학생생활관")
                .add(1,"은행사 공지")
                .add(2,"백행사 공지"));
    }
    void sortGlls(){
        ArrayList<Gll> remove=new ArrayList<>();
        Log.d("khs","sorting");
        for(int i=0;i<glls.size();i++){
            for(int j=i;j<glls.size();j++){
                if(i!=j)
                    if(glls.get(i).link.equals(glls.get(j).link))
                        remove.add(glls.get(i));
            }
        }
        glls.removeAll(remove);
        for(int i=1;i<glls.size();i++){
            Gll preGll=glls.get(i-1);
            Gll currentGll=glls.get(i);
            if(preGll.getDay()<currentGll.getDay()){
                glls.remove(i-1);
                glls.add(i,preGll);
            }
        }
    }

    String getDepartName(int id){
        for(Depart d : departs){
            if(d.id==id)
                return d.name;
        }
        return "알수없음";
    }
    String getBoardName(int did,int bid){
        for(Depart d : departs){
            if(d.id==did){
                for(Board b : d.boards){
                    if(b.id==bid)
                        return b.name;
                }
            }
        }
        return "알수없음";
    }

    void addLoadDepart(Depart d){
        if(!loadDeparts.contains(d))
            loadDeparts.add(d);
    }

    boolean save(){
        try {
            fileData.createNewFile();
            ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileData));
            oos.writeObject(loadDeparts);
            oos.writeObject(glls);
            oos.writeInt(sYear);
            oos.writeInt(sMonth);
            oos.writeInt(sDay);
            oos.flush();
            oos.close();
            return true;
        }catch(Exception e){
            e.printStackTrace();
            return false;
        }
    }
    boolean load(){
        try {
            if(!fileData.exists())
                return false;
            ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileData));
            loadDeparts=(ArrayList<Depart>)ois.readObject();
            glls=(ArrayList<Gll>)ois.readObject();
            sYear=ois.readInt();
            sMonth=ois.readInt();
            sDay=ois.readInt();
            ois.close();
            return true;
        }catch(Exception e){
            e.printStackTrace();
            return false;
        }
    }

}
