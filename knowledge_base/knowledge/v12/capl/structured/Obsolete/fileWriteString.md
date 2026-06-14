# fileWriteString

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long fileWriteString(char section[], char entry[], char value[], char filename[]);
```

## Description

Opens the file filename, finds the section section and writes the variable entry with the value value. If entry already exists, the old value is overwritten. The functional result is the number of characters written, or 0 for an error.

## Return Values

Number of written characters of 0 if an error has occurred.

## Example

```c
...
if(!fileWriteString("Device","DeviceName","LPT1","test.ini"))
write("file error");
...
This call writes the following entry in the file TEST.INI:
[Device]
DeviceName=LPT1
```

## Availability

| Up to Version |
|---|
