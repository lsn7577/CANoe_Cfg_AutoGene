# Car2x Test Service Library

> Category: `Car2x` | Type: `notes`

## Description

The Car2x Test Service Library contains Wait Functions for Car2x messages and for Tokens in these messages.

Functions

Short Description

Joins a Car2X message which has a signal that is inside or equals the given limits to the current set of waiting events.

Joins a Car2X message which has a signal that matches the given value to the current set of waiting events.

Waits for a Car2x message.

Waits for a Car2X message which has a signal that is inside or equals the given limits.

Waits for a Car2X message which has a signal that matches the given value.

| Functions | Short Description |
|---|---|
| C2xTestGetWaitForMessage | Retrieves the Car2x message that has led to the resume of the last wait statement. |
| C2xTestJoinMessage | Joins a Car2x message to the current set of waiting events. |
| C2xTestJoinSignalInRange | Joins a Car2X message which has a signal that is inside or equals the given limits to the current set of waiting events. |
| C2xTestJoinSignalMatch | Joins a Car2X message which has a signal that matches the given value to the current set of waiting events. |
| C2xTestWaitForMessage | Waits for a Car2x message. |
| C2xTestWaitForSignalInRange | Waits for a Car2X message which has a signal that is inside or equals the given limits. |
| C2xTestWaitForSignalMatch | Waits for a Car2X message which has a signal that matches the given value. |

| Version 15© Vector Informatik GmbH |
|---|
