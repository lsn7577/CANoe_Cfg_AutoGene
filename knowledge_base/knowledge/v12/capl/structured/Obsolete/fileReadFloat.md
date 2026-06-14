# fileReadFloat

> Category: `Obsolete` | Type: `function`

## Syntax

```c
float fileReadFloat(char section[], char entry[], float def, char ile);
```

## Description

Analogous to fileReadInt for floats.

## Return Values

Number of characters read.

## Example

Result:

len = 5. The array buf is filled with the values 1,2,3,32,100.

```c
File TEST.INI:
[DATA]
FIELD=1,2,3,0x20,100
.. 
int len;
char buf[20];
len = fileReadArray("DATA", "FIELD", buf, elCount(buf), "TEST.INI");
...
```

## Availability

| Up to Version |
|---|
