variable instance_type {
  description = "The type instance EC2"
  type        = string
  default     = "t2.micro"
}



locals {
    instance_count = 2
    instance_name = act6-Ismael_dev1-David_dev2
}

resource "aws_instance" "example" {
  count         = local.instance_count
  ami           = "ami-0f70b01eb0d5c5caa" 
  instance_type = var.instance_type
  tags = {
    Name = "${local.instance_name}-${count.index + 1}"
  }
}

output "server_names" {
  value = aws_instance.ismaeldavid_server_terr_tags.Name
}