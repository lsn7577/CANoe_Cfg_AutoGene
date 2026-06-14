# mostGetHWInfo

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGetHWInfo(long channel, long infoID); // form 1
long mostGetHWInfo(long channel, long infoID, char infostring[], long buffersize); // form 2
```

## Description

Provides information about the MOST interface used.

## Parameters

| Name | Type | Description |
|---|---|---|
| channel |  | Channel of the connected interface. |
| ID | Return Value | Description of the Return Value |
| kMostHWInfo_Type = 0 | >0 | Interface type: 1: VN2600/VN26102: OptoLyzer3: —4: OptoLyzer G2 3150o5: VN26406: OptoLyzer G2 3050e7: —8: OptoLyzer MOCCA compact 50e9: Logger10: OptoLyzer MOCCA compact 150c |
| kMostHWInfo_SimulationMode = 1 | 0, 1 | 0: real1: simulated |
| kMostHWInfo_Manufacturer = 2 |  | Manufacturer: "Vector", "K2L" |
| kMostHWInfo_SyncMode = 3 | >=0 | Synchronization mode: 0: off1: SW Sync active2: HW Sync active (bus interface on <channel> is Sync Master)3: HW Sync active (bus interface on <channel> is Sync Slave) |
| kMostHWInfo_SyncStatus = 4 | >=0 | Synchronization status: 0: HW Sync not active1: HW Sync active2: HW Sync works correctly |
| infostring |  | Target buffer to which text information is copied. |
| buffersize |  | Size of the target buffer. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
