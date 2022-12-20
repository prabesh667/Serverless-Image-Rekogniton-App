# Serverless-Image-Rekogniton-App
Root directory is Image_object_rekognition.
Inside root directory has samconfig.toml, template.ymal and sub-directory Rekognition_function.
samconfig.toml file contains configuration parameters created while deploying the app using sam deploy.
template.yaml is the cloudformation template to create the required resources through stack to build the app. The resources created are S3 Bucket, DynamoDb Table, S3 bucket policies, IAM Rekognition Role.
Inside the sub-directory Rekognition_funtion lies Lambda function which is invoked by the S3 GetObject event and call the aws rekognition client for image tagging and results metadat are stored in the DynamoDB table.
![template1-designer (2)](https://user-images.githubusercontent.com/57089950/208756547-6ce72dab-2953-43d2-a83d-7ecb78d7574b.png)
![serverless_rekognition_architecture](https://user-images.githubusercontent.com/57089950/208757075-b10e9476-f739-489d-a091-150fa873fa83.JPG)
