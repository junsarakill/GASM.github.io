import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/Utility/util.dart';
import 'package:skcj/database/dbHelper.dart';
import 'package:skcj/providers/selectType.dart';

class TypeList extends StatelessWidget {
  const TypeList({super.key});

  @override
  Widget build(BuildContext context) {
    List<String> tList = [];
    var strList = "";
    DBHelper dbHelper = DBHelper();

    dbHelper.getAllJow().then((result) {
      for (int i = 0; i < result.length; i++) {
        tList.add(
            "${convType(result[i].type)}: ssr=${result[i].ssr} sr=${result[i].sr} Result=${calcJow(result[i].ssr, result[i].sr)}");
      }
      strList = tList.join("\n\n");
      context.read<selectType>().setATList(strList);
    });

    return ListTile(
      title: Text(
        context.watch<selectType>().aTList,
        style: const TextStyle(fontSize: 20),
      ),
      onTap: () {
        Navigator.pop(context);
      },
    );
  }
}
