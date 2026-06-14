# A664GetFunctionalStatus

> Category: `ADFX` | Type: `function`

## Syntax

```c
BYTE A664GetFunctionalStatus (PDU aPDU)
```

## Description

This function returns the Functional Status (FS) of a AFDX-PDU (FDS) if the FDS-mode is used. In frameMode use FS-signals instead.

Note: This function is only available in PDU-mode.

## Example

Examine the Functional Status of any received FDS:

```c
on PDU * {
{
  int fs = 0;
  fs = a664GetFunctionalStatus(this);
  writeEx(-3,1, "FS of received PDU %s: %d", this.name, fs);
}
```

## Availability

| Since Version |
|---|
