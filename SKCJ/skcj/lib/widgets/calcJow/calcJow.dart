import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/widgets/calcJow/reset.dart';
import 'package:skcj/widgets/calcJow/sType.dart';
import 'package:skcj/widgets/calcJow/typeList.dart';
import '../../providers/selectType.dart';
import 'buttons.dart';
import 'dropdown.dart';

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
