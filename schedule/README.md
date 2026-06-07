Auto Commit Bot
Automatically commits to your GitHub repository 12 times per day (every 2 hours) using randomised conventional commit messages.

How It Works
GitHub Actions triggers auto_commit.py on a cron schedule.
The script picks a random commit type (feat, fix, docs, style, refactor, chore, perf) and a random message from that type's pool.
It appends a timestamped entry to activity_log.txt.
It commits and pushes that change back to the repo.
Setup (one-time)
1. Create a new public GitHub repository
Go to github.com/new, create a public repo, and clone it locally.

2. Copy these files into your repo root
Your repo should look like this:

your-repo/
├── .github/
│   └── workflows/
│       └── auto-commit.yml
├── activity_log.txt
├── auto_commit.py
└── README.md

3. Push to GitHub
git add .
git commit -m "chore: initial setup"
git push

4. Enable Actions (if not already)
Go to your repo → Actions tab → click "I understand my workflows, go ahead and enable them" if prompted.

Workflow Permissions
The workflow uses the built-in GITHUB_TOKEN — no extra setup needed.

Note: Commits made by GITHUB_TOKEN do not count toward your GitHub contribution graph because they're made by the github-actions[bot] user, not your personal account.

To make commits count on your profile: replace token: ${{ secrets.GITHUB_TOKEN }} in the workflow with a Personal Access Token (PAT):

Go to GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic).
Generate a token with repo scope.
Add it as a repository secret: repo → Settings → Secrets → Actions → New repository secret → name it PAT_TOKEN.
In auto-commit.yml, change ${{ secrets.GITHUB_TOKEN }} to ${{ secrets.PAT_TOKEN }}.
Manual Trigger
You can trigger a commit at any time without waiting for the schedule:

Repo → Actions → Auto Commit → Run workflow → Run workflow.

Customising the Schedule
The cron schedule in .github/workflows/auto-commit.yml runs every 2 hours (12×/day). To change frequency, edit the cron entries. Examples:

Frequency	Cron expression
Every hour (24×/day)	0 * * * *
Every 2 hours (12×/day)	0 */2 * * *
Every 3 hours (8×/day)	0 */3 * * *
Twice a day	0 9,18 * * *
GitHub Actions cron runs in UTC. Schedules may be delayed by up to 15 minutes during high load.

Adding Your Own Commit Messages
Edit the COMMIT_TEMPLATES dictionary in auto_commit.py. Each key is a commit type; each value is a list of messages. Add as many entries as you like.

"feat": [
    "feat: my custom message",
    ...
],