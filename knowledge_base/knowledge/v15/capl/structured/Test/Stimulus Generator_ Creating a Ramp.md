# Stimulus Generator: Creating a Ramp

> Category: `Test` | Type: `notes`

## Description

This Stimulus Generator generates a ramp. After the start the Stimulus Generator updates the data sink (signal or environment variable) periodically. Value A and value B describe the upper and lower limits of the ramp, respectively. The Reset Function of the Generator can be used either after a Generator stop or while it is operating (see below). In both cases the Reset Function causes the value of the data sink to immediately assume value A and the ramp begins anew. The Reset Function has no effect on the cycle time.

Stimulus Generator: Sample Code StmCreate_Ramp

| Note At least Time Up, Time High or Time Down have to be set to a value > 0. If check failed the measurement will be stopped. |
|---|

| Version 15© Vector Informatik GmbH |
|---|
