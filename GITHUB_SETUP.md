# GitHub Setup Instructions

## Step 1: Create a New Repository on GitHub

1. Go to [https://github.com/new](https://github.com/new)
2. Repository name: `bug-tracker-qa-workflow`
3. Description: "Comprehensive QA portfolio project with Flask bug tracker and Selenium automation"
4. Choose: **Public** (for portfolio visibility)
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click **Create repository**

## Step 2: Push Your Local Repository to GitHub

After creating the repository, run these commands:

```powershell
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/bug-tracker-qa-workflow.git

# Rename the branch to main (GitHub's default)
git branch -M main

# Push your code to GitHub
git push -u origin main
```

## Step 3: Verify Your Repository

Visit your repository URL:
```
https://github.com/YOUR_USERNAME/bug-tracker-qa-workflow
```

## Step 4: Enable GitHub Actions (Optional)

1. Go to the **Actions** tab in your repository
2. Enable workflows
3. The CI/CD pipeline will run automatically on future pushes

## Alternative: Using GitHub Desktop

If you prefer a GUI:

1. Download [GitHub Desktop](https://desktop.github.com/)
2. Install and sign in with your GitHub account
3. Click: File → Add Local Repository
4. Select: `C:\Users\sgtsa\Documents\bug-tracker-qa-workflow`
5. Click: Publish repository
6. Choose visibility (Public recommended for portfolio)
7. Click: Publish Repository

## Updating Your Repository Later

```powershell
# Stage changes
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push
```

## Common Git Commands

```powershell
# Check status
git status

# View commit history
git log --oneline

# Create a new branch
git checkout -b feature-name

# Switch branches
git checkout main

# Pull latest changes
git pull
```

## Important Notes

- ✅ Your `.gitignore` is configured to exclude:
  - Virtual environments (.venv)
  - Python cache files (__pycache__)
  - SQLite databases (*.db)
  - Test reports and screenshots
  - IDE files

- ✅ Directory structure is preserved with `.gitkeep` files

- ✅ All source code and documentation is included

- ✅ GitHub Actions CI/CD workflow is ready to use

## Portfolio Tips

1. **Update README.md** with your actual GitHub username
2. **Add a badge** for build status (after first CI run)
3. **Add screenshots** to the README
4. **Pin this repository** on your GitHub profile
5. **Add topics** to your repo: qa, testing, selenium, flask, automation, portfolio

## Need Help?

If you encounter any issues:
- Check GitHub's [guide to pushing an existing repository](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github)
- Ensure you're logged into GitHub
- Make sure your GitHub account email matches your git config

---

**Next Steps After Pushing:**

1. Update README with your personal information
2. Add repository topics for discoverability
3. Enable GitHub Pages (optional - for hosting documentation)
4. Share the link in your portfolio/resume
