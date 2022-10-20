import 'dart:async';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/providers/counts.dart';

class Buttons extends StatelessWidget {
  int idx;

  Buttons({this.idx = 0});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        ElevatedButton(
            onPressed: () {
              context.read<Counts>().add(idx);
            },
            //onLongPress: () {
            //  Timer.periodic(const Duration(milliseconds: 200), (timer) {
            //    context.read<Counts>().add();
            //  });
            //},
            child: Icon(Icons.add)),
        SizedBox(
          width: 40,
        ),
        ElevatedButton(
            onPressed: () {
              context.read<Counts>().remove(idx);
            },
            child: Icon(Icons.remove))
      ],
    );
  }
}
