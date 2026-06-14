# Unconditional (Boxed) Event Procedures

> Category: `Other` | Type: `notes`

## Description

Normally, the generic event procedures (e.g. on message *) are only called if there is no more specific event procedure in the program for the message which is received.

on message 100{ write("specific");}on message *{ write("generic");}

If you want to implement an event procedure which is called always, regardless of other event procedures, you can use a "boxed" event procedure signified by [*].

on message 100{ write("specific");}on message [*]{ write("generic");}

The "boxed" event procedures are always called before other, possibly more specific event procedures in the program.

You may use a "boxed" event procedure with the following message types:

Event Procedures

| Note The usage of "boxed" event procedures is not compatible to older versions of CANoe. They can only be used in CAPL programs with CANoe version 7.0 and higher. |
|---|

| Example on message 100{ write("specific");}on message *{ write("generic");} If the message 100 is received, the output in the Write Window will be "specific" only. |
|---|

| Example on message 100{ write("specific");}on message [*]{ write("generic");} If the message 100 is received, the output in the Write Window will be "generic" followed by "specific". |
|---|

| Note If you implement a "boxed" event procedure in the measurement setup, you should not call output(this) because of the danger of transmitting the message two times, once in the "boxed" event procedure and once in the specific event procedure. Call output(this) only in specific event procedures and unboxed generic event procedures. |
|---|

| Version 15© Vector Informatik GmbH |
|---|
