# fileReadString

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long fileReadString(char section[], char entry[], char def[], char buffer[], long bufferlen, char filename[]);
```

## Description

Searches for the variable entry in the section section of the file filename. Its content (value) is written to the buffer buffer. Its length must be passed correctly to bufferlen. If the file or entry is not found, the default value def is copied to buffer.

## Return Values

Number of bytes read

## Example

Result:

buf is filled with the characters "Feld".

```c
ile TEST.INI:
[DATA]
NAME=Feld
ADDR=200
FIELD=1,2,3,0x20,100
...
int len;
char buf[20];
fileReadString("DATA", "NAME", "DefaultString", buf, elCount(buf), "TEST.INI");
...
```

## Availability

| Up to Version |
|---|
