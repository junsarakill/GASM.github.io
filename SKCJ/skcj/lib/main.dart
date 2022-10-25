import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/database/dbHelper.dart';
import 'package:skcj/providers/selectType.dart';
import 'package:skcj/widgets/buttons.dart';
import 'package:skcj/widgets/sType.dart';

import 'models/jow.dart';

final _valueList = ["0", "1", "2", "3", "4"];
var _selectedValue = "0";

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(
    MultiProvider(
      providers: [
        //ChangeNotifierProvider(create: (_) => Counts()),
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
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              OutlinedButton(
                  onPressed: () {
                    DBHelper dbHelper = DBHelper();
                    dbHelper.insertJow(Jow(type: 4, ssr: 0, sr: 0));
                  },
                  child: Text("DB insert")),
              DropdownType(),
              sType(),
              OutlinedButton(
                  onPressed: () {
                    DBHelper dbHelper = DBHelper();
                    dbHelper.getAllJow().then((value) => value.forEach((e) {
                          print("type: ${e.type},ssr: ${e.ssr},sr: ${e.sr}");
                        }));
                  },
                  child: Text("DB select")),
              SSRButtons(),
            ],
            //children: [Counter(idx: 0), Buttons(idx: 0)],
          ),
        ),
      ),
    );
  }
}

class DropdownType extends StatefulWidget {
  const DropdownType({super.key});

  @override
  State<DropdownType> createState() => _DropdownTypeState();
}

class _DropdownTypeState extends State<DropdownType> {
  String dropdownValue = _valueList.first;

  @override
  Widget build(BuildContext context) {
    return DropdownButton<String>(
      value: dropdownValue,
      icon: const Icon(Icons.arrow_downward),
      elevation: 16,
      style: const TextStyle(color: Colors.deepPurple),
      underline: Container(
        height: 2,
        color: Colors.deepPurpleAccent,
      ),
      onChanged: (String? value) {
        setState(() {
          dropdownValue = value!;
          context.read<selectType>().setter(dropdownValue);
        });
      },
      items: _valueList.map<DropdownMenuItem<String>>((String value) {
        return DropdownMenuItem<String>(value: value, child: Text(value));
      }).toList(),
    );
  }
}
