# SetReplayFileName

> Category: `Other` | Type: `function`

## Syntax

```c
dword setReplayFileName(char nameOfReplayBlock[], char fileName[], char fileType[]);
```

## Description

Replaces the source file of an existing Replay Block. The function call temporarily stops the replay and restarts the Replay Block with the new source file.

The function call temporarily stops the replay and restarts the Replay Block with the new source file, if replay is active before file change.

The function call will not modify the configuration of the Reply block in the Simulation Setup. The new file will not be stored when saving the configuration.

If you change the source file during measurement in the configuration dialog of the Reply block, the new file name will be stored in the configuration.

Note: If the function is executed in the on start handler, no replay is started. To start the replay together with the function, the function must be executed outside the on start handler. Alternatively, the replay can be started with ReplayStart.

## Parameters

| Name | Description |
|---|---|
| nameOfReplayBlock | Contents of the Replay name field in the replay configuration dialog. |
| fileName | The new source file (as absolute or relative path to the configuration file). |
| fileType | The source file type (as string): ASC, BLF For all other source file types that are available in the selection dialog of the CANoe Replay Block, use BLF as fileType parameter. |

## Return Values

—

## Example

```c
SetReplayFilename("R", "replay_test_capl1.asc", "asc");
SetReplayFilename("R", "replay_test_capl1.blf", "blf");
SetReplayFilename("R", "replay_test_capl1.mf4", "blf");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 SP3 | 8.0 SP3 | 13.0 | — | 14 | 1.0 |
| Restricted To | Not in standalone mode | Not in standalone mode | — | — | Not in standalone mode | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | — | — | ✔ | N/A |
