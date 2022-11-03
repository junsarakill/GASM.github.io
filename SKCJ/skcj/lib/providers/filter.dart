import 'package:flutter/cupertino.dart';

import '../models/imgInfo.dart';

class filter with ChangeNotifier {
  List<String> _selectedFilter = [];
  List<String> get sFilter => _selectedFilter;

  void setter(String value) {
    _selectedFilter.add(value);
    print(_selectedFilter);
    notifyListeners();
  }

  List<String> _cardList = [];
  List<String> get cList => _cardList;

  void setCardList(List<imgInfo> value) {
    for (int i = 0; i < value.length; i++) {
      _cardList.add(value[i].toString());
    }
    notifyListeners();
  }
}
