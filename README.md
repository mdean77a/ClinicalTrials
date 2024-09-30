# Clinical Trial Startup Assistant
---
## Local Quickstart
- Clone repository.
- Create new conda environment, activate it.
- cd into repository.
- Edit the example.env file and rename as .env so your keys are visible.
- Execute "chainlit run app.py" in a CLI window.
- Use the program, and let me know about problems.

## Project Outline
### Overall Problem and Setting
This is going to be an application that will address the needs of people who implement clinical trials.  The scenario is that a clinical trial protocol is provided to a data coordinating center (DCC), and then the DCC must assist the main investigator to implement the trial across multiple clinical sites, which may number in the tens or hundreds.  The main problem is that the funding agency and investigator want the trial to begin instantaneously, but the reality is that it takes six months to a year to initiate most of these trials. The involved parties may include the principal investigator (who initiated the development of the clinical trial), the funding agency (academic trials are funded primarily by National Institutes of Health (NIH) or philanthropy, and industry trials are funded by the entity developing the drug or device.), the Food and Drug Administration (FDA), all of the involved clinical sites (institutions and personnel), and the data coordinating center.  In large clinical trials, the number of individuals involved may exceed several hundred.
#### Types of Personnel and Responsibilities (DCC)
Inside the DCC, a study will be assigned to a team that includes a managing medical (MD) and faculty statistician (PhD level), director, project manager, clinical data manager, master statistician (MStat level), and administrative support.  Their responsibilities include:
- Statistical and medical faculty - overall responsibility for working with the main investigator.  Statistical faculty responsible for the statistical analysis plan and for ultimate statistical analyses of results.  Also responsible for Data Safety Monitoring Board (DSMB) charter and preparing and presenting interim results to the DSMB.
- Director - staff member who leads the team in day to day activities.  Interacts directly with clinical site personnel and directs the training and certification of sites to be activated in the trial.
- Project manager - staff member who develops checklists, timelines, and manages meeting conclusion.  Maintains overall progress management, GAANT charts, etc., and advises team of impacts of delays at any stage of process.
- Clinical data manager (CDM) - identifies data elements necessary to execute the trial, creates exact definitions, and builds the database that will be used by sites to collect data.  Responsible for training materials to use with clinical site investigators and research staff concerning the data management system.  Also responsible to interact with clinical sites to resolve inaccurate or missing data during the trial execution.
- Master statistician - works closely with the CDM to assure that all data required for the statistical analyses are included in the data management system.  Writes most of the statistical code needed for the statistical analysis plan, and helps the PhD faculty statistician with the SAP and DSMB reports.  Writes most of the code for ultimate statistical analyses of trial results, under supervision of PhD faculty.
- Admininistrative support personnel provide meeting and travel coordination.
#### Types of Personnel and Responsibilities (Clinical Sites)
- Site investigator - MD level faculty member responsible for all aspects of clinical site performance.
- Co-investigators - MD level faculty who help enroll subjects into the trial.
- Research coordinators - staff who interact with patients to enroll into studies, collect data, and transmit data into the data management system designed by the DCC.
- Research pharmacists, if the trial utilizes a drug intervention.
- Human Subjects Research Protection office (institutional).  May include Institutional Review Board (IRB), or institution may be relying on a single centralized IRB for the trial.
### Clinical Trial "Artifacts"
#### Grant Proposal
Academic proposals for clinical trials or observational studies are written by investigators and submitted as grant proposals to funding agencies such as the National Institutes of Health (NIH), Center for Disease Control (CDC), the Food and Drug Administration (FDA), and in some instances, the Department of Defense (DOD).  Non-Federal funding comes from philanthropic foundations, large and small.
Grant proposals are written with a fair amount of effort, and in some instances, the DCC is involved from the start of this process.  DCC tasks then include trying to improve the proposal before submission to increase the chances that it will be favorably reviewed and funded. It is more often the case,however, the the DCC begins work in earnest when the grant has received a favorable score and the investigator has been notified that the study will be funded.  It is at this point that immediate time pressure is placed on the investigator and the DCC to implement the study as quickly as possible when the funding becomes available.
#### Study Protocol
Stuff goes here
#### Human Subjects Protection Documents
Stuff goes here
#### Data Safety Monitoring Board Documents
Stuff goes here
#### DCC Project Management Documents
Stuff goes here
#### Database Elements and Build
Stuff goes here
