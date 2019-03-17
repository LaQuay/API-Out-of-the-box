package com.laquay.apioutofthebox.controllers;

import android.content.Context;
import android.util.Log;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.laquay.apioutofthebox.models.Entry;
import com.laquay.apioutofthebox.utils.APIUtils;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class APIController {
    public static final String TAG = APIController.class.getSimpleName();
    private static APIController instance;

    private APIController() {
    }

    public static APIController getInstance() {
        if (instance == null) {
            createInstance();
        }
        return instance;
    }

    private synchronized static void createInstance() {
        if (instance == null) {
            instance = new APIController();
        }
    }

    public void getAllEntries(final Context context, final ResponseServerCallback responseServerCallback) {
        Log.i(TAG, "Load channels from server: " + APIUtils.ENTRY_BASE_URL);
        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(
                Request.Method.GET,
                APIUtils.ENTRY_BASE_URL,
                null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        Log.i(TAG, "Response OK");

                        try {
                            JSONArray data = response.getJSONArray("data");

                            ArrayList<Entry> entryArrayList = new ArrayList<>();
                            int id;
                            String value;
                            String date;
                            for (int i = 0; i < data.length(); ++i) {
                                JSONObject entryJSON = data.getJSONObject(i);

                                id = entryJSON.getInt("id");
                                value = entryJSON.getString("value");
                                date = entryJSON.getString("date");

                                entryArrayList.add(new Entry(id, value, date));
                            }

                            responseServerCallback.onChannelLoadServer(entryArrayList);
                        } catch (JSONException e) {
                            Log.e(TAG, "ERROR Parsing JSON");
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Do something when error occurred
                        Log.e(TAG, "Error while accessing to: " + APIUtils.ENTRY_BASE_URL);
                    }
                }
        );

        // Add JsonArrayRequest to the RequestQueue
        VolleyController.getInstance(context).addToQueue(jsonObjectRequest);
    }

    public interface ResponseServerCallback {
        void onChannelLoadServer(ArrayList<Entry> entryArrayList);
    }
}
