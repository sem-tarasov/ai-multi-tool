# AI Multi-tool
An AI multi-tool that simplifies daily AI usage

# CI/CD 
## Deployment to Google Cloud
As an option for deployment, you can use GitHub Actions. 
Example for deployment to Google Cloud is described in [this file](./.github/workflows/google.yml).

### Prerequiesits
Before deployment you should create:
1. [Google Cloud Project](https://cloud.google.com/resource-manager/docs/creating-managing-projects)

### Enviroments
For deployment using GitHUb workflow you need to set in GitHub next vars:
- GCP_PROJECT_ID

## Code Review
For reviewing the code, an integrated GitHub workflow for Claude is available following [this guide](https://docs.anthropic.com/en/docs/claude-code/github-actions).