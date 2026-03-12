# Threat Model and Security Review

## Objective
Assess the security risks of a connected-vehicle-style telemetry API deployed in AWS and identify practical mitigations aligned with AppSec and DevSecOps workflows.

## System Overview
This project simulates a vehicle-adjacent cloud API that accepts telemetry-like data, exposes operational endpoints, and runs publicly on AWS ECS Fargate.

## In-Scope Components
- FastAPI application
- Public endpoints
- Protected admin diagnostics endpoint
- Docker container image
- Amazon ECR repository
- Amazon ECS Fargate service
- CloudWatch log group
- IAM execution role
- Security group
- Terraform-managed infrastructure
- GitHub Actions security workflow

## Key Assets
- telemetry payload data
- service availability
- container image integrity
- deployment configuration
- admin diagnostics access path
- AWS runtime credentials and permissions
- logs and operational visibility

## Actors
- legitimate client sending telemetry
- administrator using diagnostics endpoint
- external unauthenticated user
- malicious actor probing public API
- cloud operator / engineer
- CI/CD system

## Trust Boundaries
1. Internet to public ECS service
2. Public API routes to protected admin route
3. Local build environment to ECR
4. ECR image registry to ECS runtime
5. Terraform code to AWS control plane
6. GitHub Actions pipeline to source code and infrastructure code

## High-Level Data Flow
1. Client sends HTTP request to public AWS ECS service
2. FastAPI application processes request
3. Telemetry payload is accepted and returned in response flow
4. Protected diagnostics route requires authorization header
5. Docker image is built locally and pushed to ECR
6. ECS pulls image from ECR and runs task
7. Logs are sent to CloudWatch

## Threat Scenarios

### 1. Unauthorized access to admin diagnostics
- Risk: attacker attempts to call `/admin/diagnostics` without valid authorization
- Impact: sensitive diagnostic exposure
- Current control: bearer token check
- Improvement: replace static token approach with stronger auth model and secret management

### 2. Abuse of public telemetry upload endpoint
- Risk: attacker sends malformed, excessive, or automated requests
- Impact: availability degradation, noisy telemetry, possible abuse path
- Current control: structured API implementation
- Improvement: add request validation hardening, rate limiting, WAF, and monitoring thresholds

### 3. Mutable container image tag risk
- Risk: `latest` tag can be replaced with different image content
- Impact: integrity loss in deployment pipeline
- Current control: ECR image scanning enabled
- Improvement: make tags immutable and use versioned deployment tags

### 4. Broad security group egress
- Risk: compromised workload can communicate broadly outbound
- Impact: expanded attacker freedom and data exfiltration risk
- Current control: basic networking for lab simplicity
- Improvement: restrict outbound destinations to explicit required paths

### 5. Limited runtime observability
- Risk: inadequate visibility into suspicious behavior or deployment anomalies
- Impact: slower detection and response
- Current control: CloudWatch log group present
- Improvement: enable stronger monitoring, alarms, container insights, and detection use cases

### 6. Build/runtime architecture mismatch
- Risk: image built for wrong platform fails in runtime
- Impact: deployment failure and service outage
- Current control: corrected with explicit amd64 build
- Improvement: enforce platform-specific build step in CI/CD

### 7. Infrastructure misconfiguration drift
- Risk: insecure or inconsistent cloud settings over time
- Impact: exposure through configuration weakness
- Current control: Terraform-managed infrastructure
- Improvement: fail pipeline on critical IaC scan findings and track remediations

## Highest-Priority Risks
1. Mutable ECR image tags
2. Broad egress in ECS security group
3. Weak admin auth model
4. Limited runtime monitoring and detection

## Existing Security Measures Demonstrated
- protected admin route behavior
- unauthorized access validation
- authorized access validation
- Terraform-managed cloud provisioning
- ECR image scanning
- ECS runtime deployment validation
- Semgrep SAST integration
- Trivy IaC/config scanning
- explicit amd64 rebuild after runtime failure

## Recommended Next Mitigations
- enforce immutable ECR tags
- replace static bearer token with stronger auth pattern
- tighten security group egress
- add alarm-based detection for suspicious API behavior
- improve secrets handling
- add formal severity gates in CI/CD
- expand logging and monitoring coverage

## Interview Summary
This threat model shows how I think about assets, trust boundaries, abuse cases, cloud deployment risk, and practical mitigations in a vehicle-adjacent API environment. It also demonstrates that I treat security as a lifecycle activity spanning design, deployment, runtime validation, and remediation.
