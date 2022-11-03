import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/database/skgsDH.dart';

import '../../providers/filter.dart';
import 'cardList.dart';

class SKGS extends StatelessWidget {
  const SKGS({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("SKGS"),
      ),
      body: ChangeNotifierProvider(
          create: (BuildContext context) => filter(),
          child: ListView(
            children: [
              const CardList(),
            ],
          )),
      drawer: Drawer(
          child: ListView(
        padding: EdgeInsets.zero,
        children: [
          const SizedBox(
            height: 100,
            child: DrawerHeader(
                decoration: BoxDecoration(
                  color: Colors.redAccent,
                ),
                child: Text(
                  "All Type",
                  style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      color: Colors.white),
                )),
          ),
          //필터 내용
          OutlinedButton(
              child: const Text("New"),
              onPressed: () {
                skgsDH skgs = skgsDH();
                skgs.newValue();
              }),
          OutlinedButton(
              child: const Text("select"),
              onPressed: () {
                skgsDH skgs = skgsDH();
                skgs.selectAll().then((value) {
                  print(value);
                });
              }),
          OutlinedButton(
              child: const Text("delete"),
              onPressed: () {
                skgsDH skgs = skgsDH();
                skgs.deleteAll();
              }),
        ],
      )),
    );
  }
}
