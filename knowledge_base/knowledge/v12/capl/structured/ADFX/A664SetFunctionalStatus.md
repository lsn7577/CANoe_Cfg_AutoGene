# A664SetFunctionalStatus

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664SetFunctionalStatus (PDU aPDU, BYTE fs)
```

## Description

This function sets the Functional Status (FS) of a AFDX-PDU (FDS).

Note: This function is only available in PDU-mode.

## Example

```c
PDU AFDX1::FDS_2_HSMU_DEMO_INT3 myPDU1; // define PDU from database
a664SetFunctionalStatus(myPDU1, 3);	    // set FS to Normal operation
myPDU1.IOM_DEMO_VFG_OIL_TEMP_A_32 = 0;	 // set a signal value in the PDU
TriggerPDU(myPDU1);	                   			// send PDU
```

## Availability

| Since Version |
|---|
