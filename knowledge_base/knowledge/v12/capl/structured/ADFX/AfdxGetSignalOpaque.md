# AfdxGetSignalOpaque

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxGetSignalOpaque( long packet, char signalName[], long bufSize, byte buffer[] ); // form 1
```

## Description

This function copies the content of an opaque data to the specified buffer. There are two different opaque data types available in AFDX:

Since the opaque type is not detectable from the payload stream it must be described explicitly by the network designer.

## Return Values

number of copied data bytes
If this value is > bufSize an error occurred.

## Example

Analyze signals from an incoming AFDX packet using DBC information

```c
on preStart
{
  AfdxRegisterReceiveCallback("OnPacket");
}
void OnPacket( long dir, long line, int64 timestamp, long bag, long afdxFlags, long packet )
{
  long lVal=0; // integer signal
  long eVal=0; // enumeration signal
  long bVal=0; // boolean signal
  double rVal = 0.0; // float signal
  char sVal[16]; // string signal
  byte oVal[16]; // opaque signal
  long len, status, err;
  long msgID;
  char msgName[256];

  // get message ID of this message
  msgID = AfdxGetMessageId( packet );

  // get message name of this message
  err = AfdxGetMessageName( packet, 256, msgName );

  // get signal status
  status = AfdxGetSignalStatus( packet, "VFG_OIL_TEMP_A_34" );

  // get integer signal
  lVal = AfdxGetSignalInt( packet, "VFG_OIL_TEMP_A_34" );

  // get float-signal 2
  rVal = AfdxGetSignalReal( packet, "VFG_OIL_TEMP_AB_32" );

  // get boolean signal 3
  bVal = AfdxGetSignalBool( packet, "VFG_OIL_TEMP_A_ON" );

  // get enumeration signal 4
  eVal = AfdxGetSignalInt( packet, “FLIGHT_GROUND_COND_3" );

  // get string signal 6
  len = AfdxGetSignalString( packet, “TEST_STRING14_CITY", 16, sVal );

  // get opaque signal 7
  len = AfdxGetSignalOpaque( packet, “TEST_OPAQUE14_IDENT", 16, oVal );
}
```

## Availability

| Since Version |
|---|
