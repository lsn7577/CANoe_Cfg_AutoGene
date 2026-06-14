# FSIL_OnNumberOfOpenFilesChanged

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void FSIL_OnNumberOfOpenFilesChanged( dword clientAddress, dword numberOfOpenFiles)
```

## Description

Is called from the FS IL if a client has opened or closed a file or directory.

## Return Values

—

## Example

```c
void FSIL_OnNumberOfOpenFilesChanged( dword clientAddress, dword numberOfOpenFiles)
{
  write("Client with address %u has %u open files", clientAddress, numberOfOpenFiles);
}
```

## Availability

| Since Version |
|---|
