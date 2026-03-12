# Project Overview

## Objective
Simulate the work of an embedded Application Security / DevSecOps engineer securing and deploying a connected-vehicle-style telemetry API in AWS.

## Business Context
The service represents a vehicle-adjacent cloud API that accepts telemetry-like data, exposes operational endpoints, and requires secure deployment and runtime validation.

## What Was Demonstrated
- Secure API endpoint design
- Docker image packaging
- Terraform-based AWS provisioning
- ECR image lifecycle
- ECS Fargate deployment
- Live endpoint validation
- Runtime issue troubleshooting
- CI/CD security scanning with Semgrep and Trivy

## Most Important Lesson
Cloud security work is not only about building infrastructure. It also requires validating runtime behavior, interpreting failure signals, and feeding findings back into engineering and security decisions.
