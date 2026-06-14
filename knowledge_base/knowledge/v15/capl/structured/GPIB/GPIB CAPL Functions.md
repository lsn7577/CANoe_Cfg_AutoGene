# GPIB CAPL Functions

> Category: `GPIB` | Type: `notes`

## Description

Error Code | Status | GPIB: Overview

| GPIB Only available with GPIB & CANoe. GPIB is a bus protocol for networking measurement devices. Equivalent names are: IEEE 488 HP-IB IEC In order to be able to use GPIB functionality, a GPIB controller must be installed on the system. |
|---|

| Functions | Short Description |
|---|---|
| GPIBDevChangePrimAddr | Changes the primary address of a device. |
| GPIBDevChangeSecAddr | Changes the secondary address of a device. |
| GPIBDevClear | Resets a device. |
| GPIBDevGotoLocal | Sets a device into local mode. |
| GPIBDevOnline | Activates/deactivates the device. |
| GPIBDevOpen | Opens a GPIB device and returns a device ID. |
| GPIBGetCnt | Returns the number of bytes transferred by the last GPIB operation. |
| GPIBGetCtrlLineStatus | Returns the status of the GPIB control lines. |
| GPIBGetError | Returns the error variable. |
| GPIBGetFloatResult | Helps functions for extracting numeric values from GPIB response strings. |
| GPIBGetIntResult | Helps functions for extracting numeric values from GPIB response strings. |
| GPIBGetStatus | Returns the status word. |
| GPIBOnError | Is called if a query or a write operation raised an error condition. |
| GPIBQuery | Query to the device. |
| GPIBQueryEx | Query to the device. |
| GPIBReqRelSysCtrl | Sets or deletes the permission to send interface clear (IFC) or remote enabler (REN). |
| GPIBResponse | Is called when the query returns. |
| GPIBWriteNum | Writes GPIB command and numeric value to the device. |
| GPIBWriteStr | Writes GPIB command to the device. |

| Note No explicit read functions are available. The response of GPIB devices is announced in the callback function GPIBResponse. Here users can implement their specific code. |
|---|

| Version 15© Vector Informatik GmbH |
|---|
