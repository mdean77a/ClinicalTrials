import chainlit as cl
import os

async def create_consent_form(task_list):
    # Find the task in the task list
    task = next((t for t in task_list.tasks if t.title == "Create consent form"), None)
    
    # Create a single message for progress updates
    progress_msg = cl.Message(content="Creating consent form...")
    await progress_msg.send()

    if task:
        task.status = cl.TaskStatus.RUNNING
        await task_list.send()

    progress_msg.content = "Writing introduction paragraph"
  
    await progress_msg.update()
      # Routine to write intro paragraph
    await cl.sleep(1)
    progress_msg.content = "Introduction written."
    await progress_msg.update()
    
    progress_msg.content = "Writing human subjets risks"
    await progress_msg.update()
    await cl.sleep(1)
    progress_msg.content = "Human subjects risks written."
    await progress_msg.update()


    progress_msg.content = "Consent form created successfully."
    await progress_msg.update()

    if task:
        task.status = cl.TaskStatus.DONE
        task.progress = None  # Remove progress bar when done
        await task_list.send()

    # # Display directory contents
    # directory_path = "."  # This will show contents of the current directory
    # contents = get_directory_contents(directory_path)
    # await cl.Message(content=f"Directory contents:\n```\n{contents}\n```").send()

def get_directory_contents(path):
    contents = []
    try:
        items = os.listdir(path)
        items.sort(key=lambda x: (not os.path.isdir(os.path.join(path, x)), x.lower()))
        for item in items:
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                contents.append(f"📁 {item}/")
            elif os.path.isfile(full_path):
                contents.append(f"📄 {item}")
            else:
                contents.append(f"❓ {item}")
    except Exception as e:
        contents.append(f"Error reading directory: {str(e)}")
    return "\n".join(contents)

