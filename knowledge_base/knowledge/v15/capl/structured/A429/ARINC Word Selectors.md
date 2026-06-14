# ARINC Word Selectors

> Category: `A429` | Type: `notes`

## Description

The offsets used together with the selector address the following parts of the ARINC word.

See Also

| Keyword | Description | Type | Access Limitation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| time | When an event handler (on a429Word/on a429Worderror) is triggered, the time stamp of the event is stored in the selector. unit: 10 µs | dword | read-only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| time_ns | When an event handler (on a429Word/on a429Worderror) is triggered, the time stamp of the event is stored in the selector. unit: nanoseconds | int64 | read-only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| msgChannel | Transmission channel (output) or the channel which triggered an event handler (on a429Word/on a429Worderror) Value range: 1..32 | word | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| ID | Label value Value range: 0..255 Example on a429Word * { if (this.ID == 55) { write("label o%o received; triggering logging...", this.ID); trigger(); }} | Example on a429Word * { if (this.ID == 55) { write("label o%o received; triggering logging...", this.ID); trigger(); }} | dword | — |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Example on a429Word * { if (this.ID == 55) { write("label o%o received; triggering logging...", this.ID); trigger(); }} |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| name | name of the ARINC word taken from the database (DBC) | char[] | read-only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| DIR | This direction is related to the corresponding event. A dedicated ARINC-429 channel may be either an Rx or Tx channel, but not both. Value range: Rx (default) Tx Example on a429Word * { if (this.DIR == Rx) { write("label o%o received", this.DIR); } if (this.DIR == Tx) { write("label o%o sent", this.DIR); }} | Example on a429Word * { if (this.DIR == Rx) { write("label o%o received", this.DIR); } if (this.DIR == Tx) { write("label o%o sent", this.DIR); }} | byte | read-only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Example on a429Word * { if (this.DIR == Rx) { write("label o%o received", this.DIR); } if (this.DIR == Tx) { write("label o%o sent", this.DIR); }} |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| parity | Overwrite the parity settings of a Tx channel for a specific ARINC word. The value may be change with the function a429SetParity. Value range: 0: use channel configuration (default) 1: disable hardware parity support 2: generate odd parity 3: generate even parity | word | read-only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TxCtrl | Define the scheduling type for the ARINC word with a429SetScheduleTx and a429StopTx. Value range: 0: on request 1: add to HW scheduler 2: remove from HW scheduler | byte | read-only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Error | The type of error is available in this field. Value Enumeration Value Description -1 a429NoError initialization value, no error 1 a429GapViolation Rx: gap error 2 a429ParityError Rx: parity violation 3 a429BitrateLow Rx: bit rate below the limit 4 a429BitrateHigh Rx: bit rate above the limit 5 a429FormatError Rx: edge detected after correctly received word 6 a429CodingError Rx: coding error during RZ coding 7 a429DutyFactor Rx: erroneous duty factor 8 a429AvgBitLength Rx: average bit length out of allowed range 256 a429LevelMismatch Tx: output short circuit 257 a429NotIdle Tx: no send access possible (after short circuit) Cross Reference You can find more detailed information about errors here. Example on a429Worderror * { switch (this.Error) { case 1: /* do some error handling here */ break; case 2: /* do some error handling here */ break; … default: break; }} | Value | Enumeration Value | Description | -1 | a429NoError | initialization value, no error | 1 | a429GapViolation | Rx: gap error | 2 | a429ParityError | Rx: parity violation | 3 | a429BitrateLow | Rx: bit rate below the limit | 4 | a429BitrateHigh | Rx: bit rate above the limit | 5 | a429FormatError | Rx: edge detected after correctly received word | 6 | a429CodingError | Rx: coding error during RZ coding | 7 | a429DutyFactor | Rx: erroneous duty factor | 8 | a429AvgBitLength | Rx: average bit length out of allowed range | 256 | a429LevelMismatch | Tx: output short circuit | 257 | a429NotIdle | Tx: no send access possible (after short circuit) | Cross Reference You can find more detailed information about errors here. | Example on a429Worderror * { switch (this.Error) { case 1: /* do some error handling here */ break; case 2: /* do some error handling here */ break; … default: break; }} | long | read-only |
| Value | Enumeration Value | Description |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| -1 | a429NoError | initialization value, no error |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 1 | a429GapViolation | Rx: gap error |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | a429ParityError | Rx: parity violation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | a429BitrateLow | Rx: bit rate below the limit |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | a429BitrateHigh | Rx: bit rate above the limit |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | a429FormatError | Rx: edge detected after correctly received word |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | a429CodingError | Rx: coding error during RZ coding |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | a429DutyFactor | Rx: erroneous duty factor |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | a429AvgBitLength | Rx: average bit length out of allowed range |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 256 | a429LevelMismatch | Tx: output short circuit |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 257 | a429NotIdle | Tx: no send access possible (after short circuit) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Cross Reference You can find more detailed information about errors here. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Example on a429Worderror * { switch (this.Error) { case 1: /* do some error handling here */ break; case 2: /* do some error handling here */ break; … default: break; }} |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| simulated | If an ARINC event is detected this selector specifies whether the event was caused by CANoe or not. Value range: 0: real event caused outside from the tool 1: simulated event caused by the tool | byte | read-only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| TxCycle | This is the cycle time (in microseconds) which is given to the HW scheduler with output. The cycle time is set with a429SetScheduleTx. | dword | read-only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| FrameLen | Length of the detected ARINC word in nanoseconds. | dword | read-only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| BitRate | Detected bit rate for the ARINC word. | dword | read-only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Gap | Specify the minimum distance to be kept for a scheduled ARINC word. This may be combined with the hardware scheduler. The gap may be set with a429SetGap in combination with a429CalcBitLength. The value is given in nanoseconds. | dword | read-only |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Keyword | Description | Type | Access Limitation |
|---|---|---|---|
| byte(x); char(x) | access 8 bits in an ARINC word; x: 0..3 | — | — |
| word(x); int(x) | access 16 bits in an ARINC word; x: 0..2 | — | — |
| dword(x); long(x) | access 32 bits in an ARINC word; x: 0 | — | — |

| Offset | 3 | 2 | 1 | 0 |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| Byte(0)/char(0) | 0 |  |  |  |  |  |  |  |
| Byte(1)/char(1) |  |  |  |  |  |  |  |  |
| Byte(2)/char(2) |  |  |  |  |  |  |  |  |
| Byte(3)/char(3) |  |  |  |  |  |  |  |  |
| Word(0)/int(0) | 0 |  |  |  |  |  |  |  |
| Word(1)/int(1) |  |  |  |  |  |  |  |  |
| Word(2)/int(2) |  |  |  |  |  |  |  |  |
| Dword(0)/long(0) | 0 |  |  |  |  |  |  |  |
| Meaning | Parity + SSM + Data | Data | Data + SDI | ARINC-Label |  |  |  |  |
| Bit number | 32 | 25 | 24 | 17 | 16 | 9 | 8 | 1 |

| Version 15© Vector Informatik GmbH |
|---|
