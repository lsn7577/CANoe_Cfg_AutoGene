# fileReadInt

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long fileReadInt(char section[], char entry[], long def, char file[]);
```

## Description

Searches for the variable entry in the section section of the file filename. If its value is a number, this number is returned as the functional result. If the file or entry is not found, or if entry does not contain a valid number, the default value def is returned as the functional result.

## Return Values

Integer read

## Example

Result:

The value 200 is assigned to the variable myAddress. If the entry ADDR does not exist in the file TEST.INI the default value 0 is assigned to myAddress.

```c
File TEST.INI:
[DATA]
NAME=Feld
ADDR=200
FIELD=1,2,3,0x20,100
...
myAddress=fileReadInt("DATA", "ADDR", 0, "TEST.INI");
...
```

## Availability

| Up to Version |
|---|
