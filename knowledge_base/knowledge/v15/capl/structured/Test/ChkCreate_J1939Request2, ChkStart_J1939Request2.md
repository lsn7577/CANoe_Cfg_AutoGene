# ChkCreate_J1939Request2, ChkStart_J1939Request2

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_J1939Request2(Node requestNode, Node responseNode, Message requestedMessage, dword expected, dword options, dword timeout, dword requestInhibitTime, dword retryInhibitTime, char[] callback1);
dword ChkCreate_ J1939Request2(Node responseNode, Message requestedMessage, dword expected, dword options, dword timeout, dword requestInhibitTime, dword retryInhibitTime, char[] callback1);
dword ChkCreate_ J1939Request2(dword requestSourceAddress, dword responseSourceAddress, Message requestedMessage, dword expected, dword options, dword timeout, dword requestInhibitTime, dword retryInhibitTime, char[] callback1);
dword ChkCreate_ J1939Request2(dword requestSourceAddress, dword responseSourceAddress, dword requestedPGN, dword expected, dword options, dword timeout, dword requestInhibitTime, dword retryInhibitTime, char[] callback1);
dword ChkCreate_J1939Request2(Node responseNode, dword expected, dword options, dword timeout, dword requestInhibitTime, dword retryInhibitTime, char[] callback1);
dword ChkStart_J1939Request2(Node requestNode , Node responseNode, Message requestedMessage, dword expected, dword options, dword timeout, dword requestInhibitTime, dword retryInhibitTime, char[] callback1);
dword ChkStart_J1939Request2(Node responseNode, Message requestedMessage, dword expected, dword options, dword timeout, dword requestInhibitTime, dword retryInhibitTime, char[] callback1);
dword ChkStart_J1939Request2(dword requestSourceAddress, dword responseSourceAddress, Message requestedMessage, dword expected, dword options, dword timeout, dword requestInhibitTime, dword retryInhibitTime, char[] callback1);
dword ChkStart_J1939Request2(dword requestSourceAddress, dword responseSourceAddress, dword requestedPGN, dword expected, dword options, dword timeout, dword requestInhibitTime, dword retryInhibitTime, char[] callback1);
dword ChkStart_J1939Request2(Node responseNode, dword expected, dword options, dword timeout, dword requestInhibitTime, dword retryInhibitTime, char[] callback1);
```

## Description

Observes the J1939 Request2 (C900h). It is possible to observe all Request2 messages or only the Request2 message for a specific send node.

## Parameters

| Name | Description |
|---|---|
| requestNode | Requesting node from database. |
| responseNode | Responding node from database. |
| requestSourceAddress | Address of the ECU which sends the request. Possible values: 0 – 253: Observe request node with this address 254, -1 (or 0xFFFFFFFF):: Observe all request nodes |
| responseSourceAddress | Address of the ECU which sends the response. Possible values: 0 – 253: Observe response node with this address 254, -1 (or 0xFFFFFFFF): Observe all response nodes |
| requestedMessage | Requested message from database (the parameter group number of this message is used). |
| requestedPGN | Parameter group number of the requested message. |
| expected | One or more expected results bit 1: the requested parameter group bit 2: the negative Acknowledgment message bit 3: the positive Acknowledgment message bit 4: the access denied Acknowledgment message bit 5: the address busy Acknowledgment message bit 6: timeout, no answer expected. You can combine the expected parameters by bitwise operations. |
| options | bit 1: allow request if request is pending bit 2: allow Acknowledgment message sent to specific destination address (required by ISO11783) You can combine the options parameters by bitwise operations. |
| timeout | Maximum allowed time between request and response (default 1250ms) [ms] |
| requestInhibitTime | Time, during the last received message, when no request for this message is allowed (default 50ms) [ms]. |
| retryInhibitTime | Time after the last timeout of the second retry (third request) until the same request can be sent again without being recognized as invalid third (default 0ms) [ms]. |
| callback1 | This parameter is optional. Name of the callback which is called when the check fails. Signature: void Callback( dword checkId ) |
| callback2 | This parameter is optional. Name of the callback which is called when the check fails. Signature: void Callback( TestCheck check ) |

## Example

```c
TestCheck check;
  // checks the if a response from N2 is received after a J1939 Request2 from node N1
  checkId = ChkStart_J1939Request2(N1, N2, GBSD, 0x01, 0, 1250, 50, 0);
  TestAddCondition(checkId);

  // sequence of different actions and waiting conditions
  TestWaitForTimeout(1000);
  TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 | 13.0 | — | — | 2.0 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
