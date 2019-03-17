package com.laquay.apioutofthebox;

import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.laquay.apioutofthebox.controllers.APIController;
import com.laquay.apioutofthebox.models.Entry;

import java.util.ArrayList;

public class MainFragment extends Fragment implements APIController.ResponseServerCallback {
    public static final String TAG = MainFragment.class.getSimpleName();
    private View rootView;

    public static MainFragment newInstance() {
        return new MainFragment();
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        rootView = inflater.inflate(R.layout.fragment_main, container, false);

        setUpElements();
        setUpListeners();

        APIController.getInstance().getAllEntries(getContext(), this);

        return rootView;
    }

    private void setUpElements() {
    }

    private void setUpListeners() {
    }

    @Override
    public void onChannelLoadServer(ArrayList<Entry> entryArrayList) {
        for (int i = 0; i < entryArrayList.size(); ++i) {
            Log.e(TAG, entryArrayList.get(i).toString());
        }
    }
}
