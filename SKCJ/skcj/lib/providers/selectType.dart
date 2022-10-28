import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:skcj/database/dbHelper.dart';
import 'package:skcj/models/jow.dart';

class selectType with ChangeNotifier {
  String _selectedValue = "0";
  String get sValue => _selectedValue;

  void setter(String value) {
    _selectedValue = value;
    notifyListeners();
  }

  //String _strResult = "99";
  //String get sResult => _strResult;

  //void setResult(String value) {
  //  _strResult = value;
  //  notifyListeners();
  //}

  String _calcResult = "99";
  String get cResult => _calcResult;

  void setCalcResult(int ssr, int sr) {
    _calcResult = (ssr * 10 + sr * 5).toString();
    notifyListeners();
  }

  String _allTypeList = "";
  String get aTList => _allTypeList;

  void setATList(String value) {
    _allTypeList = value;
    notifyListeners();
  }

  late Map<String, dynamic> _mapJow = {};
  Map<String, dynamic> get mapJow => _mapJow;

  void setMapJow(Map<String, dynamic> value) {
    _mapJow = value;
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

  void addSRJow(int type) {
    DBHelper dbHelper = DBHelper();
    dbHelper.getJow(type).then(
      (value) {
        //
        int ssr = value[0]["SSR"];
        int sr = value[0]["SR"];
        dbHelper.updateJow(Jow(type: type, ssr: ssr, sr: (sr + 1)));
      },
    );
  }

  void removeSRJow(int type) {
    DBHelper dbHelper = DBHelper();
    dbHelper.getJow(type).then(
      (value) {
        //
        int ssr = value[0]["SSR"];
        int sr = value[0]["SR"];
        dbHelper.updateJow(Jow(type: type, ssr: ssr, sr: (sr - 1)));
      },
    );
  }
}
