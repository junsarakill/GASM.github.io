import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/providers/selectType.dart';

import '../main.dart';

class DropdownType extends StatefulWidget {
  const DropdownType({super.key});

  @override
  State<DropdownType> createState() => _DropdownTypeState();
}

class _DropdownTypeState extends State<DropdownType> {
  String dropdownValue = valueList.first;

  @override
  Widget build(BuildContext context) {
    return Container(
        child: Align(
            alignment: Alignment.center,
            child: DropdownButton<String>(
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
              items: valueList.map<DropdownMenuItem<String>>((String value) {
                return DropdownMenuItem<String>(
                    value: value,
                    child: Padding(
                        padding: EdgeInsets.only(left: 10, right: 20),
                        child: Text(
                          value == "0"
                              ? "blue"
                              : value == "1"
                                  ? "red"
                                  : value == "2"
                                      ? "yellow"
                                      : value == "3"
                                          ? "purple"
                                          : value == "4"
                                              ? "green"
                                              : "error",
                          style: TextStyle(fontSize: 20),
                        )));
              }).toList(),
            )));
  }
}
