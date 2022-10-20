import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/providers/counts.dart';

class Counter extends StatelessWidget {
  int idx;
  List<String> cntName = ["Blue", "Red", "Yellow", "Purple", "Green"];

  Counter({this.idx = 0});

  @override
  Widget build(BuildContext context) {
    print('Counter');

    return Text(
      "${cntName[idx]} ${context.watch<Counts>().getCnt(idx)}",
      style: TextStyle(
        fontSize: 20,
      ),
    );
  }
}
