# testValidateSignalOutsideRangeByTxNode

> Category: `Obsolete` | Type: `notes`

## Description

or

| Deprecated Function This function replaces the function testValidateSignalOutsideRangeGM. Version 7.1: Replaced by testValidateSignalOutsideRange. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long testValidateSignalOutsideRangeByTxNode (char aTestStep[], dbSignal aSignal, dbNode aTxNode, float aLowLimit, float aHighLimit) |  |  |  |
| Function | Checks the signal value against the condition: Value < aLowLimit or Value > aHighLimit The test step is evaluated as passed or failed depending on the results. |  |  |  |
| Parameters | aTestStep Name of the test step for the test report |  |  |  |
| aSignal The signal to be polled |  |  |  |  |
| aTxNode Send node of the message whose signal should be polled |  |  |  |  |
| aLowLimit Lower limit of the signal value |  |  |  |  |
| aHighLimit Upper limit of the signal value |  |  |  |  |
| Return Values | -1: General error |  |  |  |
| 0: Correct functionality |  |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.1 | Test nodes | — | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
