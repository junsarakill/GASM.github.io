import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:skcj/database/dbHelper.dart';
import 'package:skcj/models/jow.dart';

class selectType with ChangeNotifier {
  String _selectedValue = "0";
  String get sValue => _selectedValue;

  String _strResult = "";
  String get sResult => _strResult;

  void setter(String value) {
    _selectedValue = value;
    print("현재 값: $_selectedValue");
    notifyListeners();
  }

  void setResult(String value) {
    _strResult = value;
    print("현재 값: $_strResult");
    notifyListeners();
  }

  void addSSRJow(int type) {
    DBHelper dbHelper = DBHelper();
    dbHelper.getJow(type).then(
      (value) {
        //
        int ssr = value[0]["SSR"];
        int sr = value[0]["SR"];
        dbHelper.updateJow(Jow(type: type, ssr: (ssr + 1), sr: sr));
      },
    );
  }

  void removeSSRJow(int type) {
    DBHelper dbHelper = DBHelper();
    dbHelper.getJow(type).then(
      (value) {
        //
        int ssr = value[0]["SSR"];
        int sr = value[0]["SR"];
        dbHelper.updateJow(Jow(type: type, ssr: (ssr - 1), sr: sr));
      },
    );
  }
}
