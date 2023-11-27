locals {
  data_lake_bucket = "dtc_data_lake"
}

variable "project" {
  description = "enter your GCP project ID"
  type = string
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default = "northamerica-northeast1"
  type = string
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default = "STANDARD"
}

variable "BQ_DATASET" {
  description = "BigQuery Dataset that raw data (from GCS) will be written to"
  type = string
  default = "Covid_Data"
}


# variable "TABLE_NAME" {
#   description = "BigQuery Table"
#   type = string
#   default = "Covid_Drates"
# }









