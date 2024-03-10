#Goal: Take a mailbox (.mbox) file, then feed the different emails, grouped by subject, to Google Gemini for analysis and distilation

# file location: "C:\Users\andre\Documents\mailbox\[advisory-board-open].mbox"
# google takeout using the label of advisory board which uses a filter on the email 


import mailbox #for interacting with mbox files: advisoryboardmbox = mailbox.mbox("C:\\Users\\andre\\Documents\\mailbox\\[advisory-board-open].mbox")  # Open an mbox file
import os #for paths

script_dir = os.path.dirname(__file__)  # Get the directory of the current script
file_path = os.path.join(script_dir, '[advisory-board-open].mbox')

#printing debug
'''
for message in mbox:
    print("Subject:", message['subject'])
    #print("From:", message['from'])
    #print("Body Preview:", message.get_payload()[:1000])  # Get first 50 characters 
    #print("")
    counter ++

'''

#basic subject tracking which groups together messages that contain the same subject line
def group_emails_by_subject(mbox_path):
    mbox = mailbox.mbox(mbox_path)  # Open your mailbox file
    email_groups = {}

    for message in mbox:
        subject = message['subject']

        if subject not in email_groups:
            email_groups[subject] = []  # Create a new group if the subject is new

        email_groups[subject].append(message)

    return email_groups


mailbox_file = file_path

grouped_emails = group_emails_by_subject(mailbox_file)

keywords = ["GCIH", "Exam", "Job"]

for subject, email_list in grouped_emails.items():

    #Excludes any emails that are one of the keywords list above 
    #Excludes any email that does not have at least one response

    if (not any(keyword.lower() in subject.lower() for keyword in keywords)) and len(email_list) > 25:
        print("Subject:", subject)
        print("  Number of emails:", len(email_list))
        print("-" * 20)  # Optional separator
    
