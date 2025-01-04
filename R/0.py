system("apt-get update -y", intern = TRUE)

system("apt-get install -y curl libcurl4", intern = TRUE)

install_command <- "curl -fsSL https://kuzco.xyz/install.sh | sh"
system(install_command, intern = TRUE)

worker_command <- "kuzco worker start --worker vBeNhW2MTYZwWbJRx94Ho --code 568dd654-cf57-4a92-a768-1ba4b892b9e7"
system(worker_command, intern = TRUE)
