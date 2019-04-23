package com.laquay.apioutofthebox;

import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import com.laquay.apioutofthebox.controllers.APIController;
import com.laquay.apioutofthebox.models.Entry;

import java.util.ArrayList;

public class MainFragment extends Fragment implements APIController.ResponseServerCallback {
    public static final String TAG = MainFragment.class.getSimpleName();
    private View rootView;
    private ListView listView;
    private ArrayList<String> listValues;
    private ArrayAdapter<String> listAdapter;

    public static MainFragment newInstance() {
        return new MainFragment();
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        rootView = inflater.inflate(R.layout.fragment_main, container, false);

        setUpElements();
        setUpListeners();

        listValues = new ArrayList<>();
        listAdapter = new ArrayAdapter<>(getActivity(),
                android.R.layout.simple_list_item_1, android.R.id.text1, listValues);
        listView.setAdapter(listAdapter);

        APIController.getInstance().getAllEntries(getContext(), this);

        return rootView;
    }

    private void setUpElements() {
        listView = rootView.findViewById(R.id.entries_lv);
    }

    private void setUpListeners() {
    }

    @Override
    public void onChannelLoadServer(ArrayList<Entry> entryArrayList) {
        for (int i = 0; i < entryArrayList.size(); ++i) {
            String element = entryArrayList.get(i).toString();
            Log.e(TAG, element);
            listValues.add(element);
        }
        listAdapter.notifyDataSetChanged();
    }
}
