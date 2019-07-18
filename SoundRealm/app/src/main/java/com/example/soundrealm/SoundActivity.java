package com.example.soundrealm;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;

public class SoundActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_sound);
		Thread t=new Thread()
		{
				public void run()
				{
					try {
						sleep(1000);
						Intent i=new Intent(SoundActivity.this, Genre.class);
						startActivity(i);
					} 
					catch (Exception e) {
						// TODO Auto-generated catch block
						
					}
					
				}
		};
		t.start();
		
	}

	
}
