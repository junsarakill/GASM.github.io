class JowInfo {
  final int type;
  final int ssr;
  final int sr;

  JowInfo({
    required this.type,
    required this.ssr,
    required this.sr,
  });

  Map<String, dynamic> toMap() {
    return {
      'type': type,
      'ssr': ssr,
      'sr': sr,
    };
  }

  @override
  String toString() {
    return 'JowInfo{type: $type, ssr: $ssr, sr: $sr}';
  }
}
