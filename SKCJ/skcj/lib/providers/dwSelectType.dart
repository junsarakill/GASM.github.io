import 'dart:developer';

import 'package:flutter/cupertino.dart';

class dwSelectType with ChangeNotifier {
  final List<int> _selectedValue = [0, 0, 0, 0];
  List<int> get sValue => _selectedValue;

  void setter(int index, int value) {
    _selectedValue[index] = value;
    print("$sValue");
    notifyListeners();
  }

  final List<int> _resultValue = [0, 0, 0, 0];
  List<int> get rValue => _resultValue;

  void setResult() {
    Map<int, int> cnt = {0: 0};

    sValue.forEach((e) {
      int? cNum = cnt[e];
      if (cNum == null) {
        cnt[e] = 1;
      } else {
        cnt[e] = cNum + 1;
      }
    });
    print(cnt);
    _resultValue[0] = Mobius(sValue[0] - 1);
    _resultValue[1] = Mobius(sValue[0] - 1);
    for (var e in cnt.values) {
      if (e > 1) {
        if (cnt[sValue[0]] == e) {
          _resultValue[2] = Mobius(sValue[0] - 1);
          _resultValue[3] = Mobius(sValue[0] - 1);
          break;
        }
        _resultValue[2] =
            Mobius(cnt.keys.firstWhere((element) => cnt[element] == e) - 1);
        _resultValue[3] =
            Mobius(cnt.keys.firstWhere((element) => cnt[element] == e) - 1);
        break;
      } else {
        _resultValue[2] = Mobius(sValue[0] - 1);
        _resultValue[3] = Mobius(sValue[0] - 1);
      }
    }
    print(_resultValue);
  }

  int _index = 0;
  int get idx => _index;

  void setIndex(int value) {
    _index = value;
    notifyListeners();
  }
}

//속성용 순환 숫자 반환
int Mobius(int value) {
  if (value < 0) {
    return Mobius(value + 5);
  } else if (value >= 5) {
    return Mobius(value - 5);
  } else {
    return value;
  }
}
