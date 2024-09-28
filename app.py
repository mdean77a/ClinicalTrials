# Importing the necessary libraries

import chainlit as cl
import sys
import os

# My file imports
import prompts
from create_consent_form import create_consent_form

tasks = []
task_list = None


# Define functions for each task

async def identify_data_elements():
    await cl.Message("Identifying data elements...").send()
    # Add your logic here to identify data elements
    await cl.Message("Data elements identified successfully.").send()

async def create_initiation_checklist():
    await cl.Message("Creating initiation checklist...").send()
    # Add your logic here to create the initiation checklist
    await cl.Message("Initiation checklist created successfully.").send()

# Add more functions for other tasks...

# Map task names to their corresponding functions
task_functions = {
    "Create consent form": create_consent_form,
    "Identify data elements": identify_data_elements,
    "Create initiation checklist": create_initiation_checklist,
    # Add more mappings for other tasks...
}

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content=prompts.welcome_message).send()
    options = [
        "Create consent form",
        "Identify data elements",
        "Create initiation checklist",
        "Create DCC project checklist",
        "Risk management plan",
        "DSMB charter",
        "IRB documents",
        "Done Selecting"
    ]
    
    # Initialize the task list
    task_list = cl.TaskList(title="Study Startup Tasks")
    
    while True:
        try:
            res = await cl.AskActionMessage(
                content="Please select one option:",
                actions=[
                    cl.Action(name="option", value=option, label=option)
                    for option in options
                ]
            ).send()

            if res is None:
                await cl.Message("No response received. Please try again.").send()
                continue

            selected_option = res.get("value")
            if selected_option == "Done Selecting":
                break
            elif selected_option:
                tasks.append(selected_option)
                # Add the task to the task list
                await task_list.add_task(cl.Task(title=selected_option, status=cl.TaskStatus.READY))
                await task_list.send()
                await cl.Message(f"You have selected: {tasks}").send()
            else:
                await cl.Message("No option was selected.").send()
        except Exception as e:
            await cl.Message(f"An error occurred: {str(e)}").send()
            break

    # Display the final selections
    if tasks:
        selections = "\n".join(f"- {task}" for task in tasks)
        await cl.Message(f"Your final selections:\n{selections}").send()
    else:
        await cl.Message("No tasks were selected.").send()

    ## HERE we need to ask for the protocol to be uploaded
    ## Then we need to chunk and vectorize, etc. and set up chains

# Add this new function to handle task completion
@cl.on_message
async def on_message(message: cl.Message):
    global task_list
    if task_list:
        for task in task_list.tasks:
            if task.title.lower() in message.content.lower():
                task.status = cl.TaskStatus.RUNNING
                await task_list.send()
                
                # Execute the task
                if task.title in task_functions:
                    await task_functions[task.title](task_list)
                    task.status = cl.TaskStatus.DONE
                else:
                    await cl.Message(f"No implementation found for task: {task.title}").send()
                    task.status = cl.TaskStatus.FAILED
                
                await task_list.send()


