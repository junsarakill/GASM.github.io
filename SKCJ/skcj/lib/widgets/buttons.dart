import 'dart:async';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/database/dbHelper.dart';
import 'package:skcj/providers/selectType.dart';

class SSRButtons extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    String value = context.watch<selectType>().sValue;
    DBHelper dbHelper = DBHelper();
    Future asd = dbHelper.getJow(int.parse(value));

    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        const Image(image: AssetImage("assets/20000000.png")),
        Column(
          children: [
            const SizedBox(
              child: Text(
                "asd",
                style: TextStyle(fontSize: 20),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                    onPressed: () {
                      context.read<selectType>().removeSSRJow(int.parse(value));
                    },
                    child: const Icon(Icons.remove)),
                ElevatedButton(
                    onPressed: () {
                      context.read<selectType>().addSSRJow(int.parse(value));
                    },
                    child: const Icon(Icons.add)),
              ],
            )
          ],
        )
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
        const Image(image: AssetImage("assets/10000000.png")),
        ElevatedButton(
            onPressed: () {
              context.read<selectType>().removeSRJow(int.parse(value));
            },
            child: const Icon(Icons.remove)),
        ElevatedButton(
            onPressed: () {
              context.read<selectType>().addSRJow(int.parse(value));
            },
            child: const Icon(Icons.add)),
      ],
    );
  }
}
