import requests
from datetime import datetime , timedelta

# Using Github API reference for executing the call
# https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-pull-requests
# PR state can be one of: open, closed, all
# Default PR state: open
# We need only open , closed

owner = "ranazrad"
repository = "pr-notifier"

def printPRs(state):
    body = ""
    prsCount = 0
    # API call to collect a list of all PRs
    queryParams = {'state':state}
    response = requests.get("https://api.github.com/repos/" + owner + "/" + repository + "/pulls", params=queryParams)

    # Get the valid time
    stateTime = "closed_at"
    if(state=="open"):
        stateTime = "created_at"

    # Traverse each PR and print the details of those within past 7 days
    for pr in response.json():
        prCreatedTime = datetime.strptime(pr[stateTime], "%Y-%m-%dT%H:%M:%SZ")
        isLastSevenDaysPR = datetime.now() - prCreatedTime < timedelta(days=7)
        if(isLastSevenDaysPR):
            prsCount += 1
            body += "============PR #" + str(pr["number"]) + "============\n"
            body += "ID: " + str(pr["id"]) + "\n"
            body += "URL: " + str(pr["url"]) + "\n"
            body += "Author: " + str(pr["user"]["login"]) + "\n"
            body += "From branch: " + str(pr["head"]["ref"]) + "\n"
            body += "Into branch: " + str(pr["base"]["ref"]) + "\n"
            body += "Date: " + str(pr[stateTime]) + "\n"
            body += "Title: " + str(pr["title"]) + "\n"
            body += "Description: " + str(pr["body"]) + "\n"
            body += "\n\n\n"
            

    # Check if PRs exist
    if prsCount == 0:
        body += "\nNo " + state + " PRs for the past 7 days\n"

    if prsCount > 0:
        body = "\nYou have " + str(prsCount) + " " + state + " PRs for the past 7 days\n\n" + body

    return body

mailFrom = "pr.notifier@sailpoint.com"
mailTo = "scrum.master@sailpoint.com"
mailSubject = "Past 7 days PRs - SailPoint Repos"
mailBody = printPRs('open')
mailBody += printPRs('closed')

print("\nSending Mail...\nFrom: " + mailFrom + "\nTo: " + mailTo + "\nMail Subject: " + mailSubject + "\nMail Body: " + mailBody)
