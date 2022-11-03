import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/providers/dwSelectType.dart';
import 'package:skcj/providers/selectType.dart';
import 'package:skcj/widgets/calcJow/calcJow.dart';
import 'package:skcj/widgets/camera.dart';
import 'package:skcj/widgets/recGroup/RecGroup.dart';
import 'package:skcj/widgets/skgs/skgs.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => selectType()),
        ChangeNotifierProvider(create: (_) => dwSelectType()),
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
      title: 'GameAssistanceSiteMatome',
      theme: ThemeData(
        primarySwatch: Colors.purple,
      ),
      home: const Home(),
    );
  }
}

//메인 화면
class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Navigate")),
      body: Center(
          child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          //행운 계산
          ElevatedButton(
              child: const Text("CalcJow"),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => const CalcJow()),
                );
              }),
          //대응 편성 추천
          ElevatedButton(
              child: const Text("RecGroup"),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => const RecGroup()),
                );
              }),
          //각성목록
          ElevatedButton(
              child: const Text("SKGS"),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => const SKGS()),
                );
              })
        ],
      )),
      //사진 찍기
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (_) => const Camera()),
          );
        },
        tooltip: 'camera',
        child: const Icon(Icons.camera_alt_sharp),
      ),
    );
  }
}
