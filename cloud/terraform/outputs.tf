output "bucket_url" {
  value = "gs://${google_storage_bucket.airbnb_data_bucket.name}"
}