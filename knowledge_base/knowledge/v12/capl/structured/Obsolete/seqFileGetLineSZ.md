# seqFileGetLineSZ

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long seqFileGetLineSZ(char buffer[], dword bufferSize, long file, long cStyle);
```

## Description

The function reads at most bufferSize-1 characters from the file with the handle file into the array buffer. No additional characters are read after a newline character or after end-of-file.The function retains the newline character. If cStyle is set to 1 the line is terminated by a null character, if cStyle is set to 0 not.

## Return Values

Return value is the number of characters successfully read, or a negative error code, if the operation fails.

## Availability

| Up to Version |
|---|
