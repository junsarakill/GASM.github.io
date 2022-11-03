import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:skcj/providers/selectType.dart';

class SSRButtons extends StatelessWidget {
  const SSRButtons({super.key});

  @override
  Widget build(BuildContext context) {
    String value = context.watch<selectType>().sValue;
    Map<String, dynamic> jow = context.watch<selectType>().mapJow;

    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        const Image(image: AssetImage("assets/20000000.png")),
        Column(
          children: [
            SizedBox(
              child: Text(
                jow["SSR"].toString(),
                style: const TextStyle(fontSize: 20),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                    onPressed: () {
                      context.read<selectType>().removeSSRJow(int.parse(value));
                    },
                    child: const Icon(Icons.remove)),
                ElevatedButton(
                    onPressed: () {
                      context.read<selectType>().addSSRJow(int.parse(value));
                    },
                    child: const Icon(Icons.add)),
              ],
            )
          ],
        )
      ],
    );
  }
}

class SRButtons extends StatelessWidget {
  const SRButtons({super.key});

  @override
  Widget build(BuildContext context) {
    String value = context.watch<selectType>().sValue;
    Map<String, dynamic> jow = context.watch<selectType>().mapJow;

    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        const Image(image: AssetImage("assets/10000000.png")),
        Column(
          children: [
            SizedBox(
              child: Text(
                jow["SR"].toString(),
                style: const TextStyle(fontSize: 20),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                    onPressed: () {
                      context.read<selectType>().removeSRJow(int.parse(value));
                    },
                    child: const Icon(Icons.remove)),
                ElevatedButton(
                    onPressed: () {
                      context.read<selectType>().addSRJow(int.parse(value));
                    },
                    child: const Icon(Icons.add)),
              ],
            )
          ],
        )
      ],
    );
  }
}
