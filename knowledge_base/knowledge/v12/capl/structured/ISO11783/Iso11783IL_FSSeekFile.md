# Iso11783IL_FSSeekFile

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_FSSeekFile( dword fileHandle, dword mode, dword offset );
```

## Description

This function moves the current write/read position of an open file or the read position of directory entries within a directory.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_FSSeekFile( handle, 0, 10 );
```

## Availability

| Since Version |
|---|
