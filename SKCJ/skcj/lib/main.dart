import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/providers/selectType.dart';
import 'package:skcj/widgets/buttons.dart';
import 'package:skcj/widgets/dropdown.dart';
import 'package:skcj/widgets/reset.dart';
import 'package:skcj/widgets/sType.dart';
import 'package:skcj/widgets/tyleList.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
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
        primarySwatch: Colors.purple,
      ),
      home: const Home(),
    );
  }
}

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
            ElevatedButton(
                child: const Text("CalcJow"),
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (_) => const CalcJow()),
                  );
                }),
            ElevatedButton(
                child: const Text("ACBook"),
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (_) => const ACBook()),
                  );
                }),
          ],
        )));
  }
}

class CalcJow extends StatelessWidget {
  const CalcJow({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("CalcJow"),
      ),
      body: ChangeNotifierProvider(
        create: (BuildContext context) => selectType(),
        child: ListView(
          children: const [
            ResetButton(),
            DropdownType(),
            sType(),
            SSRButtons(),
            SRButtons(),
          ],
        ),
      ),
      drawer: Drawer(
          child: ListView(
        padding: EdgeInsets.zero,
        children: const [
          SizedBox(
            height: 100,
            child: DrawerHeader(
              decoration: BoxDecoration(
                color: Colors.purpleAccent,
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

class ACBook extends StatelessWidget {
  const ACBook({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("ACBook")),
      body: ListView(
        children: const [],
      ),
    );
  }
}
