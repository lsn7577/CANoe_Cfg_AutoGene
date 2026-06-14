# valOfId

> Category: `CAN` | Type: `function`

## Syntax

```c
long valOfId(dword id);
long valOfId(message m);
```

## Description

Returns the value of a message identifier independent of its type.

Identifier as long value.

## Parameters

| Name | Description |
|---|---|
| message | Variable of the type message. |
| id | Id portion of a message. |

## Return Values

Identifier as long value.

## Example

```c
on message *
{
long x;
x = valOfId(this);
write("Received Identifier: %d",x);
output(this);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | 13.0 | — | 1.0 |
| Restricted To | CAN | CAN | CAN | CAN | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
