# Class: CanDisturbanceExternalTrigger

> Category: `CANDisturbance` | Type: `notes`

## Description

This trigger can be used, if a sequence or a frame based sequence should be sent based on a digital input value.

—

You can access control information of a CanDisturbanceExternalTrigger object with the following attributes:

| Keyword | Description | Type | Access Limitations |
|---|---|---|---|
| DIOChannel | Number of the DIO channel. Possible values: 0: DIN0 1: DIN1 | dword | — |
| TriggerType | The trigger type used for the external trigger. Possible values: 0: Active Low 1: Active High 2: Rising Edge 3: Falling Edge | dword | — |

| Version 15© Vector Informatik GmbH |
|---|
