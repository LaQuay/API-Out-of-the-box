package com.laquay.apioutofthebox.controller;

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

    public interface ResponseServerCallback {
        void onChannelLoadServer(String data);
    }
}
