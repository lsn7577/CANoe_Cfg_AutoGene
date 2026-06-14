# mostStringToAscii

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostStringToAscii(byte sourceData[], long sourceDatalen, char buffer[], long buffersize)
```

## Description

Convert MOST string to ASCII string. Unsupported characters in the input data are ignored.

Supported encodings:

0x00

Unicode, UTF16

0x01

ISO 8859/15 8 bit

0x02

Unicode, UTF8

## Return Values

>=0: number of converted characters

## Example

Output: ASCII: abc

```c
byte data[9] = {0x00,0x00,0x61,0x00,0x62,0x00,0x63,0x00,0x00);
char buffer[200];
if(0 < mostStringToAscii(data, elcount(data), buffer, elcount(buffer)))
  write("ASCII: %s", buffer);
```

## Availability

| Since Version |
|---|
