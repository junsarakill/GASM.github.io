import 'dart:io';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:image_picker/image_picker.dart';

class Camera extends StatefulWidget {
  const Camera({super.key});

  @override
  State<StatefulWidget> createState() => _CameraState();
}

class _CameraState extends State<Camera> {
  File? _image;
  final picker = ImagePicker();

  Future getImage(ImageSource imageSource) async {
    final image = await picker.pickImage(source: imageSource);

    setState(() {
      _image = File(image!.path);
    });
  }

  Widget showImage() {
    return Container(
        color: Colors.grey,
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.width,
        child: Center(
            child: _image == null
                ? Text("No image selected.")
                : Image.file(File(_image!.path))));
  }

  @override
  Widget build(BuildContext context) {
    SystemChrome.setPreferredOrientations(
        [DeviceOrientation.portraitUp, DeviceOrientation.portraitDown]);

    return Scaffold(
        backgroundColor: Colors.black,
        body: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            SizedBox(height: 25.0),
            showImage(),
            SizedBox(
              height: 50.0,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: <Widget>[
                FloatingActionButton(
                    child: Icon(Icons.add_a_photo),
                    tooltip: "pick image",
                    onPressed: () {
                      getImage(ImageSource.camera);
                    }),
                FloatingActionButton(
                    child: Icon(Icons.wallpaper),
                    tooltip: "pick image",
                    onPressed: () {
                      getImage(ImageSource.gallery);
                    }),
                FloatingActionButton(
                    child: Icon(Icons.cancel),
                    tooltip: "pick image",
                    onPressed: () {
                      Navigator.pop(context);
                    })
              ],
            )
          ],
        ));
  }
}
