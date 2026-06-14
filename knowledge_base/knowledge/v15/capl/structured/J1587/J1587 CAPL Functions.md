# J1587 CAPL Functions

> Category: `J1587` | Type: `notes`

## Description

on J1587ErrorMessage

Receipt of an error message.

on J1587Message

Receipt of a J1587 message.

Appends a J1587 parameter to a J1708 message.

Gets a J1587 parameter inside a J1708 message given a specific PID.

Gets the count of J1587 parameters inside a given J1708 message.

Selects the setting for the transport protocol.

| J1587 Only available with option .J1587. |
|---|

| Event Handler | Short Description |
|---|---|
| on J1587ErrorMessage | Receipt of an error message. |
| on J1587Message | Receipt of a J1587 message. |
| on J1587Param | Receipt of a J1587 parameter. |

| Functions | Short Description |
|---|---|
| J1587AppendParameter | Appends a J1587 parameter to a J1708 message. |
| J1587GetParameter | Gets a J1587 parameter inside a J1708 message at a given index. |
| J1587GetParameterByPID | Gets a J1587 parameter inside a J1708 message given a specific PID. |
| J1587GetParameterCount | Gets the count of J1587 parameters inside a given J1708 message. |
| setJ1587TP | Selects the setting for the transport protocol. |

| Version 15© Vector Informatik GmbH |
|---|
