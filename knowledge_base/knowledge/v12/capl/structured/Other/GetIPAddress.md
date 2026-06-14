# GetIPAddress

> Category: `Other` | Type: `function`

## Syntax

```c
long GetIPAddress(char buffer[], dword bufferSize)
```

## Description

Retrieves the default (first) IP address of the computer as a string.

## Return Values

0 if the function completed successfully, else unequal 0.

## Example

```c
char buffer[50];
GetIPAddress(buffer, elcount(buffer));
write("IP Address: %s", buffer);
```

## Availability

| Since Version |
|---|
