class imgInfo {
  final String id;
  final int activeYn;
  final String prevId;
  final String nextId;
  final String rarity;
  final String type;

  imgInfo(
      {required this.id,
      required this.activeYn,
      required this.prevId,
      required this.nextId,
      required this.rarity,
      required this.type});

  Map<String, dynamic> toMap() {
    return {
      "id": id,
      "activeYn": activeYn,
      "prevId": prevId,
      "nextId": nextId,
      "rarity": rarity,
      "type": type,
    };
  }

  @override
  String toString() {
    return """id: $id,activeYn: $activeYn,prevId: $prevId
            ,nextId: $nextId,rarity: $rarity,type: $type""";
  }
}
