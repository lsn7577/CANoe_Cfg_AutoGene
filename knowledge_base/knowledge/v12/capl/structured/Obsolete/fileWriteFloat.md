# fileWriteFloat

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long fileWriteFloat(char section[], char entry[], float def, char file[]);
```

## Description

Analogous to fileWriteInt, but writes a float variable to the file instead of a text.

## Return Values

0 if an error has occurred else 1

## Example

```c
...
if(!fileWriteInt("DeviceData","DeviceAddr",2.2, "TEST.INI"))
write("file error");
...
This call writes the following entry in the file TEST.INI:
[DeviceData]
DeviceAddr=2.2
```

## Availability

| Up to Version |
|---|
