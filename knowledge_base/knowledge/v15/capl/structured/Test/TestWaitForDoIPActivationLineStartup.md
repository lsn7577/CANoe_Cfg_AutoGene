# TestWaitForDoIPActivationLineStartup

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDoIPActivationLineStartup();
```

## Description

Wait until the DoIP Activation Line startup time has passed after start of the measurement. Please cf. Activation Line (DoIP).

## Example

Make sure that the startup time has passed in a test module or unit:

Explicitly deactivate Activation Line using the configured system variable to perform a specific test

```c
// If this testcase is run first, activation line startup will be observed
testcase ConnectToVehicle( char target[])
{
  TestWaitForDoIPActivationLineStartup(); // does nothing after startup 
time
  diagConnectChannel(target);             // form with target available since 9.0 SP3
}
SafeDoIPSending( diagRequest * req)
{
  TestWaitForDoIPActivationLineStartup(); // does nothing after startup time
  req.SendRequest();
}
testcase TC_CheckErrorWithoutActivationLine()
{
  char svActivationLine[100];
  char svActivationLineNS[100];
  long activationLineDelay;

  activationLineDelay = diagGetCommParameter(DoIP.ActivationLineStartuptime");
  if( activationLineDelay < 100)
  {
    TestStepWarning( "", "Activation Line startup time of %d is too low for this test. Ignored.", activationLineDelay);
    return;
  }
  // The entity needs enough time so that we can test if it reacts before the delay has passed

  diagCloseChannel();
  testWaitForDiagChannelClosed( 1000);

  if( 0 >= DiagGetCommParameter( "DoIP.ActivationLineSysvar", 0, svActivationLine, elcount( svActivationLine))
  || 0 >= DiagGetCommParameter( "DoIP.ActivationLineSysvarNamespace", 0, svActivationLineNS, elcount( svActivationLineNS)))
  {
    TestStepFail( "System variable to control Activation Line cannot be retrieved!");
    return;
  }

  TestStep( "", "Switch off Activation Line via system variable %s::%s", svActivationLineNS, svActivationLine);
  sysSetVariableInt( svActivationLineNS, svActivationLine, 0);
  TestWaitForTimeout( 500); // make sure the DoIP can go offline

  TestStep( "", "Switch on Activation Line via system variable %s::%s", svActivationLineNS, svActivationLine);
  sysSetVariableInt( svActivationLineNS, svActivationLine, 1);

  TestStep( "", "Do not give the entity enough time");
  TestWaitForTimeout( activationLineDelay - 100);

  TestStep( "", "Try to connect to vehicle - should fail since the startup time has not passed yet!");
  diagConnectChannel();
  if( 0 == testWaitForDiagChannelConnected( 3000))
  {
    TestStepPass( "Timeout connecting to DoIP entity before Activation Line delay passed, OK");
  } else
  {
    TestStepFail( "Connecting to the DoIP entity did not time out even though the startup time has not passed yet!");
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3 | — | — | — | 2.1 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
