# DoIP_DataCon

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_DataCon( dword count);
```

## Description

This callback is called from the DoIP layer when data was sent.

## Return Values

—

## Example

```c
void DoIP_DataCon( dword count)
{
   // pass up to the diagnostics layer
   Diag_DataCon( count);
}
```

## Availability

| Since Version |
|---|
