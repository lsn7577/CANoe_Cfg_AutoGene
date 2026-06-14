# seqFileGetLine

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long seqFileGetLine(char buffer[], dword bufferSize, long file);
```

## Description

The function reads at most bufferSize-1 characters from the file with the handle file into the array buffer. No additional characters are read after a newline character or after end-of-file.

The function retains the newline character, but the line is not zero-terminated.

## Return Values

Return value is the number of characters successfully read, or a negative error code, if the operation fails.

## Availability

| Up to Version |
|---|
