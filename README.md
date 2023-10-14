# LittleHorse Python QuickStart

- [LittleHorse Python QuickStart](#littlehorse-python-quickstart)
  - [Prerequisites](#prerequisites)
    - [Python Setup](#python-setup)
    - [LittleHorse CLI](#littlehorse-cli)
    - [Local LH Server Setup](#local-lh-server-setup)
    - [Verifying Setup](#verifying-setup)
  - [Running the Example](#running-the-example)
  - [What Just Happened?](#what-just-happened)

<p align="center">
<img alt="LH" src="https://littlehorse.dev/img/logo.jpg" width="50%">
</p>

This repo contains a minimal example to get you started using LittleHorse in python. You can run this example in two ways:

1. Using a LittleHorse Server deployed in a cloud sandbox (to get one, contact `info@littlehorse.io`).
2. Using a local deployment of a LittleHorse Server (instructions below).

In this example, we will run a classic "Greeting" workflow as a quickstart. The workflow takes in one input variable (`input-name`), and calls a `greet` Task Function with the specified `input-name` as input.

## Prerequisites

### Python Setup

First, you need to install python and also create a python environment that has the `littlehorse-client` pip package. To do that, you have two options:

Via `pip`:

```
pip install littlehorse-client==0.5.1
```

Or, via `poetry` using the configuration files in this repo:

```
poetry install
poetry shell # Don't forget this step!
```

### LittleHorse CLI

Install the LittleHorse CLI:

```
brew install littlehorse-enterprises/lh/lhctl
```

### Local LH Server Setup

If you have obtained a private LH Cloud Sandbox, you can skip this step and just follow the configuration instructions you received from the LittleHorse Team.

To run a LittleHorse Server locally in one command, you can run:

```
docker run --name littlehorse -d -p 2023:2023 public.ecr.aws/littlehorse/lh-standalone:latest
```

Using the local LittleHorse Server does not require any further configuration.

### Verifying Setup

At this point, whether you are using a local Docker deployment or a private LH Cloud Sandbox, you should be able to contact the LH Server:

```
-> lhctl search wfSpec
{
    "results": []
}
```

And you should be able to import the `littlehorse` python package:

```
-> python
>>> import littlehorse
>>>
```

## Running the Example

Without further ado, let's run the example start-to-finish.

First, we run `main.py`, which does three things:

1. Registers a `TaskDef` named `greet` with LittleHorse.
2. Registers a `WfSpec` named `quickstart` with LittleHorse.
3. Starts a Task Worker which listens to LittleHorse on the `greet` Task Queue, and executes `TaskRun`s as appropriate.

```
python -m quickstart.main
```

You can inspect your `WfSpec` with `lhctl` as follows. It's ok if the response doesn't make sense, we have a UI coming really soon which visualizes it for you!

```bash
lhctl get wfSpec quickstart
```

Now, let's run our first `WfRun`! Use `lhctl` to run an instance of our `WfSpec`. 

```
# Here, we specify that the "input-name" variable = "Obi-Wan"
lhctl run example-basic input-name Obi-Wan
```

Now let's inspect the result:

```
# This call shows the workflow specification
lhctl get wfSpec example-basic

# This call shows the result
lhctl get wfRun <wf run id>

# Inspect the first NodeRun of the WfRun
lhctl get nodeRun <wf run id> 0 1

# This shows the task run information
lhctl get taskRun <wfRunId> <taskGuid>
```

You can find more Python examples [here](https://github.com/littlehorse-enterprises/littlehorse/tree/master/sdk-python).

## What Just Happened?