provider "google" {
  project = var.project_id
  region = "europe-west2"
}

resource "google_storage_bucket" "airbnb_data_bucket" {
  name          = var.bucket_name
  location      = "europe-west2"
  force_destroy = true

  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }
}
