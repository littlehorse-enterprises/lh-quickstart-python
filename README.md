<p align="center">
<img alt="LH" src="https://littlehorse.dev/img/logo.jpg" width="50%">
</p>

# LittleHorse Python QuickStart

- [LittleHorse Python QuickStart](#littlehorse-python-quickstart)
  - [Prerequisites](#prerequisites)
    - [Python Setup](#python-setup)
    - [LittleHorse CLI](#littlehorse-cli)
    - [Local LH Server Setup](#local-lh-server-setup)
    - [Verifying Setup](#verifying-setup)
  - [Running the Example](#running-the-example)
  - [Explaining the Code](#explaining-the-code)
  - [Advanced Topics](#advanced-topics)
    - [Inspect the TaskRun](#inspect-the-taskrun)
  - [Next Steps](#next-steps)

This repo contains a minimal example to get you started using LittleHorse in python. You can run this example in two ways:

1. Using a LittleHorse Server deployed in a cloud sandbox (to get one, contact `info@littlehorse.io`).
2. Using a local deployment of a LittleHorse Server (instructions below).

In this example, we will run a classic "Greeting" workflow as a quickstart. The workflow takes in one input variable (`input-name`), and calls a `greet` Task Function with the specified `input-name` as input.

## Prerequisites

Your system needs:
* `python` 3.8 or later
* `brew` (to install `lhctl`).

### Python Setup

We need a python environment that has the `littlehorse-client` pip package. To do that, you have two options:

Install via `pip`:

```
pip install littlehorse-client==0.5.1
```

Or, install via `poetry` using the configuration files in this repo:

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

If you have obtained a private LH Cloud Sandbox, you can skip this step and just follow the configuration instructions you received from the LittleHorse Team (remember to set your environment variables!).

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

First, we run `register_workflow.py`, which does two things:

1. Registers a `TaskDef` named `greet` with LittleHorse.
2. Registers a `WfSpec` named `quickstart` with LittleHorse.

```
python -m quickstart.register_workflow
```

You can inspect your `WfSpec` with `lhctl` as follows. It's ok if the response doesn't make sense, we have a UI coming really soon which visualizes it for you!

```bash
lhctl get wfSpec quickstart
```

Now, let's run our first `WfRun`! Use `lhctl` to run an instance of our `WfSpec`. 

```
# Run the 'quickstart' WfSpec, and set 'input-name' = "obi-wan"
lhctl run quickstart input-name obi-wan
```

The response prints the initial status of the `WfRun`. Pull out the `id` and copy it!

Let's look at our `WfRun` once again:

```
lhctl get wfRun <wf_run_id>
```

Note that the status is `RUNNING`! Why hasn't it completed? That's because we haven't yet started a worker which executes the `greet` tasks. Want to verify that? Let's search for all tasks in the queue which haven't been executed yet. You should see an entry whose `wfRunId` matches the Id from above:

```
lhctl search taskRun --taskDefName greet --status TASK_SCHEDULED
```

Now let's start our worker, shall we? Please run:

```
python -m quickstart.run_worker
```

Once the worker starts up, please open another terminal and inspect our `WfRun` again:

```
lhctl get wfRun <wf_run_id>
```

Voila! It's completed. You can also verify that the Task Queue is empty now that the Task Worker executed all of the tasks:

```
lhctl search taskRun --taskDefName greet --status TASK_SCHEDULED
```

## Explaining the Code



## Advanced Topics

Here are some cool commands which scratch the surface of observability offered to you by LittleHorse. Note that we are _almost_ done with a UI which will let you do this via click-ops rather than bash-ops. But anyways, the hard part is done, which is actually storing and indexing the data.

### Inspect the TaskRun



```
# Find your completed TaskRun
lhctl search taskRun --taskDefName greet --status TASK_SUCCESS

# Inspect the results of the TaskRun. A few things to note:

# Find completed WfRun's. You should see your favorite ID here!
lhctl search wfRun --wfSpecName quickstart --status COMPLETED

# Search for obi-wan's workflow
lhctl search variable --varType STR --name input-name --value obi-wan
```

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

## Next Steps

Want to do more cool stuff with LittleHorse and Python? You can find more Python examples [here](https://github.com/littlehorse-enterprises/littlehorse/tree/master/sdk-python). This example only shows rudimentary features like tasks and variables. Some additional features not covered in this quickstart include:

* Conditionals
* Loops
* External Events (webhooks/signals etc)
* Interrupts
* User Tasks
* Multi-Threaded Workflows
* Workflow Exception Handling

We also have quickstarts in [Java](https://github.com/littlehorse-enterprises/lh-quickstart-java) and [Go](https://github.com/littlehorse-enterprises/lh-quickstart-go). Support for .NET is coming soon.

Our extensive [documentation](www.littlehorse.dev) explains LittleHorse concepts in detail and shows you how take full advantage of our system.

Our LittleHorse Server is free for production use under the SSPL license. You can find our official docker image at the [AWS ECR Public Gallery](https://gallery.ecr.aws/littlehorse/lh-server). If you would like enterprise support, or a managed service (either in the cloud or on-prem), contact `info@littlehorse.io`.

Happy riding!
