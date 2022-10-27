String convType(int type) {
  switch (type) {
    case 0:
      return "blue";
    case 1:
      return "red";
    case 2:
      return "yellow";
    case 3:
      return "purple";
    case 4:
      return "green";
    default:
      return "error";
  }
}

int calcJow(int ssr, int sr) {
  return ssr * 10 + sr * 5;
}
