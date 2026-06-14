# MediaWrite

> Category: `Media` | Type: `function`

## Syntax

```c
long MediaWrite(dword sinkWriterHandle, dword streamIndex, int64 timestamp, byte buffer[], dword length);
```

## Description

Delivers sample data to the sink writer. The buffer can be reused immediately after the function returns.

## Return Values

0: The function succeeded

## Availability

| Since Version |
|---|
