variable "bucket_name" {
  default = "abcd"
}

variable "lambda_role_name" {
  default = "abcd"
}

variable "timeout" {
  default = 600
}
variable "runtime" {
  default = "python3.10"
}

variable "handler_name" {
  default = "function"
}
variable "function_name" {
  default = "lambda_handler"
}
variable "lambda_iam_policy_name" {
  default = "abcd"
}