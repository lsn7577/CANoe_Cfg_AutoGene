# Iso11783IL_PDDOnDataChanged

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_PDDOnDataChanged( dword ddi, dword elNum, double value );
```

## Description

This function can be implemented in the CAPL program. The function is called up by the interaction layer if a process variable has been changed with a value command via the CAN Bus.

## Parameters

| Name | Description |
|---|---|
| ddi | data dictionary identifier of the changed process variables |
| elementNumber | element number of the changed process variables |
| value | new value of the process variables |

## Return Values

—

## Example

```c
void Iso11783IL_PDDOnDataChanged( dword ddi, dword elNum, double value ){
  switch( ddi) {
    case 0x200:
      switch(elNum) {
        case 2:
          // set values of sections
          Iso11783IL_PDDSetValue( Sprayer, 0x200. 3, value );
          Iso11783IL_PDDSetValue( Sprayer, 0x200. 4, value );
          Iso11783IL_PDDSetValue( Sprayer, 0x200. 5, value );
          gOutputPerArea[0] = value;
          gOutputPerArea[1] = value;
          gOutputPerArea[2] = value;
          break;
        case 3:
          gOutputPerArea[0] = value;
          break;
        case 4:
          gOutputPerArea[1] = value;
          break;
        case 5:
          gOutputPerArea[2] = value;
          break;
      }
      break;
    case 0x402: // volume count
       switch(elNum) {
        case 1:
          gVolumeCount = value;
          break;
      }
      break;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
