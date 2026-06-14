# VTIL_SetVTStatus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SetVTStatus(dword cycleTime); // form 1
```

## Description

Forms (1) and (3): This function changes the cycle time of the VT Status message.The content of VT Status message stays unchanged.

Forms (2) and (4): This function changes the content and cycle time of the VT Status message.

## Return Values

0: Function has been executed successfully

## Example

```c
pg VT12 vt12;
vt12.VTFunctionVTtoECU = 254;
vt12.SourceAdressOfActiveWSM = 1;
vt12.VisibleDataAlarmMaskID = 1000;
vt12.VisibleSoftKeyMaskID = 2000;
vt12.VTBusyCode1 = 0;
vt12.VTBusyCode2 = 0;
vt12.VTBusyCode3 = 0;
vt12.VTBusyCode4 = 0;
vt12.VTBusyCode8 = 0;
vt12.VTFunctionCode = 0;
if (VTIL_SetVTStatus( VT, 1000, vt12 ) < 0)
{
  TestStepFail("Failed to set VT Status");
}
```

## Availability

| Since Version |
|---|
