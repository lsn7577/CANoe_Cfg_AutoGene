# mostAsFsEnable, mostAsFsDisable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsFsEnable();
long mostAsFsDisable();
```

## Description

mostAsFsEnable() makes the function service available for the function block. The function block must be assigned to the CAPL program via mostApRegister(fblockID, instIDDefault) or the database. Furthermore mostAsFsEnable() enables the functions <FktIDs>, <Notification> and <NotificationCheck> of the function block for the notification service.

mostAsFsDisable() disables the function service.

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 While Application Socket is active | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
