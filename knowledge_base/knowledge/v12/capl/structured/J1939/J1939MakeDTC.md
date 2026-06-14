# J1939MakeDTC

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939MakeDTC(dword spn, byte fmi, byte oc, dword &dtcValue)
```

## Description

Function generates a DTC from the defined SPN, FMI and OC.

## Example

```c
//Fill DM1 with two DTCs and send it

  pg DM1 myDM1 = {DLC=10, SA=1};
  dword dtc;

  //Activate Protect Lamp (permanent lighting)
  myDM1.word(0) = 0xFF01;

  //Make first DTC (SPN=67890, FMI=16, OC=101)
  J1939MakeDTC(67890, 16, 101, dtc);
  myDM1.dword(2) = dtc;

  //Make second DTC (SPN=123, FMI=11, OC=5)
  J1939MakeDTC(123, 11, 5, dtc);
  myDM1.dword(6) = dtc;

  //Send DM1 message
  output(myDM1);
```

## Availability

| Since Version |
|---|
