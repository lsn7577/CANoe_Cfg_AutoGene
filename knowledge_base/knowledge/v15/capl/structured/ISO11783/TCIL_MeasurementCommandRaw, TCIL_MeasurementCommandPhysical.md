# TCIL_MeasurementCommandRaw, TCIL_MeasurementCommandPhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_MeasurementCommandRaw(dbNode client, dword ddi, dword elementNumber, char[] logTriggerType, long triggerValue); // form 1
long TCIL_MeasurementCommandRaw(dword addressClient, dword ddi, dword elementNumber, char[] logTriggerType, long triggerValue); // form 2
long TCIL_MeasurementCommandRaw(dbNode tc, dbNode client, dword ddi, dword elementNumber, char[] logTriggerType, long triggerValue); // form 3
long TCIL_MeasurementCommandRaw(dbNode tc, dword addressClient, dword ddi, dword elementNumber, char[] logTriggerType, long triggerValue); // form 4
long TCIL_MeasurementCommandPhysical(dbNode client, dword ddi, dword elementNumber, char[] logTriggerType, double triggerValue); // form 5
long TCIL_MeasurementCommandPhysical(dword addressClient, dword ddi, dword elementNumber, char[] logTriggerType, double triggerValue); // form 6
long TCIL_MeasurementCommandPhysical(dbNode tc, dbNode client, dword ddi, dword elementNumber, char[] logTriggerType, double triggerValue); // form 7
long TCIL_MeasurementCommandPhysical(dbNode tc, dword addressClient, dword ddi, dword elementNumber, char[] logTriggerType, double triggerValue); // form 8
```

## Description

These functions send a trigger definition to the client.

## Parameters

| Name | Description |
|---|---|
| tc | Task Controller simulation node to apply the function. |
| client | Task Controller client node the TC sends the Measurement command to. |
| addressClient | Address of the Task Controller client node the TC sends the Measurement command to. |
| elementNumber | Element number, 0x000..0xFFF. |
| ddi | Data dictionary identifier, 0x0000..0xFFFF. |
| logTriggerType | value |
| time_interval | The client has to send the value of the data element to the TC or DL cyclic with this time interval = triggerValue. 0 stops measurement, 100 ms is the minimum time interval. Unit: milliseconds. |
| distance_interval | The client has to send the value of the data element to the TC or DL cyclic with this distance interval = triggerValue. 0 stops measurement. Unit: millimeters |
| min_within_threshold | The client has to send the value of the data element to the TC or DL when the value is higher than the triggerValue. (231-1) or 7FFFFFFFh stops measurement. Unit: as specified by the DDI definition. |
| max_within_threshold | The client has to send the value of the data element to the TC or DL when the value is lower than the triggerValue. (-231+1) or 80000001h stops measurement. Unit: as specified by the DDI definition. |
| change_threshold | The client has to send the value of the data element to the TC or DL when the value change is higher than or equal to the triggerValue since last transmission. 0 stops measurement, 1 logs each change. Unit: as specified by the DDI definition. |
| triggerValue | Raw or physical logging trigger value. |

## Example

Example form 3

Example form 7

```c
void StartDistanceTrigger(dword ddi, dword elementNumber, dword distance)
{
  long result;
  result = TCIL_MeasurementCommandRaw(TC, Sprayer, ddi, elementNumber, "distance_interval", distance);
  switch (result)
  {
    case     0: TestStepPass(); break;
    case -2202: TestStepFail("Function is not available in passive mode of the TC IL!"); break;
    case -2204: TestStepFail("Node 'Sprayer' is no client device!"); break;
    case -2206: TestStepFail("Task Controller IL is currently not online!"); break;
    case -2210: TestStepFail("Failed to send Measurement command!"); break;
    default:    TestStepFail("Unexpected error"); break;
  }
}

void StopMinWithinThresholdTrigger(dword ddi, dword elementNumber)
{
  long result;
  result = TCIL_MeasurementCommandRaw(TC, Sprayer, ddi, elementNumber, "min_within_threshold", 0x7FFFFFFF);
  switch (result)
  {
    case 0 : TestStepPass(); break;
    default: TestStepFail("StopMinWithinThresholdTrigger", "Unexpected error (error code %i)", result); break;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0: form 1, 3, 5, 7 13.0: form 2, 4, 6, 8 | 13.0 | — | — | 2.1: form 5, 7 5.0: form 6, 8 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 5, 6, 7, 8 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2, 3, 4) | ✔ (form 1, 2, 3, 4) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form form 5, 6, 7, 8) | ✔ (form form 5, 6, 7, 8) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form form 5, 6, 7, 8) | ✔ (form form 5, 6, 7, 8) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
