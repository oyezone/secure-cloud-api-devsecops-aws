# Connected Vehicle Telemetry API Security Project

Production-style Application Security and DevSecOps portfolio project simulating a Toyota Connected-like cloud API environment in AWS.

## Executive Summary
I designed, secured, and deployed a connected-vehicle-style telemetry API to demonstrate the day-to-day work of an embedded AppSec / DevSecOps engineer. The project covers secure API development, Docker containerization, Terraform-based AWS provisioning, Amazon ECR image management, ECS Fargate deployment, live endpoint validation, and CI/CD security scanning with Semgrep and Trivy.

## Why This Project Matters
This project was built to mirror a real vehicle-adjacent cloud service where security must be embedded into engineering workflows rather than added after deployment. It demonstrates practical execution across application security, infrastructure as code, cloud deployment, runtime troubleshooting, and security automation.

## Scope
### Application
- FastAPI telemetry API
- Public and protected routes
- Live request validation and access-control testing

### Cloud
- AWS ECR
- AWS ECS Fargate
- CloudWatch Logs
- IAM execution role
- Security group and default VPC/subnet usage
- Terraform for infrastructure provisioning

### Security
- Semgrep SAST
- Trivy IaC/config scanning
- Live auth validation on public endpoints
- Cloud deployment troubleshooting and remediation

## Architecture Overview
Local development workstation  
→ Docker image build  
→ Amazon ECR image registry  
→ ECS Fargate runtime  
→ Public IP validation of live API endpoints

## Core Endpoints
- `/health`
- `/telemetry/upload`
- `/vehicle/{vehicle_id}/status`
- `/admin/diagnostics`

## Key Achievements
- Built a vehicle-adjacent telemetry API with FastAPI
- Containerized the service with Docker
- Provisioned AWS infrastructure using Terraform
- Created an ECR repository and pushed container images
- Deployed the application to ECS Fargate
- Validated live public API behavior over AWS-assigned public IP
- Confirmed unauthorized and authorized access behavior
- Integrated Semgrep and Trivy into a GitHub Actions security workflow
- Detected realistic infrastructure security findings
- Diagnosed and fixed an ECS runtime image architecture mismatch

## Featured Evidence
- [Live AWS health endpoint success](./evidence/52-public-ip-health-success.png)
- [Live AWS telemetry upload success](./evidence/53-public-ip-telemetry-success.png)
- [Live AWS admin unauthorized](./evidence/54-public-ip-admin-unauthorized.png)
- [Live AWS admin authorized](./evidence/55-public-ip-admin-authorized.png)
- [ECS task details after redeploy](./evidence/50-aws-ecs-task-details-after-redeploy.png)
- [CI/CD security workflow file](./evidence/60-github-actions-security-workflow-file.png)
- [Full evidence index](./docs/evidence-index.md)

## Most Important Technical Win
The initial ECS deployment failed because the image built on Apple Silicon did not match the runtime platform expected by ECS (`linux/amd64`). I identified the issue from ECS service events, rebuilt the image explicitly for amd64 using Docker Buildx, pushed the corrected image to ECR, forced a new ECS deployment, and confirmed the service reached steady state.

## Security Findings Identified
Examples of findings surfaced during the project:
- Mutable ECR image tags
- Broad outbound egress in the ECS security group
- Missing stronger observability hardening signals
- Opportunities to improve cloud logging and runtime visibility

These findings were treated as a practical remediation backlog rather than ignored as lab noise.

## Documentation
- [Project overview](./docs/project-overview.md)
- [Evidence index](./docs/evidence-index.md)

## Repository Layout
- `app/` — FastAPI application code
- `infra/terraform/` — Terraform infrastructure code
- `.github/workflows/` — GitHub Actions CI pipeline
- `docs/` — security notes and supporting documentation
- `evidence/` — screenshots and validation artifacts

## Interview Talking Points
This project supports discussion around:
- secure API design
- Terraform-based cloud provisioning
- container security and image lifecycle
- ECS Fargate deployment
- runtime troubleshooting
- CI/CD security integration
- shift-left security practices
- AppSec decision-making in cloud-native environments

## Next Improvements
- Make ECR tags immutable
- Tighten security group egress
- Add formal threat model documentation
- Strengthen authentication and authorization model
- Improve runtime monitoring and detection use cases
- Add pipeline gates based on severity thresholds

## Author
Oyelola Oyeneye  
GitHub: https://github.com/oyezone
