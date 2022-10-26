import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/database/dbHelper.dart';
import 'package:skcj/providers/selectType.dart';

class sType extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    String value = context.watch<selectType>().sValue;
    DBHelper dbHelper = DBHelper();

    dbHelper.getJow(int.parse(value)).then((result) {
      context.read<selectType>().setResult(result[0].toString());
      context
          .read<selectType>()
          .setCalcResult(result[0]["SSR"], result[0]["SR"]);
    });

    return Column(
      children: [
        Text(context.watch<selectType>().sResult,
            style: TextStyle(
              fontSize: 20,
            )),
        Text("합계: ${context.watch<selectType>().cResult}",
            style: TextStyle(
                fontSize: 30,
                color: int.parse(context.watch<selectType>().cResult) >= 178
                    ? Colors.red
                    : Colors.blue))
      ],
    );
  }
}
