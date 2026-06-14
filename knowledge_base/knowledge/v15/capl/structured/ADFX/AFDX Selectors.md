# AFDX Selectors

> Category: `ADFX` | Type: `notes`

## Description

More information about A664Messages Versus A664Frames.

Selectors for Identification and Timing

Selectors on Ethernet level

a664Frame

a664Message

BAG

Bandwidth allocation GAP.

If the message is initialized via a DBC, the attribute AfdxVLbag is used.

byte

x

byte[]

read-only

DIR

This direction is related to the corresponding event.

Distance

Measured timely distance between two AFDX messages on the same virtual link (VL).

Note that for a reassembled message (bit 10 in ErrFlag is set) this value is 0.

word

ErrFlag

This flag carries error details for the received message.

dword

Length of the message object given in bytes. All header fields, payload bytes and sequence counter are considered for this value.

Transmission channel (output) or the channel which triggered an event handler (on a664Frame/on a664Message).

Message name taken from an assigned data base (DBC).

If an event is detected, this selector specifies whether the event was caused by CANoe or not.

SkewMax

This is the maximum timely difference between a transmission on line A and B. The value SkewMax is considered for Rx direction only.

read-only3

time

When an event handler (on a664Frame/on a664Message) is triggered, the time stamp of the event is stored in the selector.

time_ns

int64

TxCycle

Transmission cycle of an AFDX message.

0

1 (0x0001)

Frame was received on line B (line information).

1 (0x0002)

Frame is redundant; redundancy manager detected a valid redundancy condition for this frame (option Enable Redundancy Checks has to be active and DBC attribute AfdxVLrma is set to True).

1 (0x0004)

Frame is an IP FRAGMENT.

1 (0x0008)

Frame belongs to a service access point (SAP) connection.

1 (0x0010)

Frame received on wrong line; receive line collides with MAC source address.

1 (0x0020)

Frame is not a valid AFDX frame.

1 (0x0040)

A wrong sequence number was received (option Enable Integrity Checks has to be active, DBC attribute AfdxVLintCheck is set to True).

1 (0x0080)

Redundancy error encountered; either a frame was lost or the time for Skew Max was exceeded (option Enable Redundancy Checks has to be active, DBC attribute AfdxVLrma is set to True, time according to DBC attribute AfdxVLskewMax was exceeded).

1 (0x0100)

Fragmentation / reassembly error; typically a fragment is missing or misordered.

1 (0x0200)

Protocol decoding error detected (error on IP, UDP or SNMP level).

1 (0x0400)

This is a reassembled packet (message).

1 (0x0800)

Frame was checked by redundancy management (option Enable Redundancy Checks has to be active and DBC attribute AfdxVLrma is set to True).

1 (0x1000)

A constant or value violates the AFDX recommendation (e.g. address constants / range wrong or eth-part <> IP-part).

1 (0x2000)

Frame size does not match expected size as defined in database.

1 (0x4000)

Packet is unknown (not defined in the database).

1 (0x8000)

Frame was checked by integrity management (option Enable Integrity Checks has to be active and DBC attribute AfdxVLIntCheck is set to True).

Destination MAC address. This value is constructed from EthAdrDstConst and EthVlId. Structure of destination MAC address:

EthAdrDstConst (0x03000000)

EthVlId

The selector is initialized with the values taken from EthAdrDstConst and EthVlId. Without an assigned DBC the array is initialized with {0x03, 0x00, 0x00, 0x00, 0x03, 0xE8}.

read-only1

Constant part of destination MAC address (EthAdrDst byte[0] – byte[3]).

The selector is initialized together with the selector EthAdrDst.

Source MAC address, this value is created from EthAdrSrcConst and IpAdrSrc. Structure of source MAC address:

EthAdrSrcConst (0x020000)

EthUserId (A.B.C.D)

The selector is initialized with the values taken from EthAdrSrcConst and IpAdrSrc. Without an assigned DBC the array is initialized with {0x02, 0x00, 0x00, 0x03, 0xE8, 0x00}.

The line information is taken from LineSelect.

Constant part of destination MAC address (EthAdrSrc byte[3] – byte[5]).

This number identifies a specific address part of the source MAC address (EthAdrSrc byte[1] – byte[2]).

AFDX Virtual Link Identifier (EthAdrDst byte[4] – byte[5]).

Length of an IP frame including 20 bytes of header information (options and padding is not considered).

If not explicitly set during message creation the initialization value is 0. For messages created with information from the DBC this value is derived from the AFDX payload length.

read-only2

IP destination address (consider network byte ordering for access).

read-only5

IP source address (consider network byte ordering for access).

Set the fragmentation attribute for messages to be transmitted over a VL.

If the message is initialized from a DBC, the attribute AfdxVLipFrag is used for initialization.

read-only4

IP payload area The array is limited by IpLength ([0, IpLength - 20 - 1).

The initialization value is 0.

Value of IP protocol field

Fragmentation offset (consider network byte ordering for access).

Fragmentation attribute of frame.

UdpDstPort

UDP destination Port (consider network byte ordering for access).

If the message is initialized from a DBC, the attribute AfdxVLdestUDP is used for initialization.

UdpLength

Length of the UDP payload (AfdxLength + 8).

UdpSrcPort

UDP Source Port (consider network byte ordering for access).

AfdxPayload

Payload area of AFDX message.

AfdxLength

Length of the AFDX payload.

For messages created with information from the DBC this value is derived from the AFDX payload length. Every message is created with a buffer area for the maximum size.

IntChk

Integrity check for VL.

The initialization value is 1. If the message is initialized from a DBC, the attribute AfdxVLintCheck is used for initialization.

RMA

Redundancy management.

The initialization value is 1. If the message is initialized from a DBC, the attribute AfdxVLrma is used for initialization.

LineSelect

Determine the used line A and/or B.

The initialization value is 3. If the message is initialized from a DBC, the attribute AfdxVLnetSel is used for initialization.

MaxFrameSize

Define the maximum frame size for a VL.

The initialization value is 1471. If the message is initialized from a DBC, the attribute AfdxVLmaxFrame is used for initialization.

SubVLNr

Sub VL number range.

The initialization value is 1. If the message is initialized from a DBC, the attribute AfdxVLsubVL is used for initialization.

SubVLid

Used sub VL identifier.

The initialization value is 1. If the message is initialized from a DBC, the attribute AfdxVLsubVLId is used for initialization.

read-only6

| Note For programming examples, refer to the help pages: Declaration of AFDX Frames Declaration of AFDX Messages More information about A664Messages Versus A664Frames. |
|---|

| Quick Access |
|---|
| Selectors for Identification and Timing |
| Selectors on Ethernet level |
| Selectors on IP level |
| Selectors on UDP level |
| Selectors on AFDX level |

| Keyword | Description | a664Frame | a664Message | Type | Access Limitations |
|---|---|---|---|---|---|
| BAG | Bandwidth allocation GAP. Unit: milliseconds Value range: 1 …128 (initialization value) If the message is initialized via a DBC, the attribute AfdxVLbag is used. | x | x | byte | read-only3 |
| Data | This is the complete raw content of the object as counted by the selector Length. Note that all data is given in network byte order. If you copy this to a structure, use the function memcpy_n2h(). Value range: This array of bytes is initialized with 0. | x | x | byte[] | read-only |
| DIR | This direction is related to the corresponding event. Value range: Rx = 0 (default) Tx = 1 | x | x | byte | read-only |
| Distance | Measured timely distance between two AFDX messages on the same virtual link (VL). Note that for a reassembled message (bit 10 in ErrFlag is set) this value is 0. Unit: microseconds | x | x | word | read-only |
| ErrFlag | This flag carries error details for the received message. Value range: see table below | x | x | dword | read-only |
| Keyword | Description | a664Frame | a664Message | Type | Access Limitations |
| ID | The message ID is derived from the address information (see database support). | x | x | word | - |
| Length | Length of the message object given in bytes. All header fields, payload bytes and sequence counter are considered for this value. Unit: bytes Value range: 60 … 8192 + 42 + 1 | x | x | word | read-only |
| msgChannel | Transmission channel (output) or the channel which triggered an event handler (on a664Frame/on a664Message). Value range: 1..16 | x | x | word | - |
| name | Message name taken from an assigned data base (DBC). Value range: \0 or valid name | x | x | char[] | read-only |
| SIMULATED | If an event is detected, this selector specifies whether the event was caused by CANoe or not. Value range: 0: real event caused outside from the tool 1: simulated event caused by the tool example. See example: Detect real message in CAPL. | x | x | byte | read-only |
| Keyword | Description | a664Frame | a664Message | Type | Access Limitations |
| SkewMax | This is the maximum timely difference between a transmission on line A and B. The value SkewMax is considered for Rx direction only. Unit: microseconds Value range: 0 … 65635 (initialization value). If the message is initialized via a DBC the attribute AfdxVLskewMax is used. | x | x | dword | read-only3 |
| time | When an event handler (on a664Frame/on a664Message) is triggered, the time stamp of the event is stored in the selector. Unit: 10 µs | x | x | dword | read-only |
| time_ns | When an event handler (on a664Frame/on a664Message) is triggered, the time stamp of the event is stored in the selector. Unit: nanoseconds | x | x | int64 | read-only |
| TxCycle | Transmission cycle of an AFDX message. Unit: Milliseconds Value range: If the message is initialized via a DBC the attribute AfdxMsgTxRate is used. | x | dword | - |  |

| Bit | Value | Meaning |
|---|---|---|
| 0 | 1 (0x0001) | Frame was received on line B (line information). |
| 1 | 1 (0x0002) | Frame is redundant; redundancy manager detected a valid redundancy condition for this frame (option Enable Redundancy Checks has to be active and DBC attribute AfdxVLrma is set to True). |
| 2 | 1 (0x0004) | Frame is an IP FRAGMENT. |
| 3 | 1 (0x0008) | Frame belongs to a service access point (SAP) connection. |
| 4 | 1 (0x0010) | Frame received on wrong line; receive line collides with MAC source address. |
| 5 | 1 (0x0020) | Frame is not a valid AFDX frame. |
| 6 | 1 (0x0040) | A wrong sequence number was received (option Enable Integrity Checks has to be active, DBC attribute AfdxVLintCheck is set to True). |
| 7 | 1 (0x0080) | Redundancy error encountered; either a frame was lost or the time for Skew Max was exceeded (option Enable Redundancy Checks has to be active, DBC attribute AfdxVLrma is set to True, time according to DBC attribute AfdxVLskewMax was exceeded). |
| Bit | Value | Meaning |
| 8 | 1 (0x0100) | Fragmentation / reassembly error; typically a fragment is missing or misordered. |
| 9 | 1 (0x0200) | Protocol decoding error detected (error on IP, UDP or SNMP level). |
| 10 | 1 (0x0400) | This is a reassembled packet (message). |
| 11 | 1 (0x0800) | Frame was checked by redundancy management (option Enable Redundancy Checks has to be active and DBC attribute AfdxVLrma is set to True). |
| 12 | 1 (0x1000) | A constant or value violates the AFDX recommendation (e.g. address constants / range wrong or eth-part <> IP-part). |
| 13 | 1 (0x2000) | Frame size does not match expected size as defined in database. |
| 14 | 1 (0x4000) | Packet is unknown (not defined in the database). |
| 15 | 1 (0x8000) | Frame was checked by integrity management (option Enable Integrity Checks has to be active and DBC attribute AfdxVLIntCheck is set to True). |

| Keyword | Description | a664Frame | a664Message | Type | Access Limitations |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AfdxSeqNr | AFDX sequence number. | x | x | byte | read-only |  |  |  |  |  |  |  |  |  |  |  |
| EthAdrDst | Destination MAC address. This value is constructed from EthAdrDstConst and EthVlId. Structure of destination MAC address: 48 Bit Byte 5 Byte 4 Byte 3 Byte 2 Byte 1 Byte 0 EthAdrDst EthAdrDstConst (0x03000000) EthVlId The selector is initialized with the values taken from EthAdrDstConst and EthVlId. Without an assigned DBC the array is initialized with {0x03, 0x00, 0x00, 0x00, 0x03, 0xE8}. | 48 Bit | Byte 5 | Byte 4 | Byte 3 | Byte 2 | Byte 1 | Byte 0 | EthAdrDst | EthAdrDstConst (0x03000000) | EthVlId | x | x | byte[6] | read-only1 |  |
| 48 Bit |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Byte 5 | Byte 4 | Byte 3 | Byte 2 | Byte 1 | Byte 0 |  |  |  |  |  |  |  |  |  |  |  |
| EthAdrDst |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EthAdrDstConst (0x03000000) | EthVlId |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EthAdrDstConst | Constant part of destination MAC address (EthAdrDst byte[0] – byte[3]). The selector is initialized together with the selector EthAdrDst. | x | x | dword | - |  |  |  |  |  |  |  |  |  |  |  |
| EthAdrSrc | Source MAC address, this value is created from EthAdrSrcConst and IpAdrSrc. Structure of source MAC address: 48 Bit Byte 5 Byte 4 Byte 3 Byte 2 Byte 1 Byte 0 EthAdrSrc EthAdrSrcConst (0x020000) EthUserId (A.B.C.D) LineThe line information is added once the message is received.* The selector is initialized with the values taken from EthAdrSrcConst and IpAdrSrc. Without an assigned DBC the array is initialized with {0x02, 0x00, 0x00, 0x03, 0xE8, 0x00}. The line information is taken from LineSelect. | 48 Bit | Byte 5 | Byte 4 | Byte 3 | Byte 2 | Byte 1 | Byte 0 | EthAdrSrc | EthAdrSrcConst (0x020000) | EthUserId (A.B.C.D) | LineThe line information is added once the message is received.* | x | x | byte[6] | read-only1 |
| 48 Bit |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Byte 5 | Byte 4 | Byte 3 | Byte 2 | Byte 1 | Byte 0 |  |  |  |  |  |  |  |  |  |  |  |
| EthAdrSrc |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EthAdrSrcConst (0x020000) | EthUserId (A.B.C.D) | LineThe line information is added once the message is received.* |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| EthAdrSrcConst | Constant part of destination MAC address (EthAdrSrc byte[3] – byte[5]). Value range: The value is initialized with {0x02, 0x00, 0x00} . | x | x | byte[3] | - |  |  |  |  |  |  |  |  |  |  |  |
| EthUserId | This number identifies a specific address part of the source MAC address (EthAdrSrc byte[1] – byte[2]). Value range: 1 … 65535 The selector is initialized with the value 1000. | x | x | word | - |  |  |  |  |  |  |  |  |  |  |  |
| EthVlId | AFDX Virtual Link Identifier (EthAdrDst byte[4] – byte[5]). Value range: 1 … 65535 If the message is created via the DBC, the message attribute AfdxVLid is used for initialization. | x | x | word | read-only1 |  |  |  |  |  |  |  |  |  |  |  |

| Keyword | Description | a664Frame | a664Message | Type | Access Limitations |
|---|---|---|---|---|---|
| IpLength | Length of an IP frame including 20 bytes of header information (options and padding is not considered). If not explicitly set during message creation the initialization value is 0. For messages created with information from the DBC this value is derived from the AFDX payload length. Value range: 46 ... 1500 | x | x | word | read-only2 |
| IpAdrDst | IP destination address (consider network byte ordering for access). Value range: The initialization value is 0x0. If the message is initialized from a DBC, the attribute AfdxVLdestIP is used for initialization. ICMP: If the message is initialized from a DBC, the attribute ICMP_destIP is used for initialization. | x | x | dword | read-only5 |
| IpAdrSrc | IP source address (consider network byte ordering for access). Value range: The initialization value is 10.3.232.0 (0x0A03E800). If the message is initialized from a DBC, the attribute AfdxVLsrcIP is used for initialization. | x | x | dword | read-only5 |
| IpFragAllowed | Set the fragmentation attribute for messages to be transmitted over a VL. Value range: 0 (don’t fragment) -> initialization value 1 (fragmentation allowed) If the message is initialized from a DBC, the attribute AfdxVLipFrag is used for initialization. | x | x | byte | read-only4 |
| Keyword | Description | a664Frame | a664Message | Type | Access Limitations |
| IpPayload | IP payload area The array is limited by IpLength ([0, IpLength - 20 - 1). The initialization value is 0. | x | byte[] | - |  |
| IpProtocol | Value of IP protocol field Value range: 1 (ICMP) 17 (UDP) | x | byte | - |  |
| IpFragOffset | Fragmentation offset (consider network byte ordering for access). The initialization value is 0. | x | word | - |  |
| IpIsFragment | Fragmentation attribute of frame. Value range: 0: no Fragment 1: is fragment | x | word | - |  |

| Keyword | Description | a664Frame | a664Message | Type | Access Limitations |
|---|---|---|---|---|---|
| UdpDstPort | UDP destination Port (consider network byte ordering for access). Value range: The initialization value is 1. If the message is initialized from a DBC, the attribute AfdxVLdestUDP is used for initialization. | x | x | word | read-only1 |
| UdpLength | Length of the UDP payload (AfdxLength + 8). Value range: During message creation this value is set to 1472. For messages created with information from the DBC this value is derived from the AFDX payload length. | x | x | word | read-only2 |
| UdpSrcPort | UDP Source Port (consider network byte ordering for access). Value range: The initialization value is 1. If the message is initialized from a DBC, the attribute AfdxVLsrcUDP is used for initialization. | x | x | word | read-only1 |

| Keyword | Description | a664Frame | a664Message | Type | Access Limitations |
|---|---|---|---|---|---|
| AfdxPayload | Payload area of AFDX message. | x | x | byte[] | - |
| AfdxLength | Length of the AFDX payload. Value range: 0 … 8192. For messages created with information from the DBC this value is derived from the AFDX payload length. Every message is created with a buffer area for the maximum size. | x | x | word | read-only2 |
| IntChk | Integrity check for VL. Value range: 0 (disabled) 1 (enabled) The initialization value is 1. If the message is initialized from a DBC, the attribute AfdxVLintCheck is used for initialization. | x | x | byte | read-only3 |
| RMA | Redundancy management. Value range: 0 (disabled) 1 (enabled) The initialization value is 1. If the message is initialized from a DBC, the attribute AfdxVLrma is used for initialization. | x | x | byte | read-only3 |
| Keyword | Description | a664Frame | a664Message | Type | Access Limitations |
| LineSelect | Determine the used line A and/or B. Value range: 1 (line A) 2 (line B) 3 (line A and B) The initialization value is 3. If the message is initialized from a DBC, the attribute AfdxVLnetSel is used for initialization. | x | x | byte | read-only3 |
| MaxFrameSize | Define the maximum frame size for a VL. Value range: 17 … 1471 The initialization value is 1471. If the message is initialized from a DBC, the attribute AfdxVLmaxFrame is used for initialization. | x | x | dword | read-only3 |
| SubVLNr | Sub VL number range. Value range: 1 … 4 The initialization value is 1. If the message is initialized from a DBC, the attribute AfdxVLsubVL is used for initialization. | x | x | byte | read-only3 |
| SubVLid | Used sub VL identifier. Value range: 1 … 4 The initialization value is 1. If the message is initialized from a DBC, the attribute AfdxVLsubVLId is used for initialization. | x | x | byte | read-only6 |

| Version 15© Vector Informatik GmbH |
|---|
