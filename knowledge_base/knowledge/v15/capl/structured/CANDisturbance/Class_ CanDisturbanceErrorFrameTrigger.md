# Class: CanDisturbanceErrorFrameTrigger

> Category: `CANDisturbance` | Type: `notes`

## Description

This trigger can be used to trigger on an active error flag or the error flag delimiter of an error frame. The error frame phase can be configured by a flag field.

—

You can access control information of a CanDisturbanceErrorFrameTrigger object with the following attributes:

| Keyword | Description | Type | Access Limitations |  |
|---|---|---|---|---|
| ErrorFramePhase | The phase of the error frame. Possible values: 0: Active error flag 1: Error flag delimiter | dword | — |  |
| Offset | The offset within the phase. Note If the error frame phase is the active error flag, the minimum value for the offset is 6. | Note If the error frame phase is the active error flag, the minimum value for the offset is 6. | dword | — |
| Note If the error frame phase is the active error flag, the minimum value for the offset is 6. |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
