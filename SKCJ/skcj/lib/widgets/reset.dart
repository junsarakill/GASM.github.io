import 'package:flutter/material.dart';
import '../database/dbHelper.dart';
import '../models/jow.dart';

class ResetButton extends StatelessWidget {
  const ResetButton({super.key});

  @override
  Widget build(BuildContext context) {
    return OutlinedButton(
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
