# Tasks that can be accomplished by this application

# 1. Create consent form
# 2. Identify data elements
# 3. Create initiation checklist
# 4. Create DCC project checklist
# 5. Risk management plan
# 6. DSMB charter
# 7. IRB documents

from enum import Enum
from pydantic import BaseModel, Field

class TaskInfo(BaseModel):
    description: str = Field(..., min_length=1, max_length=100)
    estimated_time: int = Field(..., ge=1, le=480, description="Estimated time in minutes")

class Task(str, Enum):
    CREATE_CONSENT_FORM = "CREATE_CONSENT_FORM"
    IDENTIFY_DATA_ELEMENTS = "IDENTIFY_DATA_ELEMENTS"
    CREATE_INITIATION_CHECKLIST = "CREATE_INITIATION_CHECKLIST"
    CREATE_DCC_PROJECT_CHECKLIST = "CREATE_DCC_PROJECT_CHECKLIST"
    RISK_MANAGEMENT_PLAN = "RISK_MANAGEMENT_PLAN"
    DSMB_CHARTER = "DSMB_CHARTER"
    IRB_DOCUMENTS = "IRB_DOCUMENTS"

task_info = {
    Task.CREATE_CONSENT_FORM: TaskInfo(description="Create consent form", estimated_time=60),
    Task.IDENTIFY_DATA_ELEMENTS: TaskInfo(description="Identify data elements", estimated_time=45),
    Task.CREATE_INITIATION_CHECKLIST: TaskInfo(description="Create initiation checklist", estimated_time=30),
    Task.CREATE_DCC_PROJECT_CHECKLIST: TaskInfo(description="Create DCC project checklist", estimated_time=40),
    Task.RISK_MANAGEMENT_PLAN: TaskInfo(description="Risk management plan", estimated_time=90),
    Task.DSMB_CHARTER: TaskInfo(description="DSMB charter", estimated_time=120),
    Task.IRB_DOCUMENTS: TaskInfo(description="IRB documents", estimated_time=180),
}

def main():
    print("Tasks available:")
    for task, info in task_info.items():
        print(f"{task.value}: {info.description} (Estimated time: {info.estimated_time} minutes)")

if __name__ == "__main__":
    main()

