# J1939TestOutputTPCM

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestOutputTPCM_RTS( pg txMsg, dword da, dword maxPacketsPerCTS, pg tpcmBuffer, dword tpcmBufferSize, dword timeout, dword options, [dword optionsArg] )
```

## Description

With this function the transmission of a message with the RTS/CTS transport protocol influenced. It can created errors during transmission, i.e. violate time distances or wrong sequence numbers.

First the transmission must be started with J1939TestOutputTPCM_RTS. Then the function J1939TestOutputTPCM_Data can be called until the result is 2 and the transmission was completed with EoMA.

Before calling J1939TestOutputTPCM_Data the tpcmBuffer can be modified and i.e. a wrong message number can be created.

## Example

```c
pg EC1 txMsg = { DLC=38 };
pg TPCM cts;
LONG result;

// send RTS and wait for first CTS
result = J1939TestOutputTPCM_RTS( txMsg, 234, 16, cts, 8, 1250, 0x00  );

// send data with wrong sequence number
cts.NextPacketNumberToBeSent = 2;
result = J1939TestOutputTPCM_Data( txMsg, 234, 10, cts, 8, 25, 100, 0x00 );

// DUT must send Abort
if (result != 3) {
  TestStepFail( “DUT has not sent Abort” );
}
```

## Availability

| Since Version |
|---|
