# Iso11783PDDOnDataChanged

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783PDDOnDataChanged( dword ecuHandle, dword ddi, dword elNum, double value );
```

## Description

This function can be implemented in the CAPL program. The function is called up by the node layer if a process variable has been changed with a value command via the CAN Bus.

## Return Values

—

## Example

```c
void Iso11783PDDOnDataChanged( dword ecuHandle, dword ddi, dword elNum, double value ){
  switch( ddi) {
    case 0x200:
      switch(elNum) {
        case 2:
          // set values of sections
          Iso11783PDDSetValue( Sprayer, 0x200. 3, value );
          Iso11783PDDSetValue( Sprayer, 0x200. 4, value );
          Iso11783PDDSetValue( Sprayer, 0x200. 5, value );
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

| Since Version |
|---|
