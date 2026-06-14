# fileGetString

> Category: `Other` | Type: `function`

## Syntax

```c
long fileGetString (char buff[], long buffsize, dword fileHandle);
```

## Description

The function reads a string from the specified file into the buffer buff.

Characters are read until the end of line is reached or the number of read characters is equal to buffsize -1.The end of line is marked either

The end of line in the buffer is represented by a line feed. See also fileGetStringSZ.

If the end of a line was encountered, the returned string contains a new line character. Else, the next call to fileGetString will start reading in the last line starting with the first character which didn't fit into the buffer on the previous call.

## Return Values

If an error occurs, the return value is 0, else 1.

## Availability

| Since Version |
|---|
