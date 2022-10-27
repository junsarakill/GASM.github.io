import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/database/dbHelper.dart';
import 'package:skcj/providers/selectType.dart';
import 'package:skcj/widgets/buttons.dart';
import 'package:skcj/widgets/dropdown.dart';
import 'package:skcj/widgets/sType.dart';
import 'package:skcj/widgets/tyleList.dart';

import 'models/jow.dart';

const valueList = ["0", "1", "2", "3", "4"];
const selectedValue = "0";

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  DBHelper dbHelper = DBHelper();

  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => selectType()),
      ],
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SenranKaguraCalculateJow',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Home(),
    );
  }
}

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Dropdown"),
      ),
      body: ChangeNotifierProvider(
        create: (BuildContext context) => selectType(),
        child: Container(
          child: ListView(
            children: [
              OutlinedButton(
                  onPressed: () {
                    DBHelper dbHelper = DBHelper();
                    dbHelper.insertJow(Jow(type: 0, ssr: 0, sr: 0));
                    dbHelper.insertJow(Jow(type: 1, ssr: 0, sr: 0));
                    dbHelper.insertJow(Jow(type: 2, ssr: 0, sr: 0));
                    dbHelper.insertJow(Jow(type: 3, ssr: 0, sr: 0));
                    dbHelper.insertJow(Jow(type: 4, ssr: 0, sr: 0));
                  },
                  child: Text("Reset")),
              DropdownType(),
              sType(),
              SSRButtons(),
              SRButtons(),
            ],
            //children: [Counter(idx: 0), Buttons(idx: 0)],
          ),
        ),
      ),
      drawer: Drawer(
          child: ListView(
        padding: EdgeInsets.zero,
        children: [
          const SizedBox(
            height: 100,
            child: DrawerHeader(
              decoration: BoxDecoration(
                color: Colors.blue,
              ),
              child: Text(
                "All type",
                style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                    color: Colors.white),
              ),
            ),
          ),
          TypeList(),
        ],
      )),
    );
  }
}
