# _DoIP_IdentificationRequest

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long _DoIP_IdentificationRequest(long type, BYTE VINorEID[]);
```

## Description

A vehicle simulation has received a Vehicle Identification Request Message. The value returned will determine the reaction of the DoIP.DLL.

Note that requests not targeted at the ECU will be ignored.

## Return Values

-2: Ignore Vehicle Identification Request, i.e. do nothing

## Example

```c
long _DoIP_IdentificationRequest(long type, BYTE VINorEID[])
{
  if( type == 1)
    write( "Received VIR without argument");
  else if( type == 2)
    write( "Received VIR with EID: %02x:%02x:%02x:%02x:%02x:%02x"
    , VINorEID[0], VINorEID[1], VINorEID[2]
    , VINorEID[3], VINorEID[4], VINorEID[5]);
  else if( type == 3)
  {
    char textVIN[17];
    int i;
    for( i = 0; i < elcount(VINorEID); ++i)
      textVIN[i] = VINorEID[i];
    write( "Received VIR with VIN: %s", textVIN);
  }
  // The response message shall be sent after waiting between 100 and 500 ms
  return 100 + random(400);
}
```

## Availability

| Since Version |
|---|
