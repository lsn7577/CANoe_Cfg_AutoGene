# AfdxGetSignalInt

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetSignalInt( long packet, char* signalName ); // form 1
```

## Description

This function returns the value of a 32-bit integer signal.

## Return Values

signal value (call AfdxGetLastErrror() to check for errors in the call)

## Example

Analyze signals from an incoming AFDX packet with two signals without DBC

Analyze signals from an incoming AFDX packet with two signals with DBC

```c
on preStart
{
 AfdxRegisterReceiveCallback("OnPacket");
}
void OnPacket( long dir, long line, int64 timestamp, long bag, long afdxFlags, long packet )
{
  long temp1, temp2;
  byte status1, status2;

  // get status bytes first to see if signals are valid
  status1 = AfdxGetSignalStatus( packet, 4 );
  status2 = AfdxGetSignalStatus( packet, 5 );
  if (status1 == 3 && status2 == 3 )
  {
    // get oil temperature
    temp1 = AfdxGetSignalInt( packet, 8 ); // offset=8
    // get oil temp 2
    temp2 = AfdxGetSignalInt( packet, 12 );  // offset=12
  // do something with this values
  }
}
on preStart
{
  AfdxRegisterReceiveCallback("OnPacket");
}
void OnPacket( long dir, long line, int64 timestamp, long bag, long afdxFlags, long packet )
{
  long temp1, temp2;
  byte status1, status2;

  // get status bytes first to see if signals are valid
  status1 = AfdxGetSignalStatus( packet, “IOM_TEST_VFG_OIL_TEMP_A_2_21” );
  status2 = AfdxGetSignalStatus( packet, “IOM_TEST_VFG_OIL_TEMP_A_2_22” );

  if (status1 == 3 && status2 == 3 )
  {
    // get oil temperature
    temp1 = AfdxGetSignalInt( packet, “IOM_TEST_VFG_OIL_TEMP_A_2_21” ); // offset=8
    // get oil temp 2
    temp2 = AfdxGetSignalInt( packet, “IOM_TEST_VFG_OIL_TEMP_A_2_21” ); // offset=12
    // do something with this values
  }
}
```

## Availability

| Since Version |
|---|
