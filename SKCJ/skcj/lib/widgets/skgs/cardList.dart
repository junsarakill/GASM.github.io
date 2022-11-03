import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/database/skgsDH.dart';

import '../../providers/filter.dart';

class CardList extends StatelessWidget {
  const CardList({super.key});

  @override
  Widget build(BuildContext context) {
    skgsDH skgs = skgsDH();
    skgs.selectAll().then((value) {
      context.read<filter>().setCardList(value);
    });
    List<String> cardList = context.watch<filter>().cList;
    return Column(
      children: [
        const Image(image: AssetImage("assets/41000201.png")),
        for (int i = 0; i < cardList.length; i++)
          Text(
            cardList[i],
            style: TextStyle(fontSize: 30),
          )
      ],
    );
  }
}
