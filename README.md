<h1 align="center"><img src="./Logo.png" height="20px"/> Rōblox: Freedom Distribution 2 <img src="./Logo.png" height="20px"/></h1>

<p align="right">
<a href="https://github.com/danyalassi/rfd-2/actions/workflows/main.yml"><img src="https://github.com/danyalassi/rfd-2/actions/workflows/main.yml/badge.svg"></a>
<a href="https://matrix.to/#/#robloxfreedomdistribution:matrix.org"><img src="https://matrix.org/images/matrix-logo.svg" height="20"></a>
</p>

_Want to host your own Rōblox LAN parties? Looking for a way to deploy your Rōblox experiences, new and old, on your own machine?_

Rōblox Freedom Distribution 2 is the solution you need. Building upon the original RFD project, this enhanced fork adds support for **2016L** and **2022M** Rōblox versions with full Studio hosting capabilities.

## What's New in RFD2

This fork adds the following major features to the original RFD project:

- **2016L Support**: Experience the classic 2016 Rōblox era with full compatibility
- **2022M Support**: Run modern Rōblox experiences with improved features
- **Integrated Studio Hosting**: Develop and test your experiences seamlessly with hosted Studio support
- **Improved Asset Compatibility**: Enhanced compatibility with modern Rōblox assets

## Introduction

Using RFD2, users can host their own server instances from compiled Rōblox binaries from:
- 2016-07-14 (2016L)
- 2018-07-25 (2018M)
- 2021-01-25 (2021E)
- 2022-10-13 (2022M)

Players can join existing servers with minimal configuration. Clients only need to keep track of which hosts and ports to connect to, as _clients will automatically connect to a server of the same version_.

**If you worked with Python 3.12+ before, [_initial_ setup](#download) is supposed to take less than a minute. Why _initial_? Freedom Distribution automatically downloads additional data (at most 90 MiB) for you.**

## Download

RFD2 is natively supported on Windows and works on GNU/Linux systems with `wine`.

### As an Executable

This is good for if you want to deploy quickly on any machine with connection to the internet.

#### For Windows

To download _as an executable_, run:

```
mkdir rfd2
cd rfd2
curl https://github.com/danyalassi/rfd-2/releases/latest/download/RFD-windows-latest.exe --output RFD.exe
```

To launch RFD2, your command line will look something like this:

```
./RFD.exe player -h 127.0.0.1 -p 2005
```

#### For GNU/Linux

RFD2 requires `wine` to be installed on your system.

For detailed instructions, consult [this guide](https://github.com/Windows81/Roblox-Freedom-Distribution/blob/main/Guides/Linux/README.MD).

```
mkdir rfd2
cd rfd2
curl https://github.com/danyalassi/rfd-2/releases/latest/download/RFD-windows-latest.exe --output RFD.exe
```

To launch RFD2, your command line will look something like this:

```
wine RFD.exe player -h 127.0.0.1 -p 2005
```

## Using the New Rōblox Versions

To specify which Rōblox version to use, modify your `GameConfig.toml` file:

```toml
[game_setup]
roblox_version = "2016L"  # Can be "2016L", "2018M", "2021E", or "2022M"
```

## Using Studio

The 2022M and 2016L versions include full Studio support. To launch Studio:

```
./RFD.exe studio --config ./GameConfig.toml
```

Or to connect to an existing server:

```
./RFD.exe studio --web_port 2006
```

## Quick Start Examples

### Running a 2016L Server

```shell
./RFD.exe server -p 2005 --config_path ./2016L-Config.toml
```

### Running a 2022M Server

```shell
./RFD.exe server -p 2005 --config_path ./2022M-Config.toml
```

### Connecting a Player

```shell
./RFD.exe player -h 127.0.0.1 -p 2005
```

## Credits

Rōblox Freedom Distribution 2 is a fork of the original [Rōblox Freedom Distribution](https://github.com/Windows81/Roblox-Freedom-Distribution) project by Windows81.

Initial adaptation from the [Rōblox Filtering Disabled](https://jetray.itch.io/roblox-filtering-disabled) project by Jetray, et al.

All the code is free-as-in-freedom software and is licensed under the GNU GPL v3.

## Copyright Acknowledgement

My use of Rōblox's binaries are prone to copyright-infringement issues. Be wary of any potential copyright takedowns.

In the event of a DMCA takedown, don't rely on forks of this repo on GitHub. Consider using other means. Also consult this [document](./LEGAL.md) if you want to know why I believe I'm protected under fair-use law.

---

<p align="center"><img src="./Logo.png" height="60px"/></p>