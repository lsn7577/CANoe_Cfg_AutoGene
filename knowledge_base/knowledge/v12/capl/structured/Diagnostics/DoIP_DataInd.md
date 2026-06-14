# DoIP_DataInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_DataInd( byte buffer[], dword count, dword ecuAddress, dword testerAddress);
```

## Description

This callback is called from the DoIP layer when new data is received.

## Return Values

—

## Example

```c
void DoIP_DataInd( byte buffer[], dword count,
                   dword ecuAddress, dword testerAddress)
{
   // gateway processing here…
   // pass data up to the diagnostics layer
   Diag_DataInd( buffer, count, 0);
}
```

## Availability

| Since Version |
|---|
