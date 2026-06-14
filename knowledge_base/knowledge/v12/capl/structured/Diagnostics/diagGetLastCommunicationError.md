# diagGetLastCommunicationError

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
syntax: long DiagGetLastCommunicationError();
```

## Description

Returns the error code of the last diagnostic request.

## Return Values

Value
Description
-1
0
The response wasn't received in expected time.
1
Time for transmission of the CAN frame on the receiver side expired.
2
Time for transmission of the CAN frame on the sender side expired.
3
Time until reception of the next Flow Control expired.
4
Time until reception of the next Consecutive Frame expired.
5
Not specified communication error.
6
The response wasn't received in the expected extended time.
7
A previously queued request was canceled.
8
Not possible to forward the message to the Bus System Proxy (not defined/open or driver error).
9
The response wasn't received in the expected RC21 completion time.
Value
Description
100
The request to send some data was rejected since another transmission is in progress.
101
A reception was active when FF or SF was received.
102
A negative ACK was received for acknowledged connections.
103
The bus did not confirm transmission of a frame in time.
104
The transmitter did not receive a FC (or AF) in time.
105
The receiver did not receive the next CF in time.
106
The peer rejected the data since it is too long.
107
Peer sent an undefined ACK.
108
A message received is not fit for processing, e.g. a First Frame where a Single Frame would have sufficed.
109
Receiver has sent too many wait frames and must therefore abort the transfer!
110
Receiver has requested the resending of an illegal frame, e.g. the First Frame.
111
ISO: Receiver requested the transfer to be aborted.
200: StartCommunication request wasn't answered by the ECU.
600: The requested function isn't supported.

## Example

```c
testcase TC()
{
  DiagRequest XY_Read req;
  int err;

  TestStep( "Test", "Step");
  DiagSetTarget("ECU");
  DiagSendRequest(req);
  if (0 == TestWaitForDiagResponse( req, 2000))
  {
    err = DiagGetLastCommunicationError();
    write("LastCommunicationError=%d", err);
  }
}
```

## Availability

| Since Version |
|---|
