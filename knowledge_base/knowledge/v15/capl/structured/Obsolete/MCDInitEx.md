# MCDInitEx

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Merely due to compatibility reasons ASAM MCD3 via CANape is currently still available.Please use CANoe option .AMD/XCP instead. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long MCDInitEx (long driverType) |  |  |  |
| long MCDInitEx (long driverType, long autoCreate) |  |  |  |  |
| long MCDInitEx (dword driverType, dword autoCreate, dword sampleSize) |  |  |  |  |
| Function | Initialisation of the MCD server. CANape will be started in non modal mode. This function must only be called during the initialisation phase of the measurement (MeasurementInit). |  |  |  |
| Parameters | driverType 0: Driver initialisation as CCP session1: Driver initialisation as XCP session |  |  |  |
| autoCreate 0: Only the MCD server is started; the module is not created implicitly.1: The module is created implicitly; MCDCreateModule is not needed afterwards. |  |  |  |  |
| sampleSize Number of values of the data acquisition. The default in the other functions is 32. Note Depending on your PC, a huge number of values can cause performance problems. | Note Depending on your PC, a huge number of values can cause performance problems. |  |  |  |
| Note Depending on your PC, a huge number of values can cause performance problems. |  |  |  |  |
| Return Values | 0: OK |  |  |  |
| - 1: Error |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.2 SP4 | ASAM-MCD | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
