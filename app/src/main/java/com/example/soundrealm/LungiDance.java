package com.example.soundrealm;

import android.app.Activity;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ImageButton;
import android.widget.Toast;

public class LungiDance extends Activity implements OnClickListener{
	
	ImageButton bb1,bb2,bb3;
	MediaPlayer mp;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_lungi_dance);
		bb1=(ImageButton)findViewById(R.id.imageButton1);
		bb2=(ImageButton)findViewById(R.id.imageButton2);
		bb3=(ImageButton)findViewById(R.id.imageButton3);
		mp=MediaPlayer.create(LungiDance.this,R.raw.lungi);
		bb1.setOnClickListener(new OnClickListener() {
	
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				Toast.makeText(LungiDance.this, "Playing", Toast.LENGTH_LONG).show();
				mp.start();
				
			}
		});
		
		bb2.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				Toast.makeText(LungiDance.this, "Paused", Toast.LENGTH_LONG).show();
				mp.pause();
			}
		});
		
		bb3.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				// TODO Auto-generated method stub
				Toast.makeText(LungiDance.this, "Stopped", Toast.LENGTH_LONG).show();
				mp.release();
			}
		});
	}

	@Override
	public void onClick(View v) {
		// TODO Auto-generated method stub
		
	}

	
}
