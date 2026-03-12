# Threat Model and Security Review

## Objective
Assess the security risks of a connected-vehicle-style telemetry API deployed in AWS and identify practical mitigations aligned with AppSec and DevSecOps workflows.

## Methodology
This threat model uses the **STRIDE** framework:
- **S**poofing
- **T**ampering
- **R**epudiation
- **I**nformation Disclosure
- **D**enial of Service
- **E**levation of Privilege

The goal is to evaluate how each STRIDE category could affect a vehicle-adjacent telemetry API and its supporting AWS deployment.

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

## STRIDE Analysis

### Spoofing
**Threat:** attacker pretends to be an authorized admin user or trusted telemetry source.  
**Example:** calling `/admin/diagnostics` with guessed or reused credentials.  
**Current control:** bearer token check on admin route.  
**Improvement:** replace static token with stronger auth pattern, better secret handling, and identity validation for privileged access.

### Tampering
**Threat:** attacker modifies requests, payloads, or deployment artifacts.  
**Example:** altered telemetry payloads or replacement of image content under a mutable `latest` tag.  
**Current control:** structured API implementation and ECR image scanning.  
**Improvement:** enforce immutable ECR tags, versioned image tags, stronger request validation, and integrity checks in pipeline.

### Repudiation
**Threat:** a caller performs actions and later denies having done so.  
**Example:** abusive use of telemetry or diagnostics endpoints without strong request attribution.  
**Current control:** CloudWatch log group is present for runtime logging.  
**Improvement:** stronger audit logging, request correlation, actor attribution, and alertable event tracking.

### Information Disclosure
**Threat:** sensitive information is exposed to unauthorized parties.  
**Example:** unauthorized access to diagnostics data or overexposed operational details.  
**Current control:** protected admin route and separation between public and privileged paths.  
**Improvement:** strengthen auth model, minimize sensitive output, and review logs and responses for unnecessary detail.

### Denial of Service
**Threat:** attacker degrades or exhausts service availability.  
**Example:** flooding the public `/telemetry/upload` endpoint with excessive requests or malformed payloads.  
**Current control:** basic service deployment and runtime validation.  
**Improvement:** rate limiting, WAF, monitoring thresholds, autoscaling considerations, and request-size validation.

### Elevation of Privilege
**Threat:** attacker gains more access than intended.  
**Example:** moving from public route access to diagnostics/admin-level access or abusing broad outbound permissions.  
**Current control:** separate protected endpoint and Terraform-managed IAM/runtime configuration.  
**Improvement:** stronger least privilege, tighter egress rules, better auth separation, and security review of administrative paths.

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
This threat model uses STRIDE to evaluate risks across API design, runtime deployment, image integrity, access control, and observability. It shows how security concerns can be translated into practical engineering mitigations in a vehicle-adjacent cloud environment.
