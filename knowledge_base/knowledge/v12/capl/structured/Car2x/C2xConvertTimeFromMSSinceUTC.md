# C2xConvertTimeFromMSSinceUTC

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xConvertTimeFromMSSinceUTC( int64 milliseconds, long refTime, long buffersize, char buffer[] ); // form 1
```

## Description

This function converts a time stamp in milliseconds since a reference time into a UTC time stamp in string format (form 1) or as long array with separate values for year, month, day and so on (form 2).

## Return Values

0 if success

## Example

```c
int64 itsTS2004 = 300000000000LL; // original time stamp in 2004 format
enum enumRefTime{en2004 = 0, en2010 = 1};
char buffer[40] ;
long utcTime[9] ;

if (C2xConvertTimeFromMSSinceUTC(itsTS2004, en2004, elcount(buffer), buffer) == 0)
{
  // output: Time stamp 2013-07-04T05:19:57.000 UTC
  write("Time stamp %s", buffer);
}

if (C2xConvertTimeFromMSSinceUTC(itsTS2004, en2004, elcount(utcTime), utcTime) == 0)
{
  write("Time stamp %d-%02d-%02dT%02d:%02d:%02d.%03d UTC", 1900+utcTime[6], utcTime[5]+1, utcTime[4], utcTime[3], utcTime[2], utcTime[1], utcTime[0]);
}
```

## Availability

| Since Version |
|---|
