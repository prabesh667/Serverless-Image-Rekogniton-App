# Serverless-Image-Rekogniton-App
Root directory is Image_object_rekognition.
Inside root directory has samconfig.toml, template.ymal and sub-directory Rekognition_function.
samconfig.toml file contains configuration parameters created while deploying the app using sam deploy.
template.yaml is the cloudformation template to create the required resources through stack to build the app. The resources created are S3 Bucket, DynamoDb Table, S3 bucket policies, IAM Rekognition Role.
Inside the sub-directory Rekognition_funtion lies Lambda function which is invoked by the S3 GetObject event and call the aws rekognition client for image tagging and results metadat are stored in the DynamoDB table.
