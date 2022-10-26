import 'package:path/path.dart';
import 'package:skcj/models/jow.dart';
import 'package:sqflite/sqflite.dart';

class DBHelper {
  // ignore: prefer_typing_uninitialized_variables
  var _db;

  Future<Database> get database async {
    if (_db != null) {
      return _db;
    } else {
      _db = openDatabase(join(await getDatabasesPath(), "Jow.db"),
          onCreate: (db, version) => _createDb(db), version: 1);
      return _db;
    }
  }

  static void _createDb(Database db) {
    db.execute("""
      CREATE TABLE JOW
      (
        TYPE INTEGER PRIMARY KEY
        ,SSR INTEGER
        ,SR INTEGER
      )
      """);
  }

  Future<void> insertJow(Jow jow) async {
    final db = await database;

    await db.insert("Jow", jow.toMap(),
        conflictAlgorithm: ConflictAlgorithm.replace);
  }

  Future<List<Jow>> getAllJow() async {
    final db = await database;

    final List<Map<String, dynamic>> maps = await db.query("Jow");
    return List.generate(maps.length, (i) {
      try {
        return Jow(
            type: maps[i]["TYPE"], ssr: maps[i]["SSR"], sr: maps[i]["SR"]);
      } catch (e) {
        print("=======================error================================");
        Jow asd = Jow(type: 0, ssr: 0, sr: 0);
        return asd;
      }
    });
  }

  Future<dynamic> getJow(int type) async {
    final db = await database;

    final List<Map<String, dynamic>> maps = (await db.query(
      "Jow",
      where: "type = ?",
      whereArgs: [type],
    ));

    return maps.isNotEmpty ? maps : null;
  }

  Future<void> updateJow(Jow jow) async {
    final db = await database;

    await db
        .update("Jow", jow.toMap(), where: "type = ?", whereArgs: [jow.type]);
  }

  Future<void> deleteJow(int type) async {
    final db = await database;

    await db.delete(
      "Jow",
      where: "type = ?",
      whereArgs: [type],
    );
  }
}
