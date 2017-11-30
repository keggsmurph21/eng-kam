#!/usr/bin/awk -f
BEGIN {
  RS="$";
  FS="/";
}

{
  nf=split($1,COMPONENTS,"^");
  for(i = 1; i<nf; i++) {
    printf COMPONENTS[i];
  }
  if($2 != "") {
    printf("^%s$",$2);
  }
}
