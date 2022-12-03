## pr-notifier
Printing out all PRs in the last 7 days using Github API

## Executing script instructions
1. Clone the repo:  
  **<code>git clone https://github.com/ranazrad/pr-notifier.git</code>**  
2. Change directory to pr-notifier:  
  **<code>cd pr-notifier</code>**  
3. Build the docker file:  
  **<code>docker build -t pr-notifier .</code>**  
4. Run the docker image to execute the script:  
  **<code>docker run pr-notifier</code>**  
5. View the stdout logs  
6. If no stdout logs, view container logs:  
  **<code>docker logs pr-notifier</code>**   

