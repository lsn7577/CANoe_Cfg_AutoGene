# J1939TestRequest

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestRequest( dword rqPGN, dword reqSA, dword respSA, dword timeout, dword options )
```

## Description

Sends a request from the address reqSA, then wait until the response is received. Within the time interval (timeout) the response or an acknowledgment must be received.

If the requested parameter group is received, the data is copied into the buffer (msgBuffer). The test module can verify the values in this buffer.

If a response is sent with the RTS/CTS transport protocol, with Bit 2 in options sending of CTS and EoMA can be activated

## Example

```c
pg EC1 rxPG;

if (J1939TestRequest( EC1, Tester, EMS, 250, 0x00 ) != 0) {
  testFail( “EC1 not received after request” );
}

if (J1939TestRequest( rxPG, Tester, EMS, 250, 0x00 ) == 0) {
  if (rxPG.AnyValue.phys > 100.0) {
    testStepFail( “EC1.AnyValue hast wrong value” );
  }
}
else {  
  testStepFail( “EC1 not received after request” );
}
```

## Availability

| Since Version |
|---|
