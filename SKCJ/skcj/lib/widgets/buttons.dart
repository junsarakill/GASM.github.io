import 'dart:async';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/database/dbHelper.dart';
import 'package:skcj/providers/selectType.dart';

class SSRButtons extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    String value = context.watch<selectType>().sValue;
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        ElevatedButton(
            onPressed: () {
              context.read<selectType>().removeSSRJow(int.parse(value));
            },
            child: Icon(Icons.remove)),
        SizedBox(
          width: 40,
        ),
        ElevatedButton(
            onPressed: () {
              context.read<selectType>().addSSRJow(int.parse(value));
            },
            child: Icon(Icons.add)),
      ],
    );
  }
}
