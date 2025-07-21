# AI Multi-tool
An AI multi-tool that simplifies daily AI usage

# CI/CD 
## Deployment to Google Cloud
As an option for deployment, you can use GitHub Actions.

### Prerequisites
Before deployment you should create:
1. [Google Cloud Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects)

### Environments
For deployment using GitHub workflow you need to set in GitHub the following vars:
- GCP_PROJECT_ID

## Code Review
For reviewing the code, an integrated GitHub workflow for Claude is available following [this guide](https://docs.anthropic.com/en/docs/claude-code/github-actions).