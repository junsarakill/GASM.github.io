import 'package:flutter/material.dart';
import 'package:skcj/database/dbHelper.dart';
import 'package:skcj/models/jow.dart';

class ResetButton extends StatelessWidget {
  const ResetButton({super.key});

  @override
  Widget build(BuildContext context) {
    return OutlinedButton(
        //초기 값으로 복구
        onPressed: () {
          DBHelper dbHelper = DBHelper();
          dbHelper.insertJow(Jow(type: 0, ssr: 0, sr: 0));
          dbHelper.insertJow(Jow(type: 1, ssr: 0, sr: 0));
          dbHelper.insertJow(Jow(type: 2, ssr: 0, sr: 0));
          dbHelper.insertJow(Jow(type: 3, ssr: 0, sr: 0));
          dbHelper.insertJow(Jow(type: 4, ssr: 0, sr: 0));
        },
        child: const Text("Reset"));
  }
}
