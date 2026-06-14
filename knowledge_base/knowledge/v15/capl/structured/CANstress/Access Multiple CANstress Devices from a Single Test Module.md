# Access Multiple CANstress Devices from a Single Test Module

> Category: `CANstress` | Type: `notes`

## Description

With previous versions of CANstress NL DLL, it was only possible to access a single CANstress device from a single test module. Since Version 2.0 of the CANstress NL DLL, it is possible to control as many CANstress devices as you like from a single test module. To do this you need to configure the available CANstress devices in the CANoe options:

Please also note the information on help page CANstress and Distributed Mode/VN8900 if you are using distributed mode or a VN8900.

To establish a connection to a specific CANstress device, you need to use the CANstressCreateServer command with the alias or number of a configured CANstress device as a parameter. You will then obtain a handle, which you can use to switch between different devices. To do this, you need to use the CANstressSetDevice function with the relevant handle as a parameter.

The NodeLayer DLL will recognize the set CANstress device. When CANstressCreateServer or CANstressSetDevice is called, the following calls to CANstress CAPL functions are executed on the set device.

// Check that CANstress devices have been configured

if (CANstressAvailableDevices() < 2){TestCaseFail();Write("Number of configured CANstress devices is less than 2!"); }

// Establish connection to "cstCAN1"deviceId1 = CANstressCreateServer("cstCAN1");CANstressConnect();

// Establish connection to "cstCAN2"deviceId2 = CANstressCreateServer("cstCAN2");CANstressConnect();

// The following commands are executed on "cstCAN2"CANstressOpen(".\\CANstress\\EngineData_BusOff.cst");

CANstressSetDevice(deviceId1);

// The following commands are executed on "cstCAN1"CANstressOpen(".\\CANstress\\EngineData_BusOff.cst");

| Example // Check that CANstress devices have been configured if (CANstressAvailableDevices() < 2){TestCaseFail();Write("Number of configured CANstress devices is less than 2!"); } // Establish connection to "cstCAN1"deviceId1 = CANstressCreateServer("cstCAN1");CANstressConnect(); // Establish connection to "cstCAN2"deviceId2 = CANstressCreateServer("cstCAN2");CANstressConnect(); // The following commands are executed on "cstCAN2"CANstressOpen(".\\CANstress\\EngineData_BusOff.cst"); CANstressSetDevice(deviceId1); // The following commands are executed on "cstCAN1"CANstressOpen(".\\CANstress\\EngineData_BusOff.cst"); |
|---|

| Version 15© Vector Informatik GmbH |
|---|
