# coTfsODChkStdEntries

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsODChkStdEntries( void );
```

## Description

The function executes a standard test of the object dictionary.

For a description of the object check, see coTfsODChkSingleEntry.

## Return Values

Error code

## Example

```c
if (coTfsODChkStdEntries() != 1) {
  write("std object dictionary check failed");
} 
else {
  write("std object dictionary check passed");
}
```
