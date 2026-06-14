# seqFileGetBlock

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long seqFileGetBlock(char buffer[], dword bufferSize, long file);
```

## Description

The function reads at most bufferSize characters from the file specified by handle file into the array buffer. The file position indicator is advanced by the number of characters successfully read. It is indeterminate after an error.

## Return Values

The return value is the number of characters successfully read, which may be less than bufferSize, if an error or end-of-file is encountered.

## Availability

| Up to Version |
|---|
