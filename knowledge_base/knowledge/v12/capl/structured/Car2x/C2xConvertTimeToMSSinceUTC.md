# C2xConvertTimeToMSSinceUTC

> Category: `Car2x` | Type: `function`

## Syntax

```c
int64 C2xConvertTimeToMSSinceUTC( int64 itsTimestamp, long refTime ); // form 1
```

## Description

This function returns the elapsed milliseconds between a reference time and a time stamp.

As time stamp input either a Unix time stamp in milliseconds (form 1) or a UTC time given with year, month, hour and so on as separate parameters (form 2) can be given. Specific reference times can be set as additional parameter.

The result can be used for the time stamps defined in e.g. a CAM or a DENM.

## Return Values

Time stamp in milliseconds or -1 in case of an error

## Example

```c
int64 itsTimestamp = 0; // original time stamp
int64 itsTS2004 = 0; // converted to 2004 format
word itsTS2004mod16unsigned = 0; // -> mod16 unsigned
long itsTS2004mod32signed = 0; // -> mod32 signed
int64 itsTS2010 = 0; // converted to 2010 format
enum enumRefTime{en2004 = 0, en2010 = 1};

// get times tamp once
itsTimestamp = C2xGetITSTimestamp();

// convert time stamps into needed formats
itsTS2004 = C2xConvertTimeToMSSinceUTC(itsTimestamp, en2004);
itsTS2004mod16unsigned = C2xConvertTimeToMSSinceUTC(itsTimestamp, en2004) & 0xFFFFFFFF;
itsTS2004mod32signed = C2xConvertTimeToMSSinceUTC(itsTimestamp, en2004) & 0x7FFFFFFFFFFFFFFFLL;
itsTS2010 = C2xConvertTimeToMSSinceUTC(itsTimestamp, en2010);
```

## Availability

| Since Version |
|---|
