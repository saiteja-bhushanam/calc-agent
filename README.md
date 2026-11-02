# calc-agent

Small LangGraph agent (`langchain.agents.create_agent`) for Amazon Bedrock AgentCore Runtime with calculator tools:
`add`, `multiply`, `delete` (removes a saved result), `list_saved`.

- `agent/` – agent code (`tools.py` plain functions, `main.py` AgentCore entrypoint)
- `infra/` – Terraform for ECR, IAM, runtime and endpoint
- `.github/workflows/deploy.yml` – test, build ARM64 image, `terraform apply` on `main`

## Run tests

    pip install pytest && pytest -q

## One-time setup

1. Create IAM roles trusting GitHub OIDC (build: ECR push; deploy: Terraform).
2. Set repo variables `AWS_BUILD_ROLE_ARN` and `AWS_DEPLOY_ROLE_ARN`.
3. Create a `prod` environment with required reviewers.
4. The first deploy needs the ECR repo and image to exist before the runtime is created:
   run `terraform apply -target=aws_ecr_repository.agent` once, then push to `main`.
5. Configure a remote Terraform backend in `infra/main.tf`.
