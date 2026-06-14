# fileWriteInt

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long fileWriteInt(char section[], char entry[], long def, char file[]);
```

## Description

Analogous to fileWriteString, but writes a long variable to the file instead of a text.

## Return Values

0 if an error has occurred else 1

## Example

```c
...
if(!fileWriteInt("DeviceData","DeviceAddr",2, "TEST.INI"))
write("file error");
...
This call writes the following entry in the file TEST.INI:
[DeviceData]
DeviceAddr=2
```

## Availability

| Up to Version |
|---|
