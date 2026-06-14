# CAN Message Selectors

> Category: `CAN` | Type: `notes`

## Description

You can access control information of the CAN message object using the following selectors:

Transmit and receive flags. If more than one flag is set, then their values will be logically ORed.

GetPDU(n, P)

long

read only

IsContainer()

PDUCount()

PDUOffset(n)

To achieve independence from the actual coding of DIR and RTR the following symbolic constants can be used:

Defining Parameter Groups

| Keyword | Description | Type | Access Limitation | CAPL-on-Board |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Identification |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| CAN | Transmission channel or channel through which the frame has been received. Value range: 1..32 | word | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| MsgChannel | Transmission channel or channel through which the frame has been received. Value range: 1..32 | word | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ID | Message identifier | dword | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| name | (unqualified) symbolic name of the message from the database (since version 7.2) | char[] | read only | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DIR | Direction of transmission, event classification; possible values: Rx, Tx, TXREQUEST | byte | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| RTR | Remote Transmission Request; possible values: 0 (no RTR), 1 (RTR) | byte | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TYPE | Combination of DIR and RTR for an efficient evaluation. (TYPE = (RTR << 8) \| DIR ) | word | — | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DLC | The data field length of a message is coded with the DLC (Data Length Code). Value range: 0..15 Data field length:CAN messages: 0..8 CAN FD messages: 0..64 J1939 parameter groups: 0..1785 | byte | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DataLength | Data length in bytes. | byte | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Message Times and Lengths |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TIME_NS | Point in time, units: nanoseconds | int64 | read only | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TIME | Point in time, units: 10 microseconds This selector is not available when executing CAPL code directly on hardware interfaces. Therefore you must use Time_ns. | dword | — | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SOF | Start-of-Frame time stamp in ns. For some CAN hardware this value is not available (value 0). In such a case a software calculation is required (see CANoe Options dialog). | int64 | read only | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FrameLen | Frame duration in ns. Note, that the frame duration always includes three bits of the Interframe Space.For some CAN hardware this value is not available (value 0). In such a case a software calculation is required (see CANoe Options dialog). | dword | read only | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bitcount | Number of bits of a CAN/CAN FD message (incl. IFS bits). For some CAN hardware this value is not available (value 0). In such a case a software calculation is required (see CANoe Options dialog). | word | — | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Data Access |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Byte(x) | Message data byte (unsigned 8 bit); possible values for xx sets the datafield byte for the beginning of the value.*: 0…63 | byte | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Word(x) | Message data word (unsigned 16 bit); possible values for xx sets the datafield byte for the beginning of the value.*: 0…62 The index is byte-oriented; for example, word(1) references to the data beginning at byte 1 and consists of byte 1…2 (16 bit). | word | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DWord(x) | Message data word (unsigned 32 bit); possible values for xx sets the datafield byte for the beginning of the value.*: 0…60 The index is byte-oriented; for example, dword(1) references to the data beginning at byte 1 and consists of byte 1…4 (32 bit). | dword | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| QWord(x) | Message data word (unsigned 64 bit); possible values for xx sets the datafield byte for the beginning of the value.*: 0…56 | qword | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| char(x) | Message data byte (signed 8 bit); possible values for xx sets the datafield byte for the beginning of the value.*: 0…63 | char | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| int(x) | Message data word (signed 16 bit); possible values for xx sets the datafield byte for the beginning of the value.*: 0…62 The index is byte-oriented; for example, int(1) references to the data beginning at byte 1 and consists of byte 1…2 (16 bit). | int | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| long(x) | Message data word (signed 32 bit); possible values for xx sets the datafield byte for the beginning of the value.*: 0…60 The index is byte-oriented; for example, long(1) references to the data beginning at byte 1 and consists of byte 1…4 (32 bit). | long | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| int64(x) | Message data word (signed 64 bit); possible values for xx sets the datafield byte for the beginning of the value.*: 0…56 | int64 | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| float(x) | Message data interpreted as IEEE float (32 bit); possible values for xx sets the datafield byte for the beginning of the value.*: 0…60 | doubleIn CAPL, both float and double are the same data type (64bit IEEE double)* | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| double(x) | Message data interpreted as IEEE double (64 bit); possible values for xx sets the datafield byte for the beginning of the value.*: 0…56 | doubleIn CAPL, both float and double are the same data type (64bit IEEE double)* | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Flags |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| MsgFlags | Transmit and receive flags. If more than one flag is set, then their values will be logically ORed. 0x02 The transmit buffer will be emptied before transmitting the message - the message is not blocked by other messages. 0x04 The NERR flag of the CAN transceiver was active at message reception (system is in single wire mode) 0x08 The message will be sent or was received in high voltage mode 0x10 Remote Frame 0x40 Transmit Acknowledge (equal to DIR==Tx) 0x80 Transmit Request (equal to DIR==TXREQUEST) All others Reserved | 0x02 | The transmit buffer will be emptied before transmitting the message - the message is not blocked by other messages. | 0x04 | The NERR flag of the CAN transceiver was active at message reception (system is in single wire mode) | 0x08 | The message will be sent or was received in high voltage mode | 0x10 | Remote Frame | 0x40 | Transmit Acknowledge (equal to DIR==Tx) | 0x80 | Transmit Request (equal to DIR==TXREQUEST) | All others | Reserved | dword | read only | ● |
| 0x02 | The transmit buffer will be emptied before transmitting the message - the message is not blocked by other messages. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x04 | The NERR flag of the CAN transceiver was active at message reception (system is in single wire mode) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x08 | The message will be sent or was received in high voltage mode |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x10 | Remote Frame |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x40 | Transmit Acknowledge (equal to DIR==Tx) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x80 | Transmit Request (equal to DIR==TXREQUEST) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| All others | Reserved |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SIMULATED | Message has been sent by a simulated CAPL node; possible values: 0 (no), 1 (yes) Has been modified for the Simulation Setup for CANoe version 1.2 resp. 2.0 to distinguish between real and simulated components. | byte | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FDF | FD Format Indicator 0 = Classic CAN message1 = CAN FD message | char | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BRS | Bit Rate Switch Only for CAN FD messages. 0: Use arbitration bit rate for data segment1: use data bit rate for data segment | char | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ESI | Error State Indicator Read/Write:0 = ESI not set1 = ESI set Write:2 = CAN controller sets ESI automatically depending on the state of the controller | char | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SRR_INV | Inverted SRR. (This value is only available for some CAN hardware and a specific driver.) Value range: 0, 1 Default: 0 | char | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| R0 | Level of the R0 bit on the bus. (This value is only available for some CAN hardware and a specific driver.) Value range: 0, 1 | char | read only | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| R1 | Level of the R1 bit on the bus. (This value is only available for some CAN hardware and a specific driver.) Value range: 0, 1 | char | read only | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TxFailed | When sending a message you can use TxReqCount to set the number of transmission attempts (single shot mode). If it wasn't possible to send the message and transmission error notification is active you will be notified in the Trace Window and in CAPL with a TXReq message and the TxFailed message selector. Value range: 0, 1 | char | read only | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PDU Access |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| GetPDU(n, P) | Retrieve the PDU with index n in this message. The first PDU has index n = 0, the last PDU has index n = PDUCount() - 1. The parameter P must be of type PDU *. Return values other than 0 indicate an error. Return Values: 0: Data access successful. -1: Wrong bus type. -2: This frame does not support accessing PDUs. -3: The PDU object is invalid. -4: PDU is not of RX type. -5: Parameter too small (e.g. array has too less bytes) -6: Message or PDU is not available (any more) -7: PDU index out of bound. Use selector PDUCount() to detemine the number of PDUs. | long | read only | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| IsContainer() | Returns 1 if at least one AUTOSAR ContainerIPdu is mapped to this message, 0 otherwise. Negative return values indicate an error. See selector GetPDU() for possible error codes. | long | read only | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PDUCount() | Returns the number of all PDUs in this message. The return value includes mapped PDU even with unset update bit. The return value includes all contained PDUs in ContainerIPdu, but not the ContainerIPdu. Negative return values indicate an error. See selector GetPDU() for possible error codes. | long | read only | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| PDUOffset(n) | Returns the byte offset of the start of the PDU with index n in the payload of the message data. Negative return values indicate an error. See selector GetPDU() for possible error codes. | long | read only | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Other Properties |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FrameCRC | Checksum of the message. | dword | read only | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TxReqCount | Number of transmission attempts for a message. (This value is only available for some CAN hardware and a specific driver.)With 0 the message will be repeated until it has been sent successfully once. See also transmission error notification. Value range: 0…15 Default: 0 | char | — | ● |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TxCountRequired | Number of required transmission attempts for a message (only valid for TxReqCount > 0). Value range: 0…15 | char | read only | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| StuffCount | Contains the stuff count of a CAN FD ISO-message. For other message formats the value is 0. | byte | read only | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Example: Data Access |
|---|

| Rx | Message was received (DIR == Rx) |
|---|---|
| Tx | Message was transmitted (DIR == Tx) |
| TXREQUEST | Transmission request was set for message (DIR == TXREQUEST) |

| RXREMOTE | Remote message was received ((DIR == RX) && RTR) |
|---|---|
| TXREMOTE | Remote message was transmitted ((DIR == Tx) && RTR) |
| TXREQUESTREMOTE | Transmission request was set for remote message ((DIR == TXREQUEST) && RTR) |
| RXDATA | Data message was received ((DIR == Rx) && !RTR) |
| TXDATA | Data message was transmitted ((DIR == Tx) && !RTR) |
| TXREQUESTDATA | Transmission request was set for data message ((DIR == TXREQUEST) && !RTR) |

| Version 15© Vector Informatik GmbH |
|---|
