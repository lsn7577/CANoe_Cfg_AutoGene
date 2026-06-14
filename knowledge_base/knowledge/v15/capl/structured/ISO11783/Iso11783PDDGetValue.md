# Iso11783PDDGetValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
float Iso11783PDDGetValue( dword ecuHandle, dbSignal signal, dword elementNumber );
float Iso11783PDDGetValue( dword ecuHandle, dword ddi, dword elementNumber );
```

## Description

The function requests the value of a process variable.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must previously have been created with Iso11783CreateECU. |
| signal | Signal from the database. The attribute ddimust be defined for the signal. The signal must be defined in the same database as the node! |
| ddi | Data Dictionary Identificator 0x000..0xFFFF |
| elementNumber | Element number, 0x000..0xFFF |

## Return Values

Value of the process variable, 0 if the variable is not defined

## Example

```c
char text[256];
value = Iso11783PDDGetValue
 ( ecuHandle, PD::AppRateSignal, 0;
if (Iso11783PDDGetLastError 
 () != 0) {
  Iso11783PDDGetLastErrorText 
 ( elCount(text), text );
  write( 
 "ERROR: %s", text );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
