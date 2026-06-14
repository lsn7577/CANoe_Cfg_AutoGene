# J1939GetFmiFromDTC

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetFmiFromDTC(dword dtc)
```

## Description

Function extracts FMI from DTC.

## Return Values

Extracted FMI.

## Example

```c
on pg DM1
{
  int totalNumOfDTCs, curNumOfDTC;
  dword dtc;
  word fmi, oc;
  dword spn;

  //Iterate over all DTC blocks
  //and extract corresponding SPN, FMI and OC
  totalNumOfDTCs = (this.dlc - 2) / 4;
  for(curNumOfDTC = 0; curNumOfDTC < totalNumOfDTCs; curNumOfDTC++)
  {
    dtc = this.dword(2 + (curNumOfDTC * 4));
    spn = J1939GetSpnFromDTC(dtc);
    fmi = J1939GetFmiFromDTC(dtc);
    oc = J1939GetOcFromDTC(dtc);
    WriteEx(-3, 3, "DM1, DTC Nr. %d: SPN=%d, FMI=%d, OC=%d",
                              curNumOfDTC+1, spn, fmi, oc);
  }
}
```

## Availability

| Since Version |
|---|
