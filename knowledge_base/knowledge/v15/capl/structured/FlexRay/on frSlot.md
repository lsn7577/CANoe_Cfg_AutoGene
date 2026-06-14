# on frSlot

> Category: `FlexRay` | Type: `event`

## Description

This event procedure is called up in each cycle after the slot is past. The event procedure is only called for slots in the static segment.

The event procedure is also called up if no frame is received in the specified slot.

Thus it will synchronously be executed to the FlexRay cycle. Therefore it cannot be used in the Measurement Setup or the analysis branch.

If any frame is not received in the slot, then the event procedure is called with the next slot that contains a frame or at the latest when the next cycle begins. For the VN interfaces it will be called approx. 500 microseconds after the slot.

If two frames are received in slot <slot ID> (on channel A and B), then the event procedure is called up just once (and in fact, with the frame contents of channel A).

The selectors always reference the contents of the Slot. The FrameType selector should be evaluated before further processing.

Value range for n: 1 <= <slot ID> <= max. static slot ID of the cluster configuration.

An optional channel parameter for event filtering can be assigned to all functions.

## Example

The following program executes an action always when the static slot 60 is expired.

```c
on frSlot 60
{
   // 
 slot 60 is over ... do action ...
   // Note: The handler is called even if any frame
   // is not received in this slot!
   if (this.Type == 1) // valid Frame was received in this slot
   {

      // Attention: Frame can be from channel A or B.
      // If received on both, then only frame from channel A
      // 
 will be signaled and retrieved here.
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 SP2 | 5.2 SP2 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |

## Selectors

| Time (data type dword)Time_ns (data type int64) | The Slot N time stamp that has been synchronized with the global time base in the computer (CAN hardware or computer system clock). The time stamp must be used if time relations should be regarded with events from other sources. This time stamp is also output in the Trace Window when receiving a frame in Slot n. Timer unit: 10 microseconds.NS timer unit: nanoseconds. Note: The Time selector is not available when executing CAPL programs directly on an interface hardware (CAPL-on-Board). Write- protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| msgChannel | Channel in the tool that the FlexRay CC determines. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_ChannelMask | Identifies the FlexRay channel of the CC. With 1 the frame was received on channel A, with 2 on channel B. If a frame is received on each channel, the only the frame from channel A is returned. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_SlotID | Always contains the n value. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_Cycle | Current FlexRay cycle number. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Type | Identifies the type of frame (=data type: int) and whether a frame has even been received.Possible values: Normal=1 A valid data frame was received. Error=-1 A faulty frame was received. Null=0 An empty (null) data frame was received. Empty=-2 No frame was received. Important: If no frame is received in the specified slot, the contents of the ChannelMask, PayloadLength, msg, Flags, HeaderCRC, Status, DIR and SIMULATED selectors are invalid! Write-protected! | Normal=1 | A valid data frame was received. | Error=-1 | A faulty frame was received. | Null=0 | An empty (null) data frame was received. | Empty=-2 | No frame was received. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Normal=1 | A valid data frame was received. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Error=-1 | A faulty frame was received. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Null=0 | An empty (null) data frame was received. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Empty=-2 | No frame was received. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_PayloadLength | Length of the presented payload in 16Bit words (=data type: word). Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| msg | Payload of the message.The number of valid databytes is specified by the PayloadLength. Direct access to the data is not possible. It takes place via byte(index), word(index) or dword(index), whereby index is always byte-oriented and counted from 0. Thus, dword(1) returns the double word from bytes 1...4 and not from bytes 4...7. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_Flags | Provides more detailed status information from the frame header, if necessary.Possible values: Bit Mask Meaning 0x1 Null Frame 0x2 Payload valid = msg contains valid data 0x4 Frame set the sync bit. 0x8 Frame set the start-up bit. 0x10 Frame set the payload preamble bit. 0x20 Frame set the reserved bit. 0x40 Frame is faulty. 0x80 The data of the redundant frame is inconsistent on both channels. 0x100 The frame is a dummy frame and was not received by the bus. 0x200 — 0x400 — 0x800 — 0x1000 — 0x2000 — 0x4000 The frame was sent/simulated. 0x8000 The frame was received in asynchronous mode. 0x10000 It is a PDU! 0x20000 PDU Rx Update Bit 0x40000 PDU Tx Update Bit 0x80000 If PDUs are received, this bit indicates a normal frame! 0x100000 Frame is part of the dynamic segment. Write-protected! | Bit Mask | Meaning | 0x1 | Null Frame | 0x2 | Payload valid = msg contains valid data | 0x4 | Frame set the sync bit. | 0x8 | Frame set the start-up bit. | 0x10 | Frame set the payload preamble bit. | 0x20 | Frame set the reserved bit. | 0x40 | Frame is faulty. | 0x80 | The data of the redundant frame is inconsistent on both channels. | 0x100 | The frame is a dummy frame and was not received by the bus. | 0x200 | — | 0x400 | — | 0x800 | — | 0x1000 | — | 0x2000 | — | 0x4000 | The frame was sent/simulated. | 0x8000 | The frame was received in asynchronous mode. | 0x10000 | It is a PDU! | 0x20000 | PDU Rx Update Bit | 0x40000 | PDU Tx Update Bit | 0x80000 | If PDUs are received, this bit indicates a normal frame! | 0x100000 | Frame is part of the dynamic segment. |
| Bit Mask | Meaning |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x1 | Null Frame |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x2 | Payload valid = msg contains valid data |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x4 | Frame set the sync bit. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x8 | Frame set the start-up bit. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x10 | Frame set the payload preamble bit. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x20 | Frame set the reserved bit. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x40 | Frame is faulty. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x80 | The data of the redundant frame is inconsistent on both channels. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x100 | The frame is a dummy frame and was not received by the bus. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x200 | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x400 | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x800 | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x1000 | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x2000 | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x4000 | The frame was sent/simulated. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x8000 | The frame was received in asynchronous mode. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x10000 | It is a PDU! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x20000 | PDU Rx Update Bit |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x40000 | PDU Tx Update Bit |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x80000 | If PDUs are received, this bit indicates a normal frame! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x100000 | Frame is part of the dynamic segment. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_HeaderCRC | Delivers the CRC in the header of the frame received. Write-protected! |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_Segment | This selector always returns Static since this event procedure is only permissible for static slots.Possible values: Static=0 Frame belongs to the status segment Dynamic=1 Frame belongs to the dynamic segment Write-protected! | Static=0 | Frame belongs to the status segment | Dynamic=1 | Frame belongs to the dynamic segment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Static=0 | Frame belongs to the status segment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Dynamic=1 | Frame belongs to the dynamic segment |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FR_Status | Delivers additional status information about the reception buffer of the CC, if necessary. Bit Mask Label Meaning 0x800 TxConflict Only with Tx frames: Will be set if there already exists a frame in that slot and cycle. Due to the bus physics a transmission conflict is not detected in any case. This bit will only be set from the VN interface. Available from CANoe 7.2. All other bits of the status are reserved. Write-protected! | Bit Mask | Label | Meaning | 0x800 | TxConflict | Only with Tx frames: Will be set if there already exists a frame in that slot and cycle. Due to the bus physics a transmission conflict is not detected in any case. This bit will only be set from the VN interface. Available from CANoe 7.2. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Bit Mask | Label | Meaning |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0x800 | TxConflict | Only with Tx frames: Will be set if there already exists a frame in that slot and cycle. Due to the bus physics a transmission conflict is not detected in any case. This bit will only be set from the VN interface. Available from CANoe 7.2. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DIR (byte data type) | Transmission direction of the message.Possible values: Tx Message was send by the hardware. Rx Message was received. TXRequest Transmit request Write-protected! | Tx | Message was send by the hardware. | Rx | Message was received. | TXRequest | Transmit request |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Tx | Message was send by the hardware. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Rx | Message was received. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TXRequest | Transmit request |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| SIMULATED | This flag indicates whether the message was simulated.Values: 0 Not simulated 1 Simulated Write-protected! | 0 | Not simulated | 1 | Simulated |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 0 | Not simulated |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | Simulated |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
