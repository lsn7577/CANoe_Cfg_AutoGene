# fileReadArray

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long fileReadArray(char section[], char entry[], char buffer[], long bufferlen, char file[]);
```

## Description

Searches for the variable entry in the section section of the file file. Its contents are interpreted as a list of byte values. The number format is decimal or with the prefix 0x it is hexadecimal. Numbers are separated by spaces, tabs, a comma, semi-colon or slash. The buffer is filled up to a quantity of bufferlen bytes.

## Return Values

Number of characters read.

## Example

Result:

len = 5. The array buf is filled with the values 1,2,3,32,100.

```c
File TEST.INI:
[DATA]
FIELD=1,2,3,0x20,100
...
int len;
char buf[20];
len = fileReadArray("DATA", "FIELD", buf, elCount(buf), "TEST.INI");
...
```

## Availability

| Up to Version |
|---|
