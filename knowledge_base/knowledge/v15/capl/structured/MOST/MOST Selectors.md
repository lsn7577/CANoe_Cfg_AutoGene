# MOST Selectors

> Category: `MOST` | Type: `notes`

## Description

obsolete!

These selectors are only valid for mostAMSMessage

These selectors are only valid for mostMessage

| Keyword | Description | Range/Valid Values | Access Limitations |
|---|---|---|---|
| ACK | Acknowledgment information | 0...0xFF | read only |
| Arbitration | Bus arbitration bytes | 0...0xFFFFFFFF | read only, Spy |
| DA | Destination address | 0...0xFFFF |  |
| DIR | Direction of transmission | Tx, Rx, TxRequest |  |
| FBlockID | Function block identifier | 0...0xFF |  |
| FunctionID | Function identifier | 0...0xFFF |  |
| ID | Message ID (CANdb lookup key)(see Database Support) | 0...0xFFFFFF | obsolete! |
| InstanceID Most_InstanceID | Instance identifier | 0...0xFF |  |
| SA | Source address | 0...0xFFFF |  |
| OpType | Operation type | 0...0xF |  |
| PIndex | PIndex is a node-based counter (1 byte) which increments per message sent. All low-level retries of a message have the same PIndex. | 0..0xFF | read only, Spy |
| MsgChannel | Transmission channel | 1...16 |  |
| MsgOrigTime | Unsynchronized hardware time stamp(unit: 10 µs) | read only |  |
| Most_IsSpy | Message was received by:1: Spy 0: Node | 0, 1 | read only |
| Most_RType | Message types: When receiving always Normal, other message types are received with mostRawMessage. When applying a mostMessage variable the type can be set to Normal, RemRead, RemWrite, Alloc, Dealloc or GetSource. | 0...0x5 |  |
| Most_State | Status information | 0...0xFF | read only |
| Most_TelID | TelID | 0...0xF |  |
| Time | Synchronized time(unit: 10 µs) | read only |  |

| Keyword | Description | Range/Valid Values | Access Limitations |
|---|---|---|---|
| BYTE(idx) | Provides access to the databytes of the complex MOST message. (BYTE(0) is the first parameter byte) | 0 <= idx <= 65534 0..0xFF |  |
| DLC | Data length code(Number of user data bytes for mostAMSMessages) | 0..65535 |  |

| Keyword | Description | Range/Valid Values | Access Limitations |
|---|---|---|---|
| Arbitration | Bus arbitration bytes | 0...0xFFFFFFFF | read only, Spy |
| BYTE(idx) | Provides access to the databytes of the MOST frame. (BYTE(0) is the first byte behind the TelLen) | 0 ≤ idx ≤ 11 0...0xFF |  |
| CAck | Returns the CRC acknowledge code | 0...0xFF | read only, Spy, MOST150 only 0x00: No Response0x01: CRC error0x04: OK |
| DLC | Data length code (TelLen) | 0...45 |  |
| Most_TelID | TelID | 0...0xF |  |
| MsgCRC | CRC code | 0...0xFFFF | read only, Spy |
| Most_RType | Message types: When receiving always Normal, other message types are received with mostRawMessage. When applying a mostMessage variable the type can be set to Normal, RemRead, RemWrite,Alloc, Dealloc or GetSource. | 0...0x5 | MOST25 only |
| PAck | Returns the preemptive acknowledge code | 0...0xFF | read only, Spy, MOST150 only 0x00: No Response0x01: Buffer full0x04: OK |
| PIndex | PIndex is a node-based counter (1 byte) which increments per message sent. All low-level retries of a message have the same PIndex. | 0..0xFF | read only, Spy, MOST150 only |

| Example Press <Ctrl>+<W> or select Signal insertion from MOST function catalog... from the shortcut menu to open a selection dialog listing all messages and their parameters from the function catalog for selection. This includes all non-nested parameters in the user data with constant width and constant position. In this context, the parameter name is inserted into the program text as a selector. |
|---|

| Keyword | Description | Range/Valid Values | Access Limitations |
|---|---|---|---|
| ACK | Acknowledgment information | 0...0xFF | read only, Spy |
| Arbitration | Bus arbitration bytes | 0...0xFFFFFFFF | read only, Spy |
| BYTE(idx) | Provides the access to the databytes of the MOST frame.0 ≤ idx ≤ 16 | 0...0xFF |  |
| DA | Destination address | 0...0xFFFF |  |
| DIR | Direction of transmission | Tx, Rx, TxRequest |  |
| MsgChannel | Transmission channel | 1...16 |  |
| MsgCRC | CRC code | 0...0xFFFF | read only, Spy |
| MsgOrigTime | Unsynchronized hardware time stamp (unit: 10µs) | read only |  |
| Most_IsSpy | Message was received by:1: Spy 0: Node | 0, 1 | read only |
| Most_RType | Message type(Normal, RemRead, RemWrite,Alloc, Dealloc, GetSource) | 0...5 |  |
| Most_State | Status information | 0...0xFF | read only |
| SA | Source address | 0...0xFFFF |  |
| Time | Synchronized time(unit: 10µs) | read only |  |

| Byte | RemoteReadRType=1 | RemoteWriteRType=2 | AllocRType=3 | DeallocRType=4 | GetSourceRType=5 |
|---|---|---|---|---|---|
| 0 | rsvd | rsvd | rsvd | rsvd | rsvd |
| 1 | MAP | MAP | Request | CL | CL |
| 2 | rsvd | LENGTH | rsvd | rsvd | rsvd |
| 3 | D0 | D0 | Answer1 | Answer1 | rsvd |
| 4 | D1 | D1 | Answer2 | 0x0 | rsvd |
| 5 | D2 | D2 | P0 | rsvd | rsvd |
| 6 | D3 | D3 | P1 | rsvd | NPR |
| 7 | D4 | D4 | P2 | rsvd | rsvd |
| 8 | D5 | D5 | P3 | rsvd | GA |
| 9 | D6 | D6 | P4 | rsvd | NAH |
| 10 | D7 | D7 | P5 | rsvd | NAL |
| 11 | rsvd | rsvd | P6 | rsvd | rsvd |
| 12 | rsvd | rsvd | P7 | rsvd | rsvd |
| 13 ... 16 | rsvd | rsvd | rsvd | rsvd | rsvd |

| Keyword | Description | Range/Valid Values | Access Limitations |
|---|---|---|---|
| Most_Light | Light state of controller | 0, 1 | read only, mostLightLockError |
| Most_Lock | Lock state of controller | 0, 1 | read only, mostLightLockError |
| Most_Error | 0: as long as lock exists 1: as soon as lock does not exists | 0, 1 | read only, mostLightLockError |
| Time | Synchronized time(unit: 10µs) | read only |  |
| MsgOrigTime | Unsynchronized hardware time stamp(unit: 10µs) | read only |  |

| Version 15© Vector Informatik GmbH |
|---|
