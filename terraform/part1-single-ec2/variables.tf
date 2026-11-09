variable "aws_region" {
  default = "ap-south-1"
}

variable "ami_id" {
  description = "Ubuntu 22.04 LTS AMI ID"
  default     = "ami-05552d2dcf89c9b78"
}

variable "instance_type" {
  default = "t2.micro"
}