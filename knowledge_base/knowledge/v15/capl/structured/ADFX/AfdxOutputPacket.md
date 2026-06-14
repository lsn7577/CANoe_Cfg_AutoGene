# AfdxOutputPacket

> Category: `ADFX` | Type: `function`

## Syntax

```c
long AfdxOutputPacket( long packet ); // form 1
long AfdxOutputPacket( long packet, long txMode, long frag, long vl, long seqNo, long rma ); // form 2
```

## Description

The specified AFDX message is transmitted with this function call.

Note that the user has complete control of all the transmission scenarios. If the message is defined in an AFDX database the corresponding message attributes (e.g. timing, redundancy) are used for the transmission. CANoe internally uses an AFDX software stack for the message handling.

In the following cases the message needs to be defined in a DBC file and the file needs to be assigned to the actual configuration:

## Parameters

| Name | Description |
|---|---|
| packet | Handle of the message to send that has been created with AfdxInitPacket. |
| txMode | Set message’s transmission behavior: 0: (CyclicOff) An active cyclic transmission is switched off. The corresponding message is transmitted at least once after this call.Note: The message needs to be defined in the assigned DBC file. 1: (CyclicOn) The message is transmitted cyclically and the cycle time is defined via the attribute AfdxMsgTxRate in the assigned DBC file.Note: The message needs to be defined in the assigned DBC file. 2: (SingleShot) The message is transmitted once. |
| frag | Activate or deactivate IP fragmentation: 0: (NoIPFragmentation) The message is transmitted without fragmentation. 1: (DoIPFragmentation) This parameter value activates the IP fragmentation for a message based on the attributes in the DBC file. The fragment’s size corresponds to the value of the attribute AfdxVLmaxFrame. Furthermore the fragmentation for the message must be allowed (attribute AfdxVLipFrag = True).Note: The message needs to be defined in the assigned DBC file. |
| vl | Activate/deactivate software controlled VL scheduling: 0: (NoAFDXVLScheduling) The corresponding virtual link of this message is not controlled by the AFDX software stack. 1: (DoAFDXVLScheduling) The corresponding virtual link of this message is controlled by the AFDX software stack. The BAG value is taken from the message’s attribute AfdxVLbag.Note: The message needs to be defined in the assigned DBC file. |
| seqNo | Activate/deactivate automatic sequence number handling: 0: (NoAFDXSeqNoManagement) The actual sequence number from message’s payload is used. 1: (DoAFDXSeqNoManagement) The sequence number is automatically updated for the message. |
| Value | Short Name Description Interface_ID updated? Message duplicated? |
| 0 | DBRelated The line assignment for the message is derived from the assigned DBC file X X |
| 1 | ForceA The message is transmitted on the specified line. X — |
| 2 | ForceB The message is transmitted on the specified line. X — |
| 3 | ForceAB The message is transmitted on both lines. X X |
| 4 | ForceAonB The message is transmitted on the other line. The assignment is inverted. X — |
| 5 | ForceBonA The message is transmitted on the other line. The assignment is inverted. X — |
| 6 | ForceABonBA The message is transmitted on both lines and the line assignment is inverted. X X |
| 7 | ForceLineA The message is transmitted on the specified line. — — |
| 8 | ForceLineB The message is transmitted on the specified line. — — |
| 9 | ForceLineAB The message is transmitted on both lines. — X |
| 10 | MACIFRelated The line assignment is derived from the given MAC source address. — X |

## Example

see example of AfdxInitPacket

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2 | — | — | — | — |
| Restricted To | — | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
