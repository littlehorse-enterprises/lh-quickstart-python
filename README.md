<p align="center">
<img alt="LH" src="https://littlehorse.dev/img/logo.jpg" width="50%">
</p>

# LittleHorse Python QuickStart

This repo contains a minimal example to get you started using LittleHorse in python. You can run this example in two ways:

1. Using a LittleHorse Server deployed in a cloud sandbox (to get one, contact `info@littlehorse.io`).
2. Using a local deployment of a LittleHorse Server (instructions below).

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

If you have obtained a private LH Cloud Sandbox, follow the configuration instructions you received from the LittleHorse Team and skip this step.

To run a LittleHorse Server locally in one command, you can run:

```
docker run --name littlehorse -d -p 2023:2023 public.ecr.aws/littlehorse/lh-standalone:latest
```

Using the local LittleHorse Server does not require any further configuration.

### Verifying Setup

You should be able to contact the LH Server:

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


```
python -m quickstart.main
```

In another terminal, use `lhctl` to run the workflow:

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

> More Python examples [here](https://github.com/littlehorse-enterprises/littlehorse/tree/master/sdk-python).
