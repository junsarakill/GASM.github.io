import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class Counts with ChangeNotifier {
  Future setNumValue() async {
    final prefs = await SharedPreferences.getInstance();
    prefs.setInt("counter", 11);
  }

  final List<int> _cntList = [0, 0, 0, 0, 0];

  int getCnt(int idx) {
    int cnt = _cntList[idx];

    return cnt;
  }

  void add(int idx) {
    _cntList[idx]++;
    notifyListeners();
  }

  void remove(int idx) {
    _cntList[idx]--;
    notifyListeners();
  }
}
