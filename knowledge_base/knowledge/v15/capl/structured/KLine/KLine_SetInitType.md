# KLine_SetInitType

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetInitType(long initType)
```

## Description

Configures the used initialization pattern.

Restriction: It is only possible to change the init type between the pre-configured init type an no init pattern. It is not possible to change between fast init and 5 baud init or vice versa.

## Parameters

| Name | Description |
|---|---|
| initType | Initialization pattern 1 = 5 baud init 2 = fast init 3 = no init pattern |

## Return Values

On success 0, otherwise a value less than 0.

## Example

Example shows a test case that makes sure that an ECU does not respond to a request after a S3 timeout.

```c
DiagRequest TesterPresent req;
long timeout_ms;
int status;
DiagSetTarget(“DUT”);

// Connect Channel
DiagConnectChannel()
status = TestWaitForDiagChannelConnected(2000);
   if (1 == status)
   {
      TestStepPass("Connected to target ECU");
   }
   else
   {
      TestStepFail("Error connecting to target ECU.”);
   }

req.SendRequest();
   if (1 != TestWaitForDiagRequestSent(req, 1000))
   {
      TestStepFail(“Request was not sent.”);
   }
   if (1 != TestWaitForDiagResponse(req, 1000))
   {
      TestStepFail(“No response received.”);
   }

// StopCommunication command shall NOT be  send after closing the channel.
KLine_SuppressAutomaticStopCommunication(1);
DiagCloseChannel();
   if (1== TestWaitForDiagChannelClosed(1000))
   {
      TestStepPass( "Channel closed successfully.");
   }
   else
   {
      TestStepFail( "Channel could not be closed.");
   }
   KLine_SetInitType(3);   // No Init

// Wait for a S3 timout
timeout_ms = 6000;
TestWaitForTimeout(timeout_ms);

// Send again a tester present request
req.SendRequest();
TestWaitForDiagRequestSent(req, 1000);
   if  (1 == TestWaitForDiagResponse(req, 1000))
   {
      TestStepFail(“Request answered in spite of  a S3 timeout ”);
   }
   else
   {
      TestStepPass(“Request not answered due to S3 timeout.”);
   }

DiagCloseChannel();
   if (1== TestWaitForDiagChannelClosed(1000))
   {
      TestStepPass( "Channel closed successfully.");
   }
   else
   {
   TestStepFail( "Channel could not be closed.");
   }

// Reset Settings
KLine_SetInitType(2); // Fast Init
KLine_SuppressAutomaticStopCommunication(0);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 8.0 | — | — | — | 1.1 SP2 |
| Restricted To | K-Line Real bus mode ECU tester | K-Line Real bus mode ECU simulation ECU tester | — | — | — | K-Line Real bus mode ECU simulation ECU tester |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
