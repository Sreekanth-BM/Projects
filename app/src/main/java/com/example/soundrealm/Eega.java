package com.example.soundrealm;

import android.app.Activity;
import android.app.ListActivity;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class Eega extends ListActivity {
	
	String [] cl={"EegaTheme","Lava"};

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		//setContentView(R.layout.activity_devotional);
		getWindow().getDecorView().setBackgroundColor(Color.GREEN);
		setListAdapter(new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1,cl));
	}

	@Override
	protected void onListItemClick(ListView l, View v, int position, long id) {
		// TODO Auto-generated method stub
		super.onListItemClick(l, v, position, id);
		try {
			
			Class c=Class.forName("com.example.soundrealm."+cl[position]);
			Intent i=new Intent(this,c);
			startActivity(i);
			
		} catch (Exception e) {
			// TODO: handle exception
		}
	}
	
	
	
}
