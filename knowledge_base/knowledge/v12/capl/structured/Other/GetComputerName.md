# GetComputerName

> Category: `Other` | Type: `function`

## Syntax

```c
long GetComputerName(char buffer[], dword bufferSize)
```

## Description

Retrieves the fully qualified name of the computer.

## Return Values

0 if the function completed successfully, else unequal 0.

## Example

```c
char buffer[50];
GetComputerName(buffer, elcount(buffer));
write("Computer name: %s", buffer);
```

## Availability

| Since Version |
|---|
