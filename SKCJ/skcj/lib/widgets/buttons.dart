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
            child: Align(
              alignment: Alignment.center,
              child: Text("SSR", style: TextStyle(fontSize: 20)),
            )),
        ElevatedButton(
            onPressed: () {
              context.read<selectType>().addSSRJow(int.parse(value));
            },
            child: Icon(Icons.add)),
      ],
    );
  }
}

class SRButtons extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    String value = context.watch<selectType>().sValue;
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        ElevatedButton(
            onPressed: () {
              context.read<selectType>().removeSRJow(int.parse(value));
            },
            child: Icon(Icons.remove)),
        SizedBox(
            width: 40,
            child: Align(
              alignment: Alignment.center,
              child: Text("SR", style: TextStyle(fontSize: 20)),
            )),
        ElevatedButton(
            onPressed: () {
              context.read<selectType>().addSRJow(int.parse(value));
            },
            child: Icon(Icons.add)),
      ],
    );
  }
}
