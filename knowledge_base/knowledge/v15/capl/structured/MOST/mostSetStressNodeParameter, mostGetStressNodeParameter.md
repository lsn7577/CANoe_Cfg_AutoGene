# mostSetStressNodeParameter, mostGetStressNodeParameter

> Category: `MOST` | Type: `function`

## Syntax

```c
MOST50 / MOST150: long mostSetStressNodeParameter(long channel, long id, long value);
MOST50 / MOST150: long mostGetStressNodeParameter(long channel, long id);
```

## Description

VN2640:

Additional parameters of the stress generators (mostGenerateBusloadCtrl, mostGenerateBusloadAsync, mostGenerateBusloadEthPkt) can be set with mostSetStressNodeParameter.

OptoLyzer G2 3150o,OptoLyzer MOCCA compact 50e and OptoLyzer MOCCA compact 150c:

The interfaces for MOST150 provides stress functionality through an additional network interface controller (NIC). For a set of stress functions (mostSetRxBufferCtrl, mostSyncAlloc) the NIC is required to be visible in the network (bypass open).

With mostSetStressNodeParameter the MOST node parameters of this additional NIC can be configured.

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface. |
| ID | Description Value Range / Meaning Availability |
| 1 | Node address 0...0xFFFF OptoLyzer G2 3150o OptoLyzer MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 2 | Group address 0x300...0x3FF OptoLyzer G2 3150o OptoLyzer MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 3 | Bypass values:0: open bypass,1: retimed bypass (only for OptoLyzer G2 3150o),2: active bypass OptoLyzer G2 3150o OptoLyzer MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 10 | Control busload destination address 0...0xFFFF VN2640 OptoLyzer G2 3150o OptoLyzer MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 11 | Control busload speed/value range VN2640:Messages per second OptoLyzer G2 3150o, OptoLyzer MOCCAcompact50e:>0: Specifies the delay between two packets (in ms)=0: send as fast as possible VN2640 OptoLyzer G2 3150o OptoLyzer MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 12 | Control busload pattern: specifies what message is sent as busload 0:FBlockID: 0xF1InstID: 0x00FuncID: 0xFFFOpType: 0xC Length 2: (OptoLyzer G2 3150o, OptoLyzer MOCCA compact 150c only)FBlockID: 0x01InstID: 0x00 FuncID: 0x000OpType: 0x1 16: (OptoLyzer G2 3150o, OptoLyzer MOCCA compact 150c only)custom message (to specify custom message use function mostConfigureBusloadCtrl) OptoLyzer G2 3150o OptoLyzer MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 13 | Control busload pattern length: amount of payload sent as busload, applies for pattern 0x00 only 6...51 (OptoLyzer G2 3150o, OptoLyzer MOCCA compact 150c5...17 (OptoLyzer MOCCA compact 50e) OptoLyzer G2 3150o OptoLyzer MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 14 | Control busload burst count: amount of messages sent as busload per (10 ms) cycle. For further information regarding the burst mode please refer to K2L socket protocol specification. 1...65535 OptoLyzer G2 3150o OptoLyzer MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 15 | Control busload send attempts 1...16 VN2640 OptoLyzer G2 3150o OptoLyzer MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 16 | Control busload counter type 0: no counter 1...4: 1-4 byte counter VN2640 OptoLyzer G2 3150o |
| 17 | Control busload counter position: specifies the position of the payload byte that is incremented 6...50 VN2640 OptoLyzer G2 3150o |
| 50 | Data packet channel busload destination address 0...0xFFFF VN2640 OptoLyzer G2 3150o MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 51 | Data packet channel busload speed/value range VN2640:Packets per second OptoLyzer G2 3150o, OptoLyzer MOCCA compact 50e, OptoLyzer MOCCA compact 150c:>0: Specifies the delay between two packets (in ms)=0: send as fast as possible VN2640 OptoLyzer G2 3150o MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 52 | Data packet channel busload pattern: specifies what a message is sent as busload 0: FBlockID: 0xF1InstID: 0x00FuncID: 0xFFFOpType: 0xC Length (2 Byte) OptoLyzer G2 3150o MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 53 | Data packet channel busload pattern length 6...48 (OptoLyzer G2 3150o, OptoLyzer MOCCA compact 150c)6…1014 (OptoLyzer MOCCA compact 50e) OptoLyzer G2 3150o OptoLyzer MOCCA compact 50e OptoLyzer MOCCA compact 150c |
| 55 | Send attempts for data packet bus load 1...16 VN2640 |
| 56 | Data packet bus load counter type 0: no counter1...4: 1-4 byte counter VN2640 |
| 57 | Data packet bus load counter position 0...1523 VN2640 |
| 75 | Send attempts for Ethernet bus load packet 1...16 VN2640 |
| 76 | Ethernet bus load counter type 0: no counter1...4: 1-4 byte counter VN2640 |
| 77 | Ethernet bus load counter position 0...1505 VN2640 |
| value | Parameter value to be set. |

## Example

Example VN2640

See mostConfigureBusloadCtrl

Example OptoLyzer G2 3150o

```c
// configure stress controller as visible network node with logical address 0x123
mostSetStressNodeParameter(1, 1, 0x123); // set node address
mostSetStressNodeParameter(1, 3, 0); // open bypass
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 | 7.2 | — | — | — | —✔ |
| Restricted To | MOST50 (since version 8.0) MOST150 | MOST50 (since version 8.0) MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
