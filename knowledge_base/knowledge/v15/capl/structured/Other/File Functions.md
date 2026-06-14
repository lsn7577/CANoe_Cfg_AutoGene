# File Functions

> Category: `Other` | Type: `notes`

## Description

There is often the need to save variables or measurement values over a period of time covering a number of measurements. File functions are provided in CAPL for this purpose.

While file access operations are generally conceived to be easy to use and reliable they are rather slow. Therefore file access should not be done in time-critical phases during measurement. It is recommended to use CAPL file access mainly in the on preStart and on stop event handlers.

File Access CAPL Functions | File Search Procedure |Configuration Requirements

| Note If file functions are used in CAPL programs in the Simulation Setup or test setup and CANoe is running in distributed mode or standalone mode, it is required to predefine the files to be accessed in advance under Configuration\|Options\|Extensions\|User Files. The files on the user computer and on the remote device are synchronized before measurement start and after measurement end. |
|---|

| Version 15© Vector Informatik GmbH |
|---|
