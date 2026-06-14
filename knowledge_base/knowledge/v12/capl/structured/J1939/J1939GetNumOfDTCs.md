# J1939GetNumOfDTCs

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939GetNumOfDTCs(pg pgWithDTCs, dword spn, byte fmi, byte oc)
```

## Description

Function looks through a J1939 diagnostic message and returns the number of DTC blocks that match the search criteria, i.e. that contains defined SPN/FMI/OC values.

## Example

```c
on pg DM1
{
  int numOfDTCs;

  //Count the number of DTCs with FMI=11
  numOfDTCs = J1939GetNumOfDTCs (this, 0xFFFFFFFF, 11, 0xFFFF);
  if(numOfDTCs > 0)
    WriteEx(-3, 3, "DM1 wiht %d DTC(s) with FMI=11 observed", numOfDTCs);
}
```

## Availability

| Since Version |
|---|
