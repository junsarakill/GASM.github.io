import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/providers/dwSelectType.dart';
import 'package:skcj/widgets/typeButtons.dart';

class RecResult extends StatelessWidget {
  const RecResult({super.key});

  @override
  Widget build(BuildContext context) {
    context.read<dwSelectType>().setResult();
    List<int> result = context.watch<dwSelectType>().rValue;
    //selectedvalue 리스트 가져와서 result: 에 넣기
    return Scaffold(
      appBar: AppBar(title: const Text("RecGroup")),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const Text(
            "Recommend",
            style: TextStyle(fontSize: 35),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Column(
                children: [
                  const Text(
                    "Gunner",
                    style: TextStyle(fontSize: 30),
                  ),
                  TypeButtons(index: 0, value: result[0]),
                ],
              ),
              const SizedBox(
                width: 30,
              ),
              Column(
                children: [
                  const Text(
                    "Rider",
                    style: TextStyle(fontSize: 30),
                  ),
                  TypeButtons(index: 1, value: result[1]),
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
                children: [
                  const Text(
                    "Gunner",
                    style: TextStyle(fontSize: 30),
                  ),
                  TypeButtons(index: 2, value: result[2]),
                ],
              ),
              const SizedBox(
                width: 30,
              ),
              Column(
                children: [
                  const Text(
                    "Rider",
                    style: TextStyle(fontSize: 30),
                  ),
                  TypeButtons(index: 3, value: result[3]),
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
        ],
      ),
    );
  }
}
