# a429SetGap

> Category: `A429` | Type: `function`

## Syntax

```c
dword a429SetGap( a429word myA429word, dword gapValue );
```

## Description

This function sets the selector gap of an ARINC word. The value is given in nanoseconds. You have to consider the bit rate on the corresponding channel. If the bit rate is high speed a value of 40000 (40 µs) specifies the standard gap of 4 bit times (as defined in /1/). For low speed at 12500 kBit/s a value of 320000 (320 µs) is needed.

Note: This modifies the ARINC word attributes only. For transmission call the function output.

## Availability

| Since Version |
|---|
