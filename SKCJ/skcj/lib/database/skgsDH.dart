import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

import '../models/imgInfo.dart';

class skgsDH {
  var _db;

  Future<Database> get database async {
    if (_db != null) {
      return _db;
    } else {
      _db = openDatabase(join(await getDatabasesPath(), "imgInfo.db"),
          onCreate: (db, version) => _createDb(db), version: 1);
      return _db;
    }
  }

  static void _createDb(Database db) {
    db.execute("""
      CREATE TABLE IMGINFO
      (
        ID TEXT PRIMARY KEY
        ,ACTIVE_YN INTEGER
        ,PREV_ID TEXT
        ,NEXT_ID TEXT
        ,RARITY TEXT
        ,TYPE TEXT
      )
""");
  }

  Future<void> insert(imgInfo imgfo) async {
    final db = await database;

    await db.insert("imgInfo", imgfo.toMap(),
        conflictAlgorithm: ConflictAlgorithm.replace);
  }

  Future<List<imgInfo>> selectAll() async {
    final db = await database;

    final List<Map<String, dynamic>> maps = await db.query("imgInfo");
    return List.generate(maps.length, (i) {
      try {
        return imgInfo(
            id: maps[i]["ID"],
            activeYn: maps[i]["ACTIVE_YN"],
            prevId: maps[i]["PREV_ID"],
            nextId: maps[i]["NEXT_ID"],
            rarity: maps[i]["RARITY"],
            type: maps[i]["TYPE"]);
      } catch (e) {
        print(
            "===============================================error=============================================");
        imgInfo asd = imgInfo(
          id: "",
          activeYn: 0,
          prevId: "",
          nextId: "",
          rarity: "",
          type: "",
        );
        return asd;
      }
    });
  }

  Future<dynamic> select(String id) async {
    final db = await database;
    final List<Map<String, dynamic>> maps = (await db.query(
      "imgInfo",
      where: "id = ?",
      whereArgs: [id],
    ));

    return maps.isNotEmpty ? maps : null;
  }

  Future<void> update(imgInfo imgfo) async {
    final db = await database;
    await db.update("imgInfo", imgfo.toMap(),
        where: "id: = ?", whereArgs: [imgfo.id]);
  }

  Future<void> delete(String id) async {
    final db = await database;
    await db.delete(
      "imgInfo",
      where: "id = ?",
      whereArgs: [id],
    );
  }

  Future<void> deleteAll() async {
    final db = await database;
    await db.delete("imgInfo");
  }

  //이미지 추가
  Future<void> newValue() async {
    final db = await database;
    db.rawInsert("""
        INSERT INTO IMGINFO(ID, ACTIVE_YN, PREV_ID, NEXT_ID, RARITY, TYPE)
        VALUES
        ("41000201",0,"start","end","ssr","yellow")
        ,("51000150",0,"start","end","ur","red")
        ,("51000250",0,"start","end","ur","yellow")
        ,("51000000",0,"start","52000000","ur","blue")
        ,("52000000",0,"51000000","end","ur","blue")
        ,("51000100",0,"start","52000100","ur","red")
        ,("52000100",0,"51000100","end","ur","red")
        ,("51000200",0,"start","end","ur","yellow")
        ,("51000001",0,"start","end","ur","blue")
        ,("51000101",0,"start","52000101","ur","red")
        ,("52000101",0,"51000101","end","ur","red")   
        ,("41000000",0,"start","51000003","ssr","blue")
        ,("51000003",0,"41000000","end","ur","blue")
        ,("51000201",0,"start","end","ur","yellow")
        ,("51000151",0,"start","end","ur","red")
        ,("51000202",0,"start","end","ur","yellow")
        ,("51000102",0,"start","end","ur","red")
        ,("51000400",0,"start","end","ur","green")
        ,("51000103",0,"start","end","ur","red")
        ,("51000203",0,"start","52000203","ur","yellow")
        ,("52000203",0,"51000203","end","ur","yellow")
        ,("51000002",0,"start","end","ur","blue")
        ,("51000300",0,"start","end","ur","purple")
        ,("51000104",0,"start","end","ur","red")
        ,("51000004",0,"start","52000004","ur","blue")
        ,("52000004",0,"51000004","62000004","ur","blue")
        ,("62000004",0,"52000004","end","ur","blue")
        ,("51000105",0,"start","52000105","ur","red")
        ,("52000105",0,"51000105","end","ur","red")
        ,("51000301",0,"start","end","ur","purple")
        ,("51000204",0,"start","end","ur","yellow")
        ,("51000205",0,"start","52000205","ur","yellow")
        ,("52000205",0,"51000205","62000205","ur","yellow")
        ,("62000205",0,"52000205","end","ur","yellow")
      """);
  }
}
