# J1939TestReceiveTPCM

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestReceiveTPCM_RTS( pg rxBuffer, dword rxBufferSize, dword da, pg tpcmBuffer, dword tpcmBufferSize, dword timeout, dword options )
```

## Description

With this function receiving of a message with the RTS/CTS transport protocol can be influenced. It can created errors during transmission, i.e. violate time distances or wrong sequence numbers.

First the function J1939TestReceiveTPCM_RTS must be called to wait for the RTS message. The DUT must be triggered to send a RTS/CTS transmission, i.e. with a request.

After that the function J1939TestReceiveTPCM_Data must be used to send a CTS message and wait for a number of data messages (TPDT). The received data is copied to rxBuffer. In the tpcmBuffer, the data for the next CTS message is copied. The function J1939TestReceiveTPCM_Data can be called until the result 2 is returned and the EoMA message was sent.

Before calling J1939TestReceiveTPCM_Data the tpcmBuffer can be modified and i.e. the another sequence number can be requested.

## Example

```c
pg EC1  rxMsg = { DLC=38 };
pg TPCM tpcm;
LONG result;

// send Request for EC1 to DUT, but do not wait for response
J1939TestRequest( EC1, Tester, EMS, 0, 0 );

// wait for RTS from DUT
result = J1939TestReceiveTPCM_RTS( rxMsg, 38, 10, tpcm, 8, 1250, 0x00 );

// send CTS and wait for data, if all packets are receive send EoMA
while (result == 1) {
  result = J1939TestReceiveRTS_Data( rxMsg, 36, 10, tpcm, 8, 5, 16, 250, 0x00 );
}
```

## Availability

| Since Version |
|---|
