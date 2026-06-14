# FSIL_OnCurrentDirectoryChanged

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void FSIL_OnCurrentDirectoryChanged( dword clientAddress, char currentDirectory[]);
```

## Description

Is called from the FS IL if a client has changed its current directory.

## Return Values

—

## Example

```c
void FSIL_OnCurrentDirectoryChanged( dword clientAddress, char currentDirectory[])
{
  write("Client with address %u has changed it current directory to '%s'", clientAddress, currentDirectory);
}
```

## Availability

| Since Version |
|---|
