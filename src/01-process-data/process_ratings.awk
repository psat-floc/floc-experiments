# processing ratings to add the year

BEGIN {
  FS=","
};

{
  # dividing by number of seconds per year + 1/4th of number of seconds in a
  # leap year (because a leap year is once in four years)
  printf "%s,%lu\n", $0, (1970 + ($4 / (31536000 + 21600)))
}
