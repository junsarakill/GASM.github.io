import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:provider/provider.dart';
import 'package:skcj/providers/counts.dart';
import 'package:skcj/widgets/buttons.dart';
import 'package:skcj/widgets/counter.dart';

//타입, ssr 개수, sr 개수
class Type {
  String? type;
  int? ssr = 0;
  int? sr = 0;

  Type(String this.type);

  @override
  String toString() {
    return "Type: {type: ${type}, ssr: ${ssr}, sr: ${sr}}";
  }
}

void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => Counts()),
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
  List<Object> typeList = [
    Type("blue"),
    Type("red"),
    Type("yellow"),
    Type("purple"),
    Type("green")
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Provider"),
      ),
      body: ChangeNotifierProvider(
        create: (BuildContext context) => Counts(),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [Counter(idx: 0), Buttons(idx: 0)],
          ),
        ),
      ),
    );
  }
}
