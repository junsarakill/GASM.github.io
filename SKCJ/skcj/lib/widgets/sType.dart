import 'package:flutter/cupertino.dart';
import 'package:provider/provider.dart';
import 'package:skcj/database/dbHelper.dart';
import 'package:skcj/providers/selectType.dart';

class sType extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    String strResult = "";
    String value = context.watch<selectType>().sValue;
    DBHelper dbHelper = DBHelper();

    dbHelper.getJow(int.parse(value)).then((result) {
      strResult = result[0].toString();
      context.read<selectType>().setResult(strResult);
    });

    return Text(context.watch<selectType>().sResult,
        style: TextStyle(
          fontSize: 20,
        ));
  }
}
