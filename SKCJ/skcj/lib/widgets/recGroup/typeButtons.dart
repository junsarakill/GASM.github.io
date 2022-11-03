import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';
import 'package:skcj/providers/dwSelectType.dart';

class TypeButtons extends StatefulWidget {
  final int index;
  final int value;

  const TypeButtons({super.key, this.index = 0, this.value = 0});

  @override
  // ignore: no_logic_in_create_state
  State<StatefulWidget> createState() => _TypeButtons(index, value);
}

class _TypeButtons extends State<TypeButtons> {
  _TypeButtons(this.index, this.value);

  final int index;
  int value;

  @override
  Widget build(BuildContext context) {
    SystemChrome.setPreferredOrientations(
        [DeviceOrientation.landscapeLeft, DeviceOrientation.landscapeRight]);
    return Row(
      children: <Widget>[
        GestureDetector(
            onTap: () => {
                  setState(() => value = 0),
                  context.read<dwSelectType>().setter(index, value),
                },
            child: SizedBox(
                height: 56,
                width: 56,
                child: ColorFiltered(
                  colorFilter: value == 0
                      ? const ColorFilter.mode(Colors.white, BlendMode.modulate)
                      : const ColorFilter.mode(Colors.grey, BlendMode.modulate),
                  child: const Image(image: AssetImage("assets/blue.png")),
                ))),
        GestureDetector(
            onTap: () => {
                  setState(() => value = 1),
                  context.read<dwSelectType>().setter(index, value),
                },
            child: SizedBox(
                height: 56,
                width: 56,
                child: ColorFiltered(
                  colorFilter: value == 1
                      ? const ColorFilter.mode(Colors.white, BlendMode.modulate)
                      : const ColorFilter.mode(Colors.grey, BlendMode.modulate),
                  child: const Image(image: AssetImage("assets/red.png")),
                ))),
        GestureDetector(
            onTap: () => {
                  setState(() => value = 2),
                  context.read<dwSelectType>().setter(index, value),
                },
            child: SizedBox(
                height: 56,
                width: 56,
                child: ColorFiltered(
                  colorFilter: value == 2
                      ? const ColorFilter.mode(Colors.white, BlendMode.modulate)
                      : const ColorFilter.mode(Colors.grey, BlendMode.modulate),
                  child: const Image(image: AssetImage("assets/yellow.png")),
                ))),
        GestureDetector(
            onTap: () => {
                  setState(() => value = 3),
                  context.read<dwSelectType>().setter(index, value),
                },
            child: SizedBox(
                height: 56,
                width: 56,
                child: ColorFiltered(
                  colorFilter: value == 3
                      ? const ColorFilter.mode(Colors.white, BlendMode.modulate)
                      : const ColorFilter.mode(Colors.grey, BlendMode.modulate),
                  child: const Image(image: AssetImage("assets/purple.png")),
                ))),
        GestureDetector(
            onTap: () => {
                  setState(() => value = 4),
                  context.read<dwSelectType>().setter(index, value),
                },
            child: SizedBox(
                height: 56,
                width: 56,
                child: ColorFiltered(
                  colorFilter: value == 4
                      ? const ColorFilter.mode(Colors.white, BlendMode.modulate)
                      : const ColorFilter.mode(Colors.grey, BlendMode.modulate),
                  child: const Image(image: AssetImage("assets/green.png")),
                ))),
      ],
    );
  }
}
