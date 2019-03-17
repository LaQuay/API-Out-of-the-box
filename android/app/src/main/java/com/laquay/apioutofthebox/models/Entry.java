package com.laquay.apioutofthebox.models;

public class Entry {
    private int id;
    private String value;
    private String data;

    public Entry(int id, String value, String data) {
        this.id = id;
        this.value = value;
        this.data = data;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
}
