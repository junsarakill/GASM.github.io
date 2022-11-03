import 'package:flutter/material.dart';
import 'package:skcj/widgets/recGroup/recResult.dart';
import 'package:skcj/widgets/recGroup/typeButtons.dart';

class RecGroup extends StatelessWidget {
  const RecGroup({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("RecGroup")),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Text(
            "Enemy Group",
            style: TextStyle(fontSize: 35),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Column(
                children: const [
                  Text(
                    "Gunner",
                    style: TextStyle(fontSize: 30),
                  ),
                  TypeButtons(index: 0),
                ],
              ),
              const SizedBox(
                width: 30,
              ),
              Column(
                children: const [
                  Text(
                    "Rider",
                    style: TextStyle(fontSize: 30),
                  ),
                  TypeButtons(index: 1),
                ],
              ),
              const SizedBox(
                width: 10,
              ),
              const Text(
                "ATK",
                style: TextStyle(fontSize: 30),
              )
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Column(
                children: const [
                  Text(
                    "Gunner",
                    style: TextStyle(fontSize: 30),
                  ),
                  TypeButtons(index: 2),
                ],
              ),
              const SizedBox(
                width: 30,
              ),
              Column(
                children: const [
                  Text(
                    "Rider",
                    style: TextStyle(fontSize: 30),
                  ),
                  TypeButtons(index: 3),
                ],
              ),
              const SizedBox(
                width: 10,
              ),
              const Text(
                "DEF",
                style: TextStyle(fontSize: 30),
              )
            ],
          ),
          ElevatedButton(
            onPressed: () {
              Navigator.push(context,
                  MaterialPageRoute(builder: (_) => const RecResult()));
            },
            child: const Text("Apply Setting"),
          )
        ],
      ),
    );
  }
}
