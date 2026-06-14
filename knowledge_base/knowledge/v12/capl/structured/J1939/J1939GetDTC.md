# J1939GetDTC

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939GetDTC(pg pgWithDTC, dword spn, byte fmi, byte oc, dword &dtcValue)
```

## Description

Function looks through a J1939 diagnostic message and returns the first DTC block that matches the search criteria, i.e. that contains defined SPN/FMI/OC values.

## Example

```c
on pg DM1
{
  int posOfDTC;
  dword foundDTC;
  word fmi, oc;
  dword spn;

  //Look for the DTC with SPN=67890
  posOfDTC = J1939GetDTC(this, 67890, 0xFFFF, 0xFFFF, foundDTC);
  if(posOfDTC > 0)
  {
    fmi = J1939GetFmiFromDTC(foundDTC);
    oc = J1939GetOcFromDTC(foundDTC);
    WriteEx(-3, 3, "DM1 with DTC (SPN=67890) observed: FMI=%d, OC=%d", fmi, oc);
  
}
  //Look for the DTC with SPN=123 and OC=5
  posOfDTC = J1939GetDTC(this, 123, 0xFFFF, 5, foundDTC);
  if(posOfDTC > 0)
  {
    fmi = J1939GetFmiFromDTC(foundDTC);
    WriteEx(-3, 3, "DM1 with DTC (SPN=123, OC=5) observed: FMI=%d", fmi);
  }
}
```

## Availability

| Since Version |
|---|
