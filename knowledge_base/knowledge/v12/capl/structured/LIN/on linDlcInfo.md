# on linDlcInfo

> Category: `LIN` | Type: `event`

## Description

The event procedure on linDlcInfo is called when the LIN hardware has successfully measured the length of an unknown frame. This only occurs when the LIN hardware is in Slave mode.

In Master mode, when no deviating values are specified by the database or CAPL functions, the LIN hardware assumes the frame length derived from the frame identifier.

The keyword this and the selectors can be used to access the data of the event that has just been received.

## Availability

| Since Version |
|---|

## Selectors

| linDlcInfo | ../Selectors/CAPLfunctionLINDLCInfo.htm |
|---|---|
