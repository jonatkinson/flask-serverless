# flask-serverless

## Summary

This is a [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) template for creating a [`serverless`](https://github.com/serverless/serverless) application with [`Flask`](https://github.com/pallets/flask), with a custom domain.

`serverless` will handle creating the necessary resources in AWS:

- A lambda function to run the Flask code.
- An API Gateway instance for handling the domain and moving traffic.
- An S3 bucket to hold your deployments.

## Prerequisites

If you want to use a custom domain, you should have provisioned a certificate in AWS Certificate Manager, and have the certificate ARN to hand.

## Usage

First, clone this repository with cookiecutter.

    cookiecutter gh:jonatkinson/flask-serverless

## Todo

Currently, this is a very early stage repository; there is a lot of opportunity to expand the use of cookiecutter variables throughout. For now, search for the word 'example' in the repository to find the right places to customise.